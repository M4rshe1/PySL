import subprocess
import time
from colorama import Fore, Style
import modules.gen_graph as gen_graph
import modules.print_result as print_result
import json
from tkinter import filedialog
import tkinter as tk
import os

# ------------------------------------------------------- #
#                   Settings / Variables                  #
# ------------------------------------------------------- #

GRAPH_FILE = False
GRAPH_DATA = True
DEFAULT_DEVICE = "google.com"
DELAY = 1  # Delay between pings in seconds
# in seconds or Xs or Xm but always as a string
# Xs = X seconds
# Xm = X minutes
# Xm and Xs are not compatible!!!!!
DEFAULT_PING_DURATION = "2m"


# ------------------------------------------------------- #
#                   Functions / Methods                   #
# ------------------------------------------------------- #


def select_file():
    if not os.path.exists("graphs"):
        os.mkdir("graphs")

    root = tk.Tk()
    root.withdraw()
    # multiple files can be selected
    file_path = filedialog.askopenfilename(title="Select a file",
                                           filetypes=(("JSON", "*.json"), ("All files", "*.*")),
                                           initialdir="graphs")

    # kill the program if no file is selected
    if file_path == "":
        print("No file selected")
        return []
    else:
        # print(file_path)
        return file_path


def select_files():
    if not os.path.exists("graphs"):
        os.mkdir("graphs")

    root = tk.Tk()
    root.withdraw()
    # multiple files can be selected
    file_path = filedialog.askopenfilenames(title="Select a file",
                                            filetypes=(("JSON", "*.json"), ("All files", "*.*")),
                                            initialdir="graphs")

    # kill the program if no file is selected
    if file_path == "":
        print("No file selected")
        return []
    else:
        # print(file_path)
        return file_path


def split_array_into_splits(arr, splits):
    """Split an array into three pieces as close to equal as possible."""
    length = len(arr)
    chunk_size = length // splits
    remainder = length % splits

    result = []
    start = 0

    for _ in range(splits):
        if remainder > 0:
            end = start + chunk_size + 1
            remainder -= 1
        else:
            end = start + chunk_size

        result.append(arr[start:end])
        start = end

    return result


def calc_bar_width(start, end, times):
    # Calculate the completion percentage
    completion_percentage = int((time.time() - start) / (end - start) * 100)

    # Ensure that the completion percentage is between 0 and 100
    completion_percentage = max(0, min(100, completion_percentage))

    # Create the completed part of the progress bar
    completed = "#" * completion_percentage

    # Ensure that the completed string is exactly 100 characters long
    completed = completed.ljust(100)

    completed = split_array_into_splits(completed, len(times))
    for i in range(len(times)):
        if times[i] == 0:
            completed[i] = Fore.RED + completed[i].replace("#", "0") + Style.RESET_ALL
        elif times[i] < 30:
            completed[i] = Fore.GREEN + completed[i] + Style.RESET_ALL
        elif times[i] < 120:
            completed[i] = Fore.YELLOW + completed[i] + Style.RESET_ALL
        else:
            completed[i] = Fore.RED + completed[i] + Style.RESET_ALL
    return "".join(completed)


