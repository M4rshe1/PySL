import os
import shutil
from organizer_modules import select_folder
from organizer_modules import SORTED_FOLDER
from organizer_modules import categories


def check_path(path):
    if not os.path.exists(path):
        os.mkdir(path)


def move_files(src_path, path):
    try:
        shutil.move(src_path, path)
    except Exception as e:
        print(f"ERROR with: {path}")
        print(e)


def file_unorganized(src_path):
    count = 0
    for c in categories:
        if not os.path.exists(src_path + "/" + c):
            continue
        for item in os.listdir(src_path + "/" + c):
            item_path = src_path + "/" + c + "/" + item
            if os.path.isfile(item_path):
                print(f"FILE ({c}): " + item)
                move_files(item_path, src_path.replace(SORTED_FOLDER, "") + item)
            elif os.path.isdir(item_path):
                print(f"FOLDER: " + item)
                move_files(item_path, src_path.replace(SORTED_FOLDER, "") + "/" + item)
            count += 1
    return count


if __name__ == "__main__":
    file_unorganized(select_folder())
