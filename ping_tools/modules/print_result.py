from colorama import Fore, Style


def print_results(res: dict, device: str, no_res_el: int):
    response_graph = [[" " for _ in range(6)] for _ in range(len(res["times"]))]
    # print(response_graph)

    print("\nResponse Graph (0 <10 <20 <30 <60 <120 <):")
    for i in range(len(res["times"])):
        if res["times"][i] == 0:
            response_graph[i][0] = Fore.RED + "#" + Style.RESET_ALL
        elif res["times"][i] < 10:
            response_graph[i][0] = Fore.GREEN + "#" + Style.RESET_ALL
        elif res["times"][i] < 20:
            response_graph[i][0] = Fore.GREEN + "#" + Style.RESET_ALL
            response_graph[i][1] = Fore.GREEN + "#" + Style.RESET_ALL
        elif res["times"][i] < 30:
            for j in range(3):
                response_graph[i][j] = Fore.GREEN + "#" + Style.RESET_ALL
        elif res["times"][i] < 60:
            for j in range(4):
                response_graph[i][j] = Fore.YELLOW + "#" + Style.RESET_ALL
        elif res["times"][i] < 120:
            for j in range(5):
                response_graph[i][j] = Fore.YELLOW + "#" + Style.RESET_ALL
        else:
            for j in range(6):
                response_graph[i][j] = Fore.RED + "#" + Style.RESET_ALL

    for i in range(len(response_graph)):
        print("".join(response_graph[i]), end="")
        print(f" : {res['times'][i]}ms")

    print("\nResponse Graph in Real Time:\n(1000ms = 1 x #)\n   ", end="")

    for i in res["times"]:

        if i == 0:
            print(Fore.RED + "####" * no_res_el + Style.RESET_ALL, end="")
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

    print("\n", end="")
    print(f"\nPing results for {device}:")
    print(f"  Total requests          : {res['req']}")
    print(f"  Received packets        : {res['res']}")
    print(f"  Lost packets            : {res['lost']}")
    print(f"  Packet loss             : {res['loss']:.2f}%")
    print(f"  Minimum response time   : {res['min']}ms")
    print(f"  Average response time   : {sum(res['times']) / len(res['times']):.2f}ms")
    print(f"  Maximum response time   : {res['max']}ms")

    return response_graph


if __name__ == "__main__":
    print("This is a module for ping_tools")
