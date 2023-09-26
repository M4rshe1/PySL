import csv
import pandas as pd
import os
import sys
from tkinter import filedialog
import tkinter as tk
import re


def convert():
    wordslist = [{"word": "null", "count": 0}]
    txt_file = open_window("txt")
    with open(txt_file) as file_in:
        filename = os.path.basename(file_in.name).split(".")[0]
        for line in file_in:
            for words in line.split():
                words = re.sub(r"[,\(\)\[\]\{\}<>]", "", words)
                found = False
                for wordListItem in wordslist:
                    if wordListItem["word"] == words.lower():
                        wordListItem["count"] += 1
                        found = True
                        break
                if not found:
                    wordslist.append({"word": words.lower(), "count": 1})
        file_in.close()

    sorted_wordslist = sorted(wordslist, key=lambda x: x["count"], reverse=True)

    with open(filename + '.csv', 'w', newline='') as csvfile:
        fieldnames = ['word', 'count']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")

        writer.writeheader()
        for word_items in sorted_wordslist:
            writer.writerow(word_items)
        csvfile.close()


def load_csv():
    input_file = open_window("csv")
    csvfile = pd.read_csv(input_file)
    for csvline in csvfile:
        print(csvline)
    input()


def open_window(file_type):
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title="Select a File",
        filetypes=[("Text files", "*.{}".format(file_type))]
    )

    root.destroy()
    return file_path


try:
    while True:
        callFunction = input("What would you like to do? (L)oad or (C)onvert: ")
        # print(callFunction)
        if callFunction.lower() == "c":
            convert()
            sys.exit()

        elif callFunction.lower() == "l":
            load_csv()
            sys.exit()

        elif callFunction.lower() == "q":
            sys.exit()
except Exception as e:
    print(e)
