import subprocess
import time
from colorama import Fore, Style
# import modules.res_over_time_graph as res_graph_time
# import modules.print_graph_ms as print_graph_ms
import modules.print_result as print_result
import json
import datetime
from tkinter import filedialog
import tkinter as tk

# ------------------------------------------------------- #
#                   Settings / Variables                  #
# ------------------------------------------------------- #

GRAPH_FILE = False
GRAPH_DATA = True
NO_RES_ELEMENTS = 4
GRAPH_MS = False
DEFAULT_DEVICE = "google.com"
# in seconds or Xs or Xm but always as a string
# Xs = X seconds
# Xm = X minutes
# Xm and Xs are not compatible!!!!!
DEFAULT_PING_DURATION = "2m"


# ------------------------------------------------------- #
#                   Functions / Methods                   #
# ------------------------------------------------------- #


def select_file():
    root = tk.Tk()
    root.withdraw()
    # multiple files can be selected
    file_path = filedialog.askopenfilenames(title="Select a file",
                                            filetypes=(("JSON", "*.json"), ("All files", "*.*")))

    # kill the program if no file is selected
    if file_path == "":
        print("No file selected")
        exit()
    else:
        # print(file_path)
        return file_path


def ping_device(device: str, duration: int):
    """
    Ping a device for a specified duration and return the results
    :param device: The device or IP address to ping
    :param duration: the duration of the ping session in seconds
    :return: a dictionary containing the ping results
    """
    try:
        received_count = 0
        lost_count = 0
        start_time = time.time()
        end_time = start_time + duration
        res_time = []
        res_timestamp = []
        print(f"Pinging {device} for {duration}s ({end_time - start_time:.0f}s")
        while time.time() < end_time:
            ping_time = time.time()
            result = subprocess.Popen(
                ['ping', '-n', '1', device],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            # print(result)
            result.communicate()
            req_time = time.time() - ping_time

            if result.returncode == 0:
                received_count += 1
                res_time.append(round(req_time * 1000))
            else:
                lost_count += 1
                res_time.append(0)
            res_timestamp.append(time.time() - start_time)
            print(
                f"\r{int((time.time() - start_time) / (end_time - start_time) * 100) * '#':<100}| "
                f"{int((time.time() - start_time) / (end_time - start_time) * 100):>3}% / "
                f"{end_time - time.time():.0f}s {Fore.GREEN}{Style.BRIGHT if result.returncode == 0 else Fore.RED}"
                f"{result.returncode}{Style.RESET_ALL} {Fore.YELLOW}{req_time * 1000:.2f}ms{Style.RESET_ALL} "
                f"{Fore.BLUE}{received_count + lost_count}{Style.RESET_ALL}",
                end=""
            )

            time.sleep(1)  # Wait for 1 second between pings
        print(
            f"\r{'#' * 100}| 100% / 0.00s {Fore.GREEN}{Style.BRIGHT}0{Style.RESET_ALL} "
            f"{Fore.YELLOW}0.00ms{Style.RESET_ALL} {Fore.BLUE}{received_count + lost_count}{Style.RESET_ALL}",
            end=""
        )
        print("\nPing session completed.")
        return {
            "req": received_count + lost_count,
            "res": received_count,
            "lost": lost_count,
            "loss": lost_count / (received_count + lost_count) * 100,
            "min": min([x for x in res_time if x > 0]),
            "max": max(res_time),
            "times": res_time,
            "timestamps": res_timestamp
        }

    except KeyboardInterrupt:
        print("\nPing session interrupted.")


# ------------------------------------------------------- #
#                          Main                           #
# ------------------------------------------------------- #


if __name__ == "__main__":
    device_to_ping = (input(f"Enter device or IP address to ping (default: {DEFAULT_DEVICE}):\n>> ")
                      or DEFAULT_DEVICE)
    ping_duration = (input(f"Enter ping duration Xs or Xm (default: {DEFAULT_PING_DURATION}):\n>> ")
                     or str(DEFAULT_PING_DURATION))
    while True:
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
            if GRAPH_DATA and not GRAPH_FILE:
                with open(
                        f"graphs/ping_data_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json", "w"
                ) as file:
                    json.dump(ping_result, file, indent=4)

        # if GRAPH_MS:
        #     print_graph_ms.print_graph_ms(ping_result)
        # if GRAPH_FILE:
        #     file = input("Enter filename (default: responses_over_time-[datatime].png):\n>> ") or None
        #     if file:
        #         res_graph_time.print_graph_time(ping_result, file, GRAPH_FILE, GRAPH_DATA)
        #     else:
        #         res_graph_time.print_graph_time(ping_result, graph_data=GRAPH_DATA, graph_file=GRAPH_FILE)

        print_result.print_results(ping_result, device_to_ping, NO_RES_ELEMENTS)

        redo = input("Ping again? (y/n)\n>> ")
        if redo.lower() == "n":
            break
