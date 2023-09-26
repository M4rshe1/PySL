import os
import shutil
from organizer_modules import select_folder
from organizer_modules import EXCLUDE
from organizer_modules import SORTED_FOLDER
from organizer_modules import EXT_LIST_TYPE

# COUNTER
count = 0


def check_path(path):
    if not os.path.exists(path):
        os.mkdir(path)


def move_files(src_path, path):
    global count
    try:
        shutil.move(src_path, path)
    except Exception as e:
        print(f"ERROR with: {path}")
        print(e)
    count += 1


def sort_files(src_path):
    path = src_path + "/" + SORTED_FOLDER
    os.chdir(src_path)
    check_path(path)

    for item in os.listdir():
        if item in EXCLUDE:
            continue
        item_path = src_path + "/" + item
        if os.path.isfile(item_path):
            for cat, extension in EXT_LIST_TYPE.items():
                # print("EXT: " + str(extension))
                # print(item.split(".")[-1].lower())
                if item.split(".")[-1].lower() in extension:
                    print(f"FILE ({cat}): " + item)
                    check_path(path + "/" + cat)
                    move_files(item_path, path + "/" + cat.upper() + "/" + item)

        elif os.path.isdir(item_path):
            print(f"FOLDER: " + item)
            check_path(path + "/FOLDERS")
            move_files(item_path, path + "/FOLDERS/" + item)

    for item in os.listdir():
        if item in EXCLUDE:
            continue
        item_path = src_path + "/" + item
        if os.path.isfile(item_path):
            print(f"FILE (OTHER): " + item)
            check_path(path + "/OTHER")
            move_files(item_path, path + "/OTHER/" + item)
    return count


if __name__ == "__main__":
    folder_to_organize = select_folder()
    count = sort_files(folder_to_organize)
    input(f"Sorted {count} files/folders")
