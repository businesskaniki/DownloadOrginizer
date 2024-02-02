import os
import shutil
import platform

operating_sys = platform.system()

image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"]
video_extensions = [
    ".mp4",
    ".avi",
    ".mkv",
    ".mov",
    ".flv",
    ".wmv",
    ".webm",
    ".mpeg",
    ".3gp",
]
document_extensions = [
    ".doc",
    ".docx",
    ".pdf",
    ".txt",
    ".odt",
    ".rtf",
    ".xls",
    ".xlsx",
    ".csv",
    ".ppt",
    ".pptx",
]
audio_extensions = [
    ".mp3",
    ".wav",
    ".flac",
    ".aac",
    ".ogg",
    ".wma",
    ".m4a",
    ".aiff",
    ".alac",
]
software_extensions = [
    ".deb",
    ".rpm",
    ".exe",
    ".msi",
    ".dmg",
    ".pkg",
    ".appimage",
    ".zip",
    ".tar.gz",
    ".tar.xz",
]


def move_to_folder(file_path, folder_path):
    destination_path = os.path.join(folder_path, os.path.basename(file_path))

    if not os.path.exists(destination_path):
        try:
            shutil.move(file_path, destination_path)
            print(
                f"File '{file_path}' moved to '{os.path.basename(folder_path)}' folder."
            )
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
        except PermissionError:
            print(
                f"Permission error moving file '{file_path}' to '{os.path.basename(folder_path)}' folder."
            )
        except Exception as er:
            print(
                f"Error moving file '{file_path}' to '{os.path.basename(folder_path)}' folder: {er}"
            )
    else:
        print(
            f"File '{os.path.basename(file_path)}' already exists in '{os.path.basename(folder_path)}' folder. Skipping."
        )


downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")

folders_mapping = {
    "Software": software_extensions,
    "Videos": video_extensions,
    "Audios": audio_extensions,
    "Documents": document_extensions,
    "Images": image_extensions,
}

if os.path.exists(downloads_dir):
    for folder_name, extensions in folders_mapping.items():
        path = os.path.join(downloads_dir, folder_name)

        if not os.path.exists(path):
            try:
                os.makedirs(path)
                print(f"Folder '{folder_name}' created at {path}")
            except OSError as e:
                print(f"Error creating '{folder_name}' folder: {e}")

        for item in os.listdir(downloads_dir):
            item_path = os.path.join(downloads_dir, item)
            if os.path.isfile(item_path):
                _, file_ext = os.path.splitext(item)
                if file_ext in extensions:
                    move_to_folder(item_path, path)
else:
    print("Downloads directory does not exist.")
