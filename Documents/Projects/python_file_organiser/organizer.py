import os
import shutil 
import argparse

# --- START OF MISSING PART 1 ---
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
# --- END OF MISSING PART 1 ---

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

       
        # THIS IS THE CRUCIAL PART THAT PROCESSES EACH FILE
        for filename in files:
            # Optional: ignore hidden files (files starting with a dot)
            if filename.startswith('.'):
                print(f"Skipping hidden file: {filename}")
                continue

            # Construct the full path to the file
            file_path = os.path.join(directory_path, filename)

            # Get the file extension
            _ , extension = os.path.splitext(filename) # The first part (name) is not needed here, hence '_'
            extension = extension.lower() # Normalize to lowercase for consistent matching

            # Determine the target category
            target_category_name = "Other" # Default category if no match is found
            for category_name, extensions_list in FILE_CATEGORIES.items():
                if extension in extensions_list:
                    target_category_name = category_name
                    break # Found a category, no need to check further for this file
            
            print(f"File: {filename}, Extension: {extension}, Determined Category: {target_category_name}")
            
            # --- Logic to create folder and move file will go here in the next step ---
        

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