# ------------------------------------------------------- #
#                   Import libraries                      #
# ------------------------------------------------------- #

import subprocess
import time
from tkinter import filedialog
import tkinter as tk
from colorama import Fore, Style
import os
import concurrent.futures
import json

# ------------------------------------------------------- #
#                   Settings / Variables                  #
# ------------------------------------------------------- #

SLEEP_TIME = 10
FILE_OVERWRITE = "ip.json"


def ping_device(device):
    ping = subprocess.Popen(
        ['ping', '-n', '1', device],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = ping.communicate()
    output = stdout.decode('utf-8', 'replace')
    # print all information from the ping command
    # print(ping.returncode)

    if ping.returncode == 0:
        val = True
    else:
        val = False
    return val


def read_file(file):
    with open(file, "r") as f:
        data = json.load(f)
    return data


def select_file():
    root = tk.Tk()
    root.withdraw()
    # multiple files can be selected
    file_path = filedialog.askopenfilenames(title="Select a file",
                                            filetypes=(("Python", "*.json"), ("All files", "*.*")),
                                            initialdir=os.getcwd())

    # kill the program if no file is selected
    if file_path == "":
        print("No file selected")
        exit()
    else:
        return file_path


if __name__ == '__main__':
    if not os.path.exists(FILE_OVERWRITE):
        file_selected = select_file()
    else:
        file_selected = [FILE_OVERWRITE]
    ips = read_file(file_selected[0])
    results = []  # List to store the return values

    while True:
        print("Pinging...")
        for ip in ips["devices"]:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(ping_device, ip["ip"])  # Store the future object
                result = future.result()
                results.append(result)  # Store the result in the list

        print(f"\n\n\n\n\n\n\{'name':<20} {'IP':<15} {'Status':<15}")
        for i in range(len(ips["devices"])):
            # print(results[i])
            if results[i]:
                print(f"{Fore.GREEN}{ips['devices'][i]['name']:<20} {ips['devices'][i]['ip']:<15} UP{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}{ips['devices'][i]['name']:<20} {ips['devices'][i]['ip']:<15} DOWN{Style.RESET_ALL}")
        results = []
        print(f"Sleeping for {SLEEP_TIME} seconds...")
        for i in range(SLEEP_TIME):
            print(f"\r{int(i / SLEEP_TIME * 100) * '#':<100}| {SLEEP_TIME - i:>3}s", end="")
            time.sleep(1)
        print(f"\r{'#'*100}| 0s")
        print("\n" * 100)