def ping_device(device: str, duration: int):
    """
    Ping a device for a specified duration and return the results
    :param device: The device or IP address to ping
    :param duration: the duration of the ping session in seconds
    :return: an array containing the ping results
    """
    try:
        received_count = 0
        lost_count = 0
        start_time = time.time()
        end_time = start_time + duration
        res_time = []
        res_timestamp = []
        starttime = time.time()

        print(f"Pinging {device} for {duration}s...")
        while time.time() < end_time:
            result = subprocess.Popen(
                ['ping', '-n', '1', device],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            result.communicate()
            req_time = 0
            if result.returncode == 0:
                output = int(str(result.communicate()[0]).split("Maximum = ")[-1].split("ms")[0])
                received_count += 1
                if output == 0:
                    res_time.append(1)
                    output = 1
                req_time = output
                res_time.append(round(req_time))
            else:
                lost_count += 1
                res_time.append(0)
            res_timestamp.append(time.time() - start_time)

            bar = calc_bar_width(start_time, end_time, res_time)

            print(
                f"\r{bar:<100}| "
                f"{int((time.time() - start_time) / (end_time - start_time) * 100):>3}% / "
                f"{end_time - time.time():.0f}s {Fore.GREEN}{Style.BRIGHT if result.returncode == 0 else Fore.RED}"
                f"{result.returncode}{Style.RESET_ALL} {Fore.YELLOW}{req_time}ms{Style.RESET_ALL} "
                f"{Fore.BLUE}{received_count + lost_count}{Style.RESET_ALL}",
                end=""
            )

            time.sleep(DELAY)
        bar = calc_bar_width(start_time, end_time, res_time)
        print(
            f"\r{bar}| 100% / 0.00s {Fore.GREEN}{Style.BRIGHT}0{Style.RESET_ALL} "
            f"{Fore.YELLOW}0.00ms{Style.RESET_ALL} {Fore.BLUE}{received_count + lost_count}{Style.RESET_ALL}",
            end=""
        )

        print("\nPing session completed.")

        avg = 0
        avg_count = 0
        for i in res_time:
            if i != 0:
                avg += i
                avg_count += 1
        avg = round(avg / avg_count, 2)

        return {
            "req": received_count + lost_count,
            "res": received_count,
            "lost": lost_count,
            "loss": lost_count / (received_count + lost_count) * 100,
            "min": min([x for x in res_time if x > 0]),
            "max": max(res_time),
            "starttime": starttime,
            "device": device,
            "endtime": time.time(),
            "times": res_time,
            "timestamps": res_timestamp,
            "pingtime": duration,
            "avg": avg
        }

    except KeyboardInterrupt:
        print("\nPing session interrupted.")


# ------------------------------------------------------- #
#                          Main                           #
# ------------------------------------------------------- #


if __name__ == "__main__":

    print(""
          " _____ _               _______          _\n"
          "|  __ (_)             |__   __|        | |\n"
          "| |__) | _ __   __ _     | | ___   ___ | |\n"
          "|  ___/ | '_ \ / _' |    | |/ _ \ / _ \| |\n"
          "| |   | | | | | (_| |    | | (_) | (_) | |\n"
          "|_|   |_|_| |_|\__, |    |_|\___/ \___/|_|\n"
          "                __/ |\n"
          "               |___/\n"
          )
    print("****************************************************************")
    print("* Ping Tool by Colin Heggli 2023                               *")
    print("* https://colin.heggli.dev                                     *")
    print("* https;//github.com/M4rshe1                                   *")
    print("****************************************************************")
    print("")
    print("")
    print("What would you like to do?")
    print("  p - Ping a device")
    print("  l - Load a graph from a file")
    print("  c - continue a previous ping session")
    print("  g - generate a graph")
    print("  m - merge ping results")
    print("  s - split results")
    choose = input(">> ")
    all_ping_data = []
    if choose == "l":
        file_path = select_file()
        if not file_path:
            print("No file selected")
            exit()
        with open(file_path) as f:
            all_ping_data = json.load(f)
    elif choose == "c":
        file_path = select_file()
        if not file_path:
            print("No file selected")
            exit()
        with open(file_path) as f:
            all_ping_data = json.load(f)
        device = all_ping_data[0]["device"]
        duration = all_ping_data[0]["pingtime"]
        all_ping_data.append(ping_device(device, duration))
    elif choose == "p":
        device = input(f"Device to ping, Default ({DEFAULT_DEVICE}): ")
        duration = input(f"Duration of ping session, Default ({DEFAULT_PING_DURATION}): ")
        all_ping_data.append(ping_device(device, int(duration)))
    elif choose == "g":
        file_path = select_files()
        if not file_path:
            print("No file selected")
            exit()
        for file in file_path:
            with open(file) as f:
                all_ping_data.append(json.load(f))
        gen_graph.gen_graph(all_ping_data, f"graphs/{all_ping_data[0]['starttime'].replace(':', '_')}graph")
    elif choose == "m":
        file_path = select_files()
        if not file_path:
            print("No file selected")
            exit()
        for file in file_path:
            with open(file) as f:
                all_ping_data.append(json.load(f))
        print_result.print_results(all_ping_data)
    elif choose == "s":
        file_path = select_file()
        filename = file_path.split("/")[-1]
        if not file_path:
            print("No file selected")
            exit()
        with open(file_path) as f:
            all_ping_data = json.load(f)
            for i in all_ping_data:
                with open(f"{filename}/split_{i['starttime'].replace(':', '_')}.json", "w") as k:
                    json.dump([i], k)
    else:
        print("Invalid choice")
        exit()