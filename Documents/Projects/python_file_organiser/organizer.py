import os
import shutil
import argparse

# Define file categories and their associated extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp", ".heic"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".odt", ".rtf", ".csv", ".xls", ".xlsx", ".ppt", ".pptx", ".md"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
    "Video": [".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv", ".webm"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
    "Scripts": [".py", ".js", ".sh", ".bat", ".java", ".cpp", ".c", ".html", ".css"],
    "Executables & Installers": [".exe", ".msi", ".dmg", ".app"],
    # Add more categories and extensions as you see fit
    "Other": [] # Catch-all for unknown extensions
}

def organize_files(directory_path):
    print(f"Attempting to organize files in: {directory_path}")

    # 1. Check if the directory exists
    if not os.path.isdir(directory_path):
        print(f"Error: Directory '{directory_path}' not found or is not a directory.")
        return

    # 2. List files in the directory
    try:
        # List all entries, then filter for files only directly within the target directory
        entries = os.listdir(directory_path)
        files_in_root_dir = [f for f in entries if os.path.isfile(os.path.join(directory_path, f))]
        
        if not files_in_root_dir:
            print("No files found directly in the root of the directory to organize.")
            return
        print(f"Found files in root: {files_in_root_dir}")

        # Iterate over the files found directly in the directory_path
        for original_filename in files_in_root_dir:
            
            # Optional: ignore hidden files (files starting with a dot)
            if original_filename.startswith('.'):
                print(f"Skipping hidden file: {original_filename}")
                continue

            # Construct the full path to the source file
            source_file_path = os.path.join(directory_path, original_filename)

            # Get the file extension
            _ , extension = os.path.splitext(original_filename) 
            extension = extension.lower() # Normalize to lowercase for consistent matching

            # Determine the target category
            target_category_name = "Other" # Default category if no match is found
            for category_name_iter, extensions_list in FILE_CATEGORIES.items():
                if extension in extensions_list:
                    target_category_name = category_name_iter
                    break # Found a category, no need to check further for this file
            
            print(f"File: {original_filename}, Extension: {extension}, Determined Category: {target_category_name}")
            
            # Construct the full path for the target category folder
            target_folder_path = os.path.join(directory_path, target_category_name)

            # Create target category folder if it doesn't exist
            try:
                if not os.path.exists(target_folder_path):
                    os.makedirs(target_folder_path)
                    print(f"Created directory: {target_folder_path}")
            except OSError as e:
                print(f"Error creating directory {target_folder_path}: {e}. Skipping file {original_filename}.")
                continue # Skip to the next file if folder creation fails

            # Prepare filename for destination (might be changed if file exists)
            current_filename_for_dest = original_filename
            destination_file_path = os.path.join(target_folder_path, current_filename_for_dest)

            # --- SAFETY CHECK: Avoid overwriting files ---
            # If a file with the same name already exists in the target folder,
            # rename the new file to avoid overwriting.
            count = 1
            name_part, ext_part = os.path.splitext(original_filename)
            while os.path.exists(destination_file_path):
                # If "file.txt" exists, try "file (1).txt", then "file (2).txt", etc.
                current_filename_for_dest = f"{name_part} ({count}){ext_part}"
                destination_file_path = os.path.join(target_folder_path, current_filename_for_dest)
                count += 1
            # --- END SAFETY CHECK ---

            # Move the file
            try:
                shutil.move(source_file_path, destination_file_path)
                if original_filename != current_filename_for_dest: # If we renamed the file
                     print(f"Moved '{original_filename}' to '{target_category_name}/{current_filename_for_dest}' (renamed to avoid overwrite)")
                else:
                    print(f"Moved '{original_filename}' to '{target_category_name}/'")
            except OSError as e:
                print(f"Error moving file {original_filename}: {e}")
            except Exception as e: # Catch any other unexpected errors during move
                print(f"An unexpected error occurred while moving {original_filename}: {e}")

    except PermissionError:
        print(f"Error: Permission denied to access directory '{directory_path}'.")
        return
    except OSError as e:
        print(f"Error accessing directory contents: {e}")
        return
    except Exception as e: # General catch-all for unexpected errors
        print(f"An unexpected error occurred: {e}")
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