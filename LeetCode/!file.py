import os


def convert_filename(file_name):
    return file_name.replace(" ", "_").replace(".", "").lower()


if __name__ == "__main__":
    print("finished challenges: ", end="")
    print(sum(1 for file in os.listdir() if file != "!file.py"))
    while True:
        filename = input("Enter file name: ").strip()
        if len(filename) > 5:
            open(convert_filename(filename) + ".py", "w").close()
            # open it as a new tab in pycharm
            # For this to work, you need to have pycharm in your path
            # C:\Users\%USERNAME%\AppData\Local\Programs\PyCharm Professional\bin\pycharm64.exe
            os.system("pycharm " + convert_filename(filename) + ".py")
