import csv
import pandas as pd
import os


def convert():
    wordslist = [{"word": "", "anzahl": 0}]
    with open(".\dancin.txt") as file_in:
        filename = os.path.basename(file_in.name).split(".")[0]
        for line in file_in:
            for words in line.split():
                found = False
                for wordListItem in wordslist:
                    if wordListItem["word"] == words:
                        wordListItem["anzahl"] += 1
                        found = True
                        break
                if not found:
                    wordslist.append({"word": words, "anzahl": 1})

    sorted_wordslist = sorted(wordslist, key=lambda x: x["anzahl"], reverse=True)

    with open('words.csv', 'w', newline='') as csvfile:
        fieldnames = ['word', 'anzahl']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")

        writer.writeheader()
        for worditems in sorted_wordslist:
            writer.writerow(worditems)


def load():
    InputFile = input("Enter full name of File: ")
    if not InputFile.find(".csv"):
        InputFile += ".csv"

    csvfile = pd.read_csv(InputFile)
    print(csvfile)


while True:
    callFunction = input("What would you like to do? (L)oad or (C)onvert: ")
    print(callFunction)
    if callFunction.lower().find("c"):
        convert()
    elif callFunction.lower().find("l"):
        load()

# print(wordslist)
