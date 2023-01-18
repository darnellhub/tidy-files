Tidy Folders
 
Tidy Folders is a simple yet powerful file organizing tool that helps you keep your files organized by sorting them into different folders based on their file type.

Features

* Select a folder to sort
* Sorts files into predefined folders based on file type
* Progress bar to show sorting progress

How to use

1. Clone or download the repository to your local machine.
2. Open the application by running the main.py file.
3. Click on the "Select Folder" button and select the folder you want to sort.
4. Press the "Sort" button and wait for the sorting process to complete.
5. The sorted files will be placed in their respective folders and any remaining files will be placed in the "OTHER" folder.

File Types

The app sorts files into the following folders:
* DOCUMENTS: [".numbers",".ppt", ".pptx", ".otf", ".xls", ".odt", ".ott", ".doc", ".ods", ".csv", ".pdf", ".docx", ".txt", ".xlsx"]
* IMAGES: [".HEIC",".heic", ".raw", ".tiff", ".eps", ".svg", ".jpg", ".JPG", ".PNG", ".jpeg", ".png", ".gif"]
* AUDIO: [".flac", ".wma", ".mp3", ".m4a", ".wav"]
* VIDEO: [".MOV", ".MP4", ".mkv", ".wmv", ".mpeg", ".mp4", ".mov", ".avi"]
* SOFTWARE: [".msi",".exe", ".dmg", ".pkg",".bin"]
* ZIP FILES: [".zip", ".rar", ".bz2"]
* TORRENTS: [".torrent"]
* PHOTOSHOP: [".psd", ".psdt"]

You can add or remove file types as per your requirement.

Requirements
* Python 3.x
* Tkinter
* os
* shutil        


Installation
1. Clone or download the repository to your local machine.
2. Make sure you have Python 3.x installed on your machine.
3. Run the main.py file to start the application.

Notes
1. The application will only sort files in the selected folder, it will not recursively sort subfolders.
2. The application will not move any files that are currently in use by another application.
4. The application will not sort hidden files.
5. This application is for personal use only, use at your own risk.
