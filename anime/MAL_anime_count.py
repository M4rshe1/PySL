import xml.dom.minidom
import tkinter as tk
import tkinter.filedialog as filedialog
import os

animes = []


def select_folder():
    # print("Select a folder")
    root = tk.Tk()
    # print("Select a folder")
    root.withdraw()
    # print("Select a folder")
    path = filedialog.askopenfilename(
        title="Select a MAL XML file",
        filetypes=[("XML", "*.xml")],
        initialdir=f"/users/{os.getlogin()}/Downloads"
    )
    # print("Select a folder")
    if path == "":
        print("No file selected")
        exit()
    else:
        return path


def get_file_content(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


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
    count_watched_ep = 0
    count_watching_ep = 0
    count_planned_ep = 0
    count_dropped_ep = 0
    count_hold_ep = 0
    count_ep = 0

    last_anime = "----------------------------------"
    for anime in anime_list_xml:
        anime_name = anime.getElementsByTagName("series_title")[0].firstChild.nodeValue
        anime_status = anime.getElementsByTagName("my_status")[0].firstChild.nodeValue
        # anime_ep = anime.getElementsByTagName("my_watched_episodes")[0].firstChild.nodeValue
        anime_ep = anime.getElementsByTagName("series_episodes")[0].firstChild.nodeValue
        count_ep += int(anime_ep)
        # print(anime_status)
        # print(anime_name)
        count += 1
        if last_anime not in anime_name:
            last_anime = anime_name
            if anime_status == "Completed":
                count_watched += 1
                count_watched_ep += int(anime_ep)
            elif anime_status == "Watching":
                count_watching += 1
                count_watching_ep += int(anime_ep)
            elif anime_status == "Plan to Watch":
                count_planned += 1
                count_planned_ep += int(anime_ep)
            elif anime_status == "Dropped":
                count_dropped += 1
                count_dropped_ep += int(anime_ep)
            elif anime_status == "On-Hold":
                count_hold += 1
                count_hold_ep += int(anime_ep)

        else:
            if anime_status == "Completed":
                count_watched_ep += int(anime_ep)
            elif anime_status == "Watching":
                count_watching += 1
                count_watching_ep += int(anime_ep)
            elif anime_status == "Plan to Watch":
                count_planned += 1
                count_planned_ep += int(anime_ep)
            elif anime_status == "Dropped":
                count_dropped += 1
                count_dropped_ep += int(anime_ep)
            elif anime_status == "On-Hold":
                count_hold += 1
                count_hold_ep += int(anime_ep)
    print("Category      : Count   : Episodes : Percentage")
    print("------------------------------------------------")
    print(f"Completed     : {count_watched:<8}: {count_watched_ep:<9}: {count_watched/count*100:.2f}%")
    print(f"Watching      : {count_watching:<8}: {count_watching_ep:<9}: {count_watching/count*100:.2f}%")
    print(f"Plan to watch : {count_planned:<8}: {count_planned_ep:<9}: {count_planned/count*100:.2f}%")
    print(f"Dropped       : {count_dropped:<8}: {count_dropped_ep:<9}: {count_dropped/count*100:.2f}%")
    print(f"On-Hold       : {count_hold:<8}: {count_hold_ep:<9}: {count_hold/count*100:.2f}%")
    print("-----------------------------------------------")
    print(f"Total         : {count:<8}: {count_ep:<9}: 100%")
    # print(f"Watched EP    : ")
