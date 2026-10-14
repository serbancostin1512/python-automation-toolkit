from pathlib import Path
import shutil

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "Documents" : [".pdf",".doc",".docx",".txt",".md",".odt"],
    "Spreadsheets" : [".xls",".xlsx",".csv"],
    "Videos": [".mp4",".mkv",".mov",".avi"],
    "Audio" : [".mp3",".wav",".flac",".m4a"],
    "Archives": [".zip",".rar",".7z",".tar",".gz"],
    "Code": [".py",".js",".html",".css",".java",".cpp"]
}

def get_category(file_path):
    extension = file_path.suffix.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"

def get_unique_path(destination):
    if not destination.exists():
        return destination

    folder = destination.parent
    name = destination.stem
    extension = destination.suffix
    counter = 1

    while True:
        new_name = f"{name}_{counter}{extension}"
        new_path = folder / new_name

        if not new_path.exists():
            return new_path

        counter += 1

def organize_files(folder_path):
    folder = Path(folder_path).expanduser()

    if not folder.exists() or not folder.is_dir():
        print("Error: the folder does not exist.")
        return

    files = [item for item in folder.iterdir() if item.is_file()]

    if not files:
        print("No files found in this folder.")
        return

    plan = []

    print("\n ===FILE ORGANIZATION PREVIEW ===")

    for file_path in files:
        category = get_category(file_path)
        destination_folder = folder / category
        destination = get_unique_path(destination_folder / file_path.name)

        plan.append((file_path, destination))

        print(f"{file_path.name} -> {category}/{destination.name}")

    answer = input (
        "\nDo you want to move these files (y/n):"
    ).strip().lower()

    if answer != 'y':
        print("Operation cancelled. No file were moved.")
        return

    moved_count = 0

    for source, destination in plan:
        try:
            destination.parent.mkdir(parents=True, exist_ok=True)

            destination = get_unique_path(destination)

            shutil.move(str(source), str(destination))
            moved_count +=1

            print(f"Moved: {source.name}")
        except OSError as error:
            print(f"Could not move {source.name}: {error}")

    print(f"\nFinished! {moved_count} file(s) moved")

def main():
    print("=== PYTHON FILE ORGANIZER === ")
    print("This program organizes file by file type")

    folder_path = input(
        "\nEnter the path of the folder to organize:"
        ).strip().strip('"')

    organize_files(folder_path)

if __name__ == "__main__":
    main()