# Python File Organizer

A command-line utility written in Python to organize files within a specified directory into subdirectories based on their file type.

## Features

*   Scans a target directory for files.
*   Categorizes files based on their extensions (e.g., images, documents, videos, archives).
*   Creates subdirectories for these categories if they don't already exist.
*   Moves files from the target directory into their respective category subfolders.
*   Includes a safety mechanism to prevent overwriting: if a file with the same name already exists in the destination category folder, the new file being moved will be renamed (e.g., `document.pdf` becomes `document (1).pdf`).
*   Provides informative output to the console during the organization process.

## Technologies Used

*   Python 3.x
*   Standard Python libraries:
    *   `os`: For interacting with the file system (paths, listing directories, checking existence).
    *   `shutil`: For robust file operations (moving files).
    *   `argparse`: For parsing command-line arguments.

## Setup

1.  Ensure you have Python 3 installed on your system.
2.  Clone this repository or download the `organizer.py` script.
    ```bash
    # If you plan to clone (after pushing to GitHub)
    # git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
    # cd YOUR_REPOSITORY_NAME
    ```
3.  No external libraries need to be installed beyond what comes with Python.

## Usage

Run the script from your terminal, providing the path to the directory you want to organize as a command-line argument.

```bash
py organizer.py C:\path\to\your\messy_folder
    **Example:**

    If you have a folder named `MyDownloads` on your Desktop that you want to organize:

    *On Windows:*
    ```bash
    py organizer.py C:\Users\YourUserName\Desktop\MyDownloads
    ```

    *On macOS/Linux:*
    ```bash
    python organizer.py /Users/YourUserName/Desktop/MyDownloads
    ```

    The script will then create subfolders like `Images`, `Documents`, etc., inside `MyDownloads` and move the files accordingly.

    ## How it Works (Brief Overview)

    1.  The script takes a target directory path as a command-line argument.
    2.  It verifies that the provided path is a valid, accessible directory.
    3.  It lists all files (not sub-folders) directly within the target directory.
    4.  For each file:
        a.  Its extension is extracted (e.g., `.txt`, `.jpg`).
        b.  The script determines the appropriate category (e.g., "Documents", "Images") based on a predefined mapping of extensions. Files with unrecognized extensions are typically moved to an "Other" category.
        c.  A subdirectory for the determined category is created within the target directory if it doesn't already exist.
        d.  The file is moved from its original location into the category subdirectory. If a file with the same name already exists in the destination, the script renames the incoming file (e.g., `file (1).ext`) to prevent data loss.
    5.  Informative messages are printed to the console throughout the process.

    ## (Optional: Add a section if you implement --dry-run or other enhancements)
    # ## Future Enhancements (Ideas)
    # *   `--dry-run` mode: Simulate the organization process without actually moving files.
    # *   Configurable categories: Allow users to define their own categories and extensions via a configuration file (e.g., JSON).
    # *   Recursive organization: Add an option to organize files within subdirectories of the target folder as well.
    # *   Logging: Save a log of operations to a file.
    # *   GUI: A simple graphical user interface.

    ## Author

    *   Gugu Madonsela - https://github.com/gugumadonsela
    