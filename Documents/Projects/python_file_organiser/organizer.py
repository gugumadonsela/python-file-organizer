import os
import shutil # We'll use this later
import argparse

def organize_files(directory_path):
    print(f"Attempting to organize files in: {directory_path}")

    # 1. Check if the directory exists
    if not os.path.isdir(directory_path):
        print(f"Error: Directory '{directory_path}' not found or is not a directory.")
        return

    # 2. List files in the directory
    try:
        # List all entries, then filter for files only
        entries = os.listdir(directory_path)
        files = [f for f in entries if os.path.isfile(os.path.join(directory_path, f))]
        
        if not files:
            print("No files found in the directory to organize.")
            return
        print(f"Found files: {files}")
        # --- Further processing of files will go here ---

    except PermissionError:
        print(f"Error: Permission denied to access directory '{directory_path}'.")
        return
    except OSError as e:
        print(f"Error accessing directory contents: {e}")
        return

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Organize files in a directory by their type.")
    parser.add_argument("directory", help="The directory path to organize.")
    # Example of adding an optional argument (we might use it later)
    # parser.add_argument("--dry-run", action="store_true", help="Simulate organizing without moving files.")

    args = parser.parse_args()
    
    # It's good practice to get the absolute path
    absolute_directory_path = os.path.abspath(args.directory)
    organize_files(absolute_directory_path)