import subprocess
import time
from colorama import Fore, Style
import modules.gen_graph as gen_graph
import modules.print_result as print_result
import json
import datetime
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
    if input("Enter l to load a file.\n>> ").lower() == "l":
        json_file = select_file()
        if len(json_file) < 1:
            pass
        with open(json_file[0], "r") as file:
            ping_result = json.load(file)
        print_result.print_results(json_file[0], ping_result)
        if input("Enter g to generate a graph.\n>> ") == "g":
            graph_file_name = json_file[0].split("/")[-1].split(".")[0].replace("result", "graph")
            gen_graph.gen_graph(ping_result, graph_file_name + ".png")

        exit()
    else:
        pass

    redone = False
    all_ping_results = []
    device_to_ping = (input(f"Enter device or IP address to ping (default: {DEFAULT_DEVICE}):\n>> ")
                      or DEFAULT_DEVICE)
    ping_duration = (input(f"Enter ping duration Xs or Xm (default: {DEFAULT_PING_DURATION}):\n>> ")
                     or str(DEFAULT_PING_DURATION))
    while True:
        if not redone:
            if device_to_ping.lower() == "load":
                # print("Loading...")
                file_to_load = select_file()[0]
                with open(file_to_load, "r") as file:
                    ping_result = json.load(file)
            else:
                if ping_duration[-1] == "s":
                    ping_duration = int(ping_duration[:-1])
                elif ping_duration[-1] == "m":
                    ping_duration = int(ping_duration[:-1]) * 60
                elif ping_duration[-1].isnumeric():
                    ping_duration = int(ping_duration)

        ping_result = ping_device(device_to_ping, ping_duration)
        all_ping_results.append(ping_result)
        print_result.print_results(device_to_ping, all_ping_results)

        redo = input("Ping again? (y/n)\n>> ")
        if redo.lower() == "n":
            if GRAPH_DATA:
                with open(
                        f"graphs/ping_data_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json", "w"
                ) as file:
                    json.dump(all_ping_results, file, indent=4)
            if GRAPH_FILE:
                gen_graph.gen_graph(all_ping_results,
                                    f"graphs/ping_graph_"
                                    f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png")
            break
        elif redo.lower() == "y" or redo == "":
            redone = True
            continue
