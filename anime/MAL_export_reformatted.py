import xml.dom.minidom
import tkinter as tk
import tkinter.filedialog as filedialog
import os
import json


from colorama import Fore, Style, Back

animes = {"stats": {}, "faults": {"not_completely_watched": []}, "animes": {}}


def select_folder():
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askopenfilename(
        title="Select a MAL XML file",
        filetypes=[("XML", "*.xml")],
        initialdir=f"/users/{os.getlogin()}/Downloads"
    )
    if path == "":
        print("No file selected")
        exit()
    else:
        return path


def get_file_content(file_path):
    with open(file_path, "r", encoding="utf-8") as xml_file:
        return xml_file.read()


def rounded_percentage(value, total):
    if value == 0:
        return 0
    percentage = max(value / total * 100, 1)
    return round(percentage)


def print_bare(watching, watched, hold, dropped, planned, total, title):
    print()
    print(title)

    print(Fore.GREEN + Back.GREEN + "#" * rounded_percentage(watching, total), end="")
    print(Fore.BLUE + Back.BLUE + "#" * rounded_percentage(watched, total), end="")
    print(Fore.YELLOW + Back.YELLOW + "#" * rounded_percentage(hold, total), end="")
    print(Fore.RED + Back.RED + "#" * rounded_percentage(dropped, total), end="")
    print(Fore.LIGHTWHITE_EX + Back.LIGHTWHITE_EX + "#" * rounded_percentage(planned, total), end="")
    print(Style.RESET_ALL)


