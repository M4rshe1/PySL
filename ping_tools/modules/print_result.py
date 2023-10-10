from datetime import datetime

from colorama import Fore, Style


def print_results(device: str, all_results):
    # print(all_results)
    # get the longest times element in all_results
    longest = all_results[0]
    for i in all_results:
        if len(i["times"]) > len(longest["times"]):
            longest = i

    response_graph = [[" "] for _ in range(len(longest["times"]))]
    # print(response_graph)

    print("\nResponse Graph ((", end="")
    print(Fore.RED + "0" + Style.RESET_ALL, end="")
    print(Fore.GREEN + " <10" + Style.RESET_ALL, end="")
    print(")", end="")
    print(Fore.GREEN + " <20 <30" + Style.RESET_ALL, end="")
    print(Fore.YELLOW + " <60" + Style.RESET_ALL, end="")
    print(Fore.RED + " <120" + Style.RESET_ALL, end="")
    print(Fore.RED + " <" + Style.RESET_ALL, end="")
    print(")")

    for j, res in enumerate(all_results):
        for i in range(len(res["times"])):
            if res["times"][i] == 0:
                response_graph[i].append(Fore.RED + "0      " + Style.RESET_ALL)
            elif res["times"][i] < 10:
                response_graph[i].append(Fore.GREEN + "#      " + Style.RESET_ALL)
            elif res["times"][i] < 20:
                response_graph[i].append(Fore.GREEN + "##     " + Style.RESET_ALL)
            elif res["times"][i] < 30:
                response_graph[i].append(Fore.GREEN + "###    " + Style.RESET_ALL)
            elif res["times"][i] < 60:
                response_graph[i].append(Fore.YELLOW + "####   " + Style.RESET_ALL)
            elif res["times"][i] < 120:
                response_graph[i].append(Fore.YELLOW + "#####  " + Style.RESET_ALL)
            else:
                response_graph[i].append(Fore.RED + "###### " + Style.RESET_ALL)
            response_graph[i].append(f" : {(str(res['times'][i]) + 'ms'):<11}")
            if not len(all_results) == 1 and not j == len(all_results) - 1:
                response_graph[i].append("  |  ")

    for i in range(len(response_graph)):
        print("".join(response_graph[i]))

    print("\nResponse Graph in Real Time:\n(1000ms = 1 x #)")
    for j in all_results:
        print("   ", end="")
        for i in j["times"]:
            if i == 0:
                print(Fore.RED + "0000" + Style.RESET_ALL, end="")
            elif i < 30:
                print(Fore.GREEN + "#" + Style.RESET_ALL, end="")
            elif i < 120:
                print(Fore.YELLOW + "#" + Style.RESET_ALL, end="")
            elif i < 1000:
                print(Fore.RED + "#" + Style.RESET_ALL, end="")
            elif i < 2000:
                print(Fore.RED + "##" + Style.RESET_ALL, end="")
            elif i < 3000:
                print(Fore.RED + "###" + Style.RESET_ALL, end="")
            else:
                print(Fore.YELLOW + "####" + Style.RESET_ALL, end="")
        print("")

    summary = [
        "  Total requests          : ",
        "  Received packets        : ",
        "  Lost packets            : ",
        "  Packet loss             : ",
        "  Minimum response time   : ",
        "  Average response time   : ",
        "  Maximum response time   : "
    ]

    for k, j in enumerate(all_results):
        summary[0] += f"{j['req']:<10}"
        summary[1] += f"{j['res']:<10}"
        summary[2] += f"{j['lost']:<10}"
        summary[3] += f"{str(round(j['loss'], 2)) + '%':<10}"
        summary[4] += f"{j['min']:<10}"
        summary[5] += f"{str(round(sum(j['times']) / len(j['times']), 2)) + 'ms':<10}"
        summary[6] += f"{j['max']:<10}"
        if not len(all_results) == 1 and not k == len(all_results) - 1:
            for i in range(len(summary)):
                summary[i] += " : "

    start_time = datetime.fromtimestamp(round(all_results[0]["start-time"], 0))
    end_time = datetime.fromtimestamp(round(all_results[0]["end-time"], 0))
    time_diff = end_time - start_time
    print("\n", end="")
    print(f"\nPing results for {device}:")
    for i in summary:
        print(i)
    print("\n", end="")
    print(f"  Start time              : {start_time.strftime('%Y.%m.%d %H:%M:%S')}")
    print(f"  End time                : {end_time.strftime('%Y.%m.%d %H:%M:%S')}")
    print(f"  Time                    : "
          f"{str(datetime.utcfromtimestamp(time_diff.total_seconds()).strftime('%HH:%MM:%SS'))}")
    print(f"  Device                  : {all_results[0]['device']}")
    print(f"  Ping Duration           : {all_results[0]['duration']}s")

    return response_graph


if __name__ == "__main__":
    print("This is a module for ping_tools")
