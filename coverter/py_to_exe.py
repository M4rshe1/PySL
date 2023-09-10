import os
import subprocess
from tkinter import filedialog
import tkinter as tk


# open explorer to select python file
def select_file():
    # Hide the Tkinter GUI
    root = tk.Tk()
    root.withdraw()
    # multiple files can be selected
    file_path = filedialog.askopenfilenames(title="Select a file",
                                            filetypes=(("Python", "*.py"), ("All files", "*.*")))

    # file_path = filedialog.askopenfilename(initialdir="/", title="Select a file",
    #                                        filetypes=(("Python", "*.py"), ("All files", "*.*")))
    # Break if a file is selected
    # kill the program if no file is selected
    if file_path == "":
        print("No file selected")
        exit()
    else:
        return file_path


def convert_py_to_exe(file_path):
    input("Icon for the exe?\nName the *.ico file like the python file and place it in the same folder as the python "
          "file."
          "\n>> ")

    icon_path = file_path.split("/")[:-1] + [file_path.split("/")[-1].split(".")[0] + ".ico"]
    # convert array back to path
    icon_path = "/".join(icon_path)
    # print(icon_path)
    if os.path.exists(icon_path):
        subprocess.call(
            f"pyinstaller --onefile --icon={icon_path} {file_path}")
    else:
        subprocess.call(
            f"pyinstaller --onefile {file_path}")
    print("Done")
    # delete all .spec files
    for files in os.listdir():
        if files.endswith(".spec"):
            os.remove(files)


file_selected = select_file()
for file in file_selected:
    convert_py_to_exe(file)
