Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
"""
setup_data_dirs.py

Sets up the FinTrust portfolio data directory structure
and reports what's there.

"""

import sys
import os
from pathlib import Path
from datetime import date


def setup_directories(base_dir):
    """Create the standard FinTrust data directory structure."""
    
    dirs = [
        base_dir / "transactions" / "current",
        base_dir / "transactions" / "archive",
        base_dir / "statements" / str(date.today().year),
        base_dir / "reports" / "monthly",
    ]

    for directory in dirs:
        directory.mkdir(parents=True, exist_ok=True)
        print(f"Created: {directory}")

    return dirs


def report_directory(base_dir):
    """Print a summary of all files in the data directory."""

    all_files = list(base_dir.rglob("*"))

    file_list = [f for f in all_files if f.is_file()]
    dir_list = [f for f in all_files if f.is_dir()]

    print(f"\nDirectory report for: {base_dir.resolve()}")
    print(f"Subdirectories: {len(dir_list)}")
...     print(f"Files: {len(file_list)}")
... 
...     if file_list:
...         total_bytes = sum(f.stat().st_size for f in file_list)
...         print(f"Total size: {total_bytes:,} bytes")
... 
...         print("\nFiles:")
...         for file in sorted(file_list):
...             print(
...                 f"  {file.relative_to(base_dir)} "
...                 f"({file.stat().st_size:,} bytes)"
...             )
... 
... 
... def main():
...     # Get base directory from command line or environment variable
...     if len(sys.argv) > 1:
...         base_dir = Path(sys.argv[1])
...     else:
...         base_dir = Path(
...             os.environ.get(
...                 "FINTRUST_DATA_DIR",
...                 "data/fintrust"
...             )
...         )
... 
...     print(f"Setting up FinTrust data directories in: {base_dir}")
... 
...     if not base_dir.exists():
...         print("Base directory does not exist - creating it.")
... 
...     setup_directories(base_dir)
...     report_directory(base_dir)
... 
...     print("\nSetup complete.")
...     sys.exit(0)
... 
... 
... if __name__ == "__main__":
