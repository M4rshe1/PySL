# Convert any video format to mp4 format

import os
import subprocess
from tkinter import filedialog
import tkinter as tk
import moviepy.editor as moviepy


# open explorer to select any video media file format
def select_file():
    # Hide the Tkinter GUI
    root = tk.Tk()
    root.withdraw()
    # multiple files can be selected
    file_path = filedialog.askopenfilenames(title="Select a file",
                                            filetypes=(("Video", " *.mkv *.avi *.mov *.flv *.wmv *.webm"),
                                                       ("All files", "*.*")))

    # kill the program if no file is selected
    if file_path == "":
        input("No file selected, Press enter to exit.")
        exit()
    else:
        return file_path


if __name__ == "__main__":
    file_selected = select_file()
    for file in file_selected:
        print(f"Converting {file} to mp4")
        output_file = f"{os.path.splitext(file)[0]}.mp4"
        video = moviepy.VideoFileClip(file)
        video.write_videofile(output_file)
        print("Done")
    input("Done, Press enter to exit.")
