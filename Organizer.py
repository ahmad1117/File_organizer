import os
import shutil
folder_path = input("Enter the path of the folder you wan t to organize: ")
file_types = {
    "images": [".jpg", ".jpeg", ".png", ".gif"],
    "documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "videos": [".mp4", ".mkv", ".avi"],
    "audio": [".mp3", ".wav", ".aac"],
    "archives": [".zip", ".rar", ".tar", ".gz"],
    "scripts": [".py", ".js", ".html", ".css"],
    "other": []}
for filename in os.listdir(folder_path):
    file_ext = os.path.splitext(filename)[1].lower()
    moved = False


def move_file(folder_path, filename, folder):
    for folder, extentios in file_types.items():
        if file_ext in extentios:
            move_file(folder_path, filename, folder)
            moved = True
            break
    if not moved:
        move_file(folder_path, filename, "other")
