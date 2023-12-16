from file_unorganizer import file_unorganized
from file_organizer import sort_files
from file_counter import count_files
import os


# sort, unsort or count
MODE = "sort"

# folder to sort/unsort/count
FOLDER = f"/users/{os.getlogin()}/Downloads"

if MODE == "sort":
    sort_files(FOLDER)
elif MODE == "unsort":
    file_unorganized(FOLDER)
elif MODE == "count":
    count_files(FOLDER)
else:
    print("Invalid mode")

