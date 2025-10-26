#!/usr/bin/env python3
"""
Mermaid Documentation Update Script

This script automates the process of updating the Mermaid documentation
by downloading the latest version from the GitHub repository.
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path


def run_command(cmd, description, check=True, capture_output=False):
    """Run a shell command and handle errors."""
    print(f"🔄 {description}...")
    try:
        if capture_output:
            result = subprocess.run(cmd, shell=True, check=check,
                                  capture_output=True, text=True)
            return result.stdout.strip()
        else:
            subprocess.run(cmd, shell=True, check=check)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error {description}: {e}")
        if capture_output:
            print(f"Output: {e.output}")
        return False


def check_gh_available():
    """Check if gh CLI is available."""
    return run_command("gh --version", "Checking if gh CLI is available",
                      check=False, capture_output=True) is not None


def backup_existing_docs():
    """Backup existing mermaid_docs directory."""
    if Path("mermaid_docs").exists():
        print("📁 Found existing mermaid_docs directory")

        # Remove old backup if it exists
        if Path("mermaid_docs_old").exists():
            print("🗑️  Removing existing mermaid_docs_old directory")
            shutil.rmtree("mermaid_docs_old")

        # Rename current directory
        print("📝 Renaming mermaid_docs to mermaid_docs_old")
        shutil.move("mermaid_docs", "mermaid_docs_old")
        return True
    return False


def clone_repository():
    """Clone the mermaid repository to a temporary location."""
    temp_repo = "temp-mermaid-repo"

    # Remove existing temp repo if it exists
    if Path(temp_repo).exists():
        try:
            shutil.rmtree(temp_repo, ignore_errors=True)
        except Exception:
            pass

    success = run_command(
        f"gh repo clone mermaid-js/mermaid {temp_repo} -- --depth 1",
        "Cloning mermaid repository (shallow clone)"
    )

    if success:
        return temp_repo
    return None


def copy_docs_files(temp_repo):
    """Copy documentation files from the cloned repository."""
    source_path = Path(temp_repo) / "packages" / "mermaid" / "src" / "docs"
    target_path = Path("mermaid_docs")

    if not source_path.exists():
        print(f"❌ Source path does not exist: {source_path}")
        return False

    # Create target directory
    target_path.mkdir(exist_ok=True)

    try:
        # Copy only relevant documentation files and directories
        for item in source_path.iterdir():
            try:
                # Skip hidden directories (starting with .)
                if item.is_dir() and item.name.startswith('.'):
                    continue

                if item.is_file():
                    # Only copy .md files
                    if item.suffix.lower() == '.md':
                        shutil.copy2(item, target_path / item.name)
                        print(f"  📄 Copied: {item.name}")
                elif item.is_dir():
                    # Copy directory and filter its contents later
                    shutil.copytree(item, target_path / item.name, dirs_exist_ok=True)
                    print(f"  📁 Copied directory: {item.name}")
            except PermissionError:
                # Skip files we can't access
                continue

        # Filter the copied directories to only keep .md files and non-empty directories
        filter_documentation_files(target_path)

        print("✅ Copying and filtering documentation files completed successfully")
        return True
    except Exception as e:
        print(f"❌ Error copying documentation files: {e}")
        return False


def filter_documentation_files(target_path):
    """Filter directory to only keep .md files and remove empty directories."""
    print("🔍 Filtering documentation files...")

    def filter_directory(directory):
        """Recursively filter a directory."""
        if not directory.is_dir():
            return True

        items_to_remove = []
        subdirs_to_check = []

        for item in directory.iterdir():
            if item.is_file():
                # Remove non-.md files
                if item.suffix.lower() != '.md':
                    items_to_remove.append(item)
            elif item.is_dir():
                subdirs_to_check.append(item)

        # First, filter subdirectories recursively
        for subdir in subdirs_to_check:
            if not filter_directory(subdir):
                items_to_remove.append(subdir)

        # Remove files that aren't .md files
        for item in items_to_remove:
            try:
                if item.is_file():
                    item.unlink()
                    print(f"    🗑️  Removed file: {item.relative_to(target_path)}")
                elif item.is_dir():
                    shutil.rmtree(item)
                    print(f"    🗑️  Removed directory: {item.relative_to(target_path)}")
            except Exception as e:
                print(f"    ⚠️  Could not remove {item}: {e}")

        # Check if directory is now empty (excluding this check itself)
        try:
            remaining_items = list(directory.iterdir())
            return len(remaining_items) > 0
        except Exception:
            return False

    # Apply filtering to all subdirectories
    for item in target_path.iterdir():
        if item.is_dir():
            filter_directory(item)

    print("✅ Documentation filtering completed")

    # Clean up empty directories at the end
    remove_empty_directories(target_path)


def remove_empty_directories(target_path):
    """Remove empty directories from the documentation."""
    print("🧹 Removing empty directories...")

    def remove_empty_dirs(directory):
        """Recursively remove empty directories."""
        removed_any = False
        try:
            # First, process subdirectories
            for item in list(directory.iterdir()):
                if item.is_dir():
                    if remove_empty_dirs(item):
                        removed_any = True

            # Check if current directory is empty (excluding . and ..)
            items = list(directory.iterdir())
            if len(items) == 0:
                # Don't remove the root directory
                if directory != target_path:
                    try:
                        directory.rmdir()
                        print(f"    🗑️  Removed empty directory: {directory.relative_to(target_path)}")
                        return True
                    except Exception as e:
                        print(f"    ⚠️  Could not remove empty directory {directory}: {e}")
        except Exception as e:
            print(f"    ⚠️  Error processing directory {directory}: {e}")

        return removed_any

    # Run the cleanup until no more empty directories are found
    while remove_empty_dirs(target_path):
        pass

    print("✅ Empty directory cleanup completed")


def cleanup_temp_repo(temp_repo):
    """Clean up the temporary repository."""
    if not temp_repo:
        return

    temp_path = Path(temp_repo)
    if temp_path.exists():
        try:
            # First try to remove read-only attributes (Windows issue)
            if os.name == 'nt':  # Windows
                import stat
                for root, dirs, files in os.walk(temp_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        try:
                            os.chmod(file_path, stat.S_IWRITE)
                        except Exception:
                            pass

            # Now remove the directory
            shutil.rmtree(temp_path, ignore_errors=True)

            # Verify it's actually gone
            if temp_path.exists():
                # If still exists, try one more time with a different approach
                import time
                time.sleep(0.1)  # Small delay for Windows file system
                try:
                    shutil.rmtree(temp_path, ignore_errors=True)
                except Exception:
                    pass

            if not temp_path.exists():
                print("🧹 Cleaned up temporary repository")
            else:
                print(f"⚠️  Warning: Could not completely remove temp repository: {temp_repo}")

        except Exception as e:
            print(f"⚠️  Warning: Could not fully clean up temp repository: {e}")


def verify_download():
    """Verify that files were downloaded successfully."""
    target_path = Path("mermaid_docs")
    if not target_path.exists():
        return False

    # Check for key .md files
    key_files = ["index.md"]
    for file_name in key_files:
        if not (target_path / file_name).exists():
            print(f"❌ Missing key file: {file_name}")
            return False

    # Count .md files and directories to ensure we got documentation
    try:
        md_files = list(target_path.rglob("*.md"))
        directories = [item for item in target_path.rglob("*") if item.is_dir()]
        total_items = len(md_files) + len(directories)

        print(f"✅ Downloaded {len(md_files)} .md files and {len(directories)} directories")

        # Should have at least some .md files
        return len(md_files) > 0
    except Exception:
        return False


def ask_cleanup_old_docs():
    """Ask user if they want to delete the old documentation."""
    if Path("mermaid_docs_old").exists():
        print("\n🗑️  Old documentation directory exists: mermaid_docs_old")
        try:
            response = input("Delete mermaid_docs_old? (y/N): ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            # Default to 'no' if input fails
            response = 'n'

        if response in ['y', 'yes', '']:
            try:
                shutil.rmtree("mermaid_docs_old")
                print("✅ Removed mermaid_docs_old directory")
                return True
            except Exception as e:
                print(f"❌ Error removing mermaid_docs_old: {e}")
                return False
        else:
            print("ℹ️  Keeping mermaid_docs_old directory")
            return False
    return True


def rollback_backup():
    """Rollback by restoring the backup if something went wrong."""
    if Path("mermaid_docs_old").exists():
        if Path("mermaid_docs").exists():
            shutil.rmtree("mermaid_docs")
        shutil.move("mermaid_docs_old", "mermaid_docs")
        print("🔄 Restored backup documentation")


def main():
    """Main function to update documentation."""
    print("🚀 Starting Mermaid documentation update...")

    # Check prerequisites
    if not check_gh_available():
        print("❌ gh CLI is not available. Please install GitHub CLI first.")
        sys.exit(1)

    temp_repo = None
    backup_existed = False

    try:
        # Step 1: Backup existing docs
        backup_existed = backup_existing_docs()

        # Step 2: Clone repository
        temp_repo = clone_repository()
        if not temp_repo:
            print("❌ Failed to clone repository")
            if backup_existed:
                rollback_backup()
            sys.exit(1)

        # Step 3: Copy files
        if not copy_docs_files(temp_repo):
            print("❌ Failed to copy documentation files")
            if backup_existed:
                rollback_backup()
            sys.exit(1)

        # Step 4: Verify download
        if not verify_download():
            print("❌ Download verification failed")
            if backup_existed:
                rollback_backup()
            sys.exit(1)

        print("\n🎉 Documentation update completed successfully!")

        # Step 5: Ask about cleanup
        ask_cleanup_old_docs()

    except KeyboardInterrupt:
        print("\n⚠️  Update interrupted by user")
        if backup_existed:
            rollback_backup()
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        if backup_existed:
            rollback_backup()
        sys.exit(1)
    finally:
        # Always cleanup temporary repository
        if temp_repo:
            cleanup_temp_repo(temp_repo)


if __name__ == "__main__":
    main()