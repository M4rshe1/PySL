# script to download youtube videos

from pytube import YouTube
from pytube import Playlist
import os

# check if download folder exists
# if not create one
if not os.path.exists("downloads"):
    os.makedirs("downloads")

# check if download/youtube folder exists
# if not create one
if not os.path.exists("downloads/youtube"):
    os.makedirs("downloads/youtube")


def download_audio(link, do_playlist):

    # download playlist
    # print(do_playlist)
    if do_playlist:
        try:
            youtube_playlist = Playlist(link)
            download_video_folder = "downloads/Youtube Playlist - " + youtube_playlist.title
            print("Playlist Title: ", youtube_playlist.title)

            # check if folder with playlist name exists
            # if not create one
            if not os.path.exists(download_video_folder):
                os.makedirs(download_video_folder)

            for video in youtube_playlist.videos:
                print("Downloading...")
                audio_stream = video.streams.filter(only_audio=True).first()
                audio_stream.download(download_video_folder)
                print("Download completed!!")
        except Exception as e:
            print("a1 Connection Error: ", e)

    else:
        try:
            # object creation using YouTube which was imported in the beginning
            yt = YouTube(link)
            print("Video Title: ", yt.title)

            # to download the highest quality video
            ys = yt.streams.get_audio_only()
            print("Downloading...")
            # starting download
            ys.download("downloads")
            print("Download completed!!")

        except Exception as ee:
            print("a2 Connection Error: ", ee)


def download_video(link, do_playlist):
    if do_playlist:
        youtube_playlist = Playlist(link)
        download_video_folder = "downloads/Youtube Playlist - " + youtube_playlist.title
        print("Playlist Title: ", youtube_playlist.title)
        for video in do_playlist.videos:
            try:
                video.streams.filter(progressive=True, file_extension="mp4").first().download(
                    output_path=download_video_folder)
                print(f"Downloaded: {video.title}")
            except Exception as e:
                print(f"v1 Error downloading {video.title}: {str(e)}")
    else:
        try:
            # set file name
            # object creation using YouTube which was imported in the beginning
            yt = YouTube(link)
            print("Video Title: ", yt.title)

            # to download the highest quality video
            ys = yt.streams.get_highest_resolution()
            print("Downloading...")
            # starting download
            ys.download("downloads/youtube")
            print("Download completed!!")

        except Exception as e:
            print("v2 Connection Error: ", e)


if __name__ == "__main__":
    while True:
        video_link = input("link of the video/PlayList to be downloaded. \nPlaylists has to be at least unlisted!\n>> ")
        if video_link == "":
            print("Invalid input, Try again.")
            continue
        if video_link == "exit":
            break
        # check if link is valid
        playlist = True
        if video_link.startswith("https://www.youtube.com/watch?v="):
            playlist = False

        elif video_link.startswith("https://www.youtube.com/playlist?list="):
            print("Playlist detected.")
            playlist = True
        else:
            print("Invalid link, Try again.")
            continue

        mode = input("Mode: \n1 : audio\n2 : video\n>> ")
        if mode == "1":
            download_audio(video_link, playlist)
            break
        elif mode == "2":
            download_video(video_link, playlist)
            break
        else:
            print("Invalid input, Try again.")