if __name__ == "__main__":
    file = select_folder()
    file_content = get_file_content(file)
    dom = xml.dom.minidom.parseString(file_content)
    dom.normalize()
    anime_list_xml = dom.getElementsByTagName("anime")
    count_watched = 0
    count_watching = 0
    count_planned = 0
    count_dropped = 0
    count_hold = 0
    count = 0
    count_watched_season = 0
    count_watched_ep = 0
    count_watching_ep = 0
    count_planned_ep = 0
    count_dropped_ep = 0
    count_hold_ep = 0
    count_ep = 0
    count_watched_epw = 0
    count_planned_epw = 0
    count_watching_epw = 0
    count_dropped_epw = 0
    count_hold_epw = 0
    count_epw = 0
    count_season = 0
    season = 0
    last_anime = "----------------------------------"

    for anime in anime_list_xml:
        anime_name = anime.getElementsByTagName("series_title")[0].firstChild.nodeValue
        anime_status = anime.getElementsByTagName("my_status")[0].firstChild.nodeValue
        anime_epw = anime.getElementsByTagName("my_watched_episodes")[0].firstChild.nodeValue
        anime_ep = anime.getElementsByTagName("series_episodes")[0].firstChild.nodeValue
        anime_type = anime.getElementsByTagName("series_type")[0].firstChild.nodeValue
        count_ep += int(anime_ep)
        count_epw += int(anime_epw)
        count_season += 1

        if anime_ep != anime_epw and anime_status == "Completed":
            animes["faults"]["not_completely_watched"].append(anime_name)
        if last_anime not in anime_name:
            count += 1
            season = 1
            last_anime = anime_name

            animes["animes"][anime_name] = [
                {"name": anime_name, "status": anime_status, "ep": anime_ep, "epw": anime_epw, "season": season,
                 "type": anime_type}
            ]

            if anime_status == "Completed":
                count_watched += 1

        else:
            season += 1
            animes["animes"][last_anime].append(
                {"name": anime_name, "status": anime_status, "ep": anime_ep, "epw": anime_epw, "season": season,
                 "type": anime_type}
            )
        if anime_status == "Completed":
            count_watched_ep += int(anime_ep)
            count_watched_epw += int(anime_epw)
            count_watched_season += 1
        elif anime_status == "Watching":
            count_watching += 1
            count_watching_ep += int(anime_ep)
            count_watching_epw += int(anime_epw)
        elif anime_status == "Plan to Watch":
            count_planned += 1
            count_planned_ep += int(anime_ep)
            count_planned_epw += int(anime_epw)
        elif anime_status == "Dropped":
            count_dropped += 1
            count_dropped_ep += int(anime_ep)
            count_dropped_epw += int(anime_epw)
        elif anime_status == "On-Hold":
            count_hold += 1
            count_hold_ep += int(anime_ep)
            count_hold_epw += int(anime_epw)

    animes["stats"]["total"] = count
    animes["stats"]["status"] = {}
    animes["stats"]["status"]["completed"] = count_watched
    animes["stats"]["status"]["watching"] = count_watching
    animes["stats"]["status"]["plan to watch"] = count_planned
    animes["stats"]["status"]["dropped"] = count_dropped
    animes["stats"]["status"]["on-hold"] = count_hold
    animes["stats"]["status_mal"] = {}
    animes["stats"]["status_mal"]["Completed"] = count_watched_season
    animes["stats"]["status_mal"]["Watching"] = count_watching
    animes["stats"]["status_mal"]["Plan to watch"] = count_planned
    animes["stats"]["status_mal"]["Dropped"] = count_dropped
    animes["stats"]["status_mal"]["On-hold"] = count_hold
    animes["stats"]["ep"] = {}
    animes["stats"]["ep"]["total"] = count_ep
    animes["stats"]["ep"]["completed"] = count_watched_ep
    animes["stats"]["ep"]["watching"] = count_watching_ep
    animes["stats"]["ep"]["plan to watch"] = count_planned_ep
    animes["stats"]["ep"]["dropped"] = count_dropped_ep
    animes["stats"]["ep"]["on-hold"] = count_hold_ep
    animes["stats"]["epw"] = {}
    animes["stats"]["epw"]["total"] = count_epw
    animes["stats"]["epw"]["completed"] = count_watched_epw
    animes["stats"]["epw"]["watching"] = count_watching_epw
    animes["stats"]["epw"]["plan to watch"] = count_planned_epw
    animes["stats"]["epw"]["dropped"] = count_dropped_epw
    animes["stats"]["epw"]["on-hold"] = count_hold_epw

    print(f"                  : Total Anime   : %            : Total Seasons   : %            : Total EP   : %         "
          f"   : Total EP Watched   : %         ")
    print("------------------------------------------------------------------------------------------------------------"
          "-------------------------------------")
    print(
        Fore.GREEN + f"  Watching        : {count_watching:<12}  : {str(round(count_watching / count * 100, 2)) + '%':<12}"
                     f" : {count_watching:<15} : {str(round(count_watching_ep / count_ep * 100, 2)) + '%':<12}"
                     f" : {count_watching_ep:<10} : {str(round(count_watching_ep / count_ep * 100, 2)) + '%':<12}"
                     f" : {count_watching_epw:<18} : {str(round(count_watching_epw / count_epw * 100, 2)) + '%'}")
    print(
        Fore.BLUE + f"  Completed       : {count_watched:<12}  : {str(round(count_watched / count * 100, 2)) + '%':<12}"
                    f" : {count_watched_season:<15} : {str(round(count_watched_ep / count_ep * 100, 2)) + '%':<12}"
                    f" : {count_watched_ep:<10} : {str(round(count_watched_ep / count_ep * 100, 2)) + '%':<12}"
                    f" : {count_watched_epw:<18} : {str(round(count_watched_epw / count_epw * 100, 2)) + '%'}")
    print(Fore.YELLOW + f"  On-hold         : {count_hold:<12}  : {str(round(count_hold / count * 100, 2)) + '%':<12}"
                        f" : {count_hold:<15} : {str(round(count_hold_ep / count_ep * 100, 2)) + '%':<12} : {count_hold_ep:<10}"
                        f" : {str(round(count_hold_ep / count_ep * 100, 2)) + '%':<12} : {count_hold_epw:<18}"
                        f" : {str(round(count_hold_epw / count_epw * 100, 2)) + '%'}")
    print(
        Fore.RED + f"  Dropped         : {count_dropped:<12}  : {str(round(count_dropped / count * 100, 2)) + '%':<12}"
                   f" : {count_dropped:<15} : {str(round(count_dropped_ep / count_ep * 100, 2)) + '%':<12}"
                   f" : {count_dropped_ep:<10} : {str(round(count_dropped_ep / count_ep * 100, 2)) + '%':<12}"
                   f" : {count_dropped_epw:<18} : {str(round(count_dropped_epw / count_epw * 100, 2)) + '%'}")
    print(Style.RESET_ALL, end="")
    print(f"  Plan to watch   : {count_planned:<12}  : {str(round(count_planned / count * 100, 2)) + '%':<12}"
          f" : {count_planned:<15} : {str(round(count_planned_ep / count_ep * 100, 2)) + '%':<12}"
          f" : {count_planned_ep:<10} : {str(round(count_planned_ep / count_ep * 100, 2)) + '%':<12}"
          f" : {count_planned_epw:<18} : {str(round(count_planned_epw / count_epw * 100, 2)) + '%'}")
    print("------------------------------------------------------------------------------------------------------------"
          "-------------------------------------")
    print(f"  Total           : {count:<12}  : {str(round(count / count * 100, 2)) + '%':<12} : {count_season:<15}"
          f" : {str(round(count_ep / count_ep * 100, 2)) + '%':<12} : {count_ep:<10}"
          f" : {str(round(count_ep / count_ep * 100, 2)) + '%':<12} : {count_epw:<18}"
          f" : {str(round(count_epw / count_epw * 100, 2)) + '%'}")
    print("------------------------------------------------------------------------------------------------------------"
          "-------------------------------------")
    print_bare(count_watching, count_watched, count_hold, count_dropped, count_planned, count, "Total Anime: ")
    print_bare(count_watching, count_watched_season, count_hold, count_dropped, count_planned, count_season,
               "Total Seasons: ")
    print_bare(count_watching_ep, count_watched_ep, count_hold_ep, count_dropped_ep, count_planned_ep, count_ep,
               "Total EP: ")
    print_bare(count_watching_epw, count_watched_epw, count_hold_epw, count_dropped_epw, count_planned_epw, count_epw,
               "Total EP Watched: ")

    output = json.dumps(animes, indent=4)
    with open("anime.json", "w", encoding="utf-8") as f:
        f.write(output)
    input("\nPress Enter to exit")
