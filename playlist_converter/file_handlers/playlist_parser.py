"""_summary_

    Returns:
        _type_: _description_
    """
import os
from time import sleep
from logging import Logger
from argparse import Namespace
from types import MethodType

class PlaylistParser:

    def __init__(self, logger: Logger=NotImplemented, playlist_downloads_path: str="", message: MethodType=NotImplemented):
        """_summary_

        Args:
            logger (Logger, optional): _description_. Defaults to NotImplemented.
        """        
        self.logger = logger
        self.playlist_downloads_path = playlist_downloads_path
        self.message = message

    def selection(self, args: Namespace=NotImplemented, file_list: list[str]=NotImplemented):
        """_summary_

        Args:
            args (_type_): _description_
        """
        if os.path.exists(self.playlist_downloads_path):
            pass
        else:
            os.makedirs(self.playlist_downloads_path)
            self.message("Playlist dir didn't exist. Waiting for playlist downloads")
            while len(os.listdir(self.playlist_downloads_path)) < 100:
                sleep(30)
        file_list = os.listdir(self.playlist_downloads_path)
        file = ""
        file_list.sort()
        while len(settings.fileList) < 1:
            for num, f in enumerate(file_list):
                message(str(num + 1) + ". " + f)
            if args.select == 0:
                conversion_selection = "all" if args.a else input(
                    "\nPlease input a playlist number to convert,"
                            "\n\tif you wish to convert all files,"
                            "\n\tplease type 'all'\n")
            else:
                conversion_selection = args.select
            if isinstance(conversion_selection, str) and conversion_selection.lower() == "all":
                os.system('cls' if os.name == 'nt' else 'clear')
                message("Converting " + str(len(file_list)) + " files")
                settings.fileList = file_list
            elif (isinstance(conversion_selection, str) and conversion_selection.isdigit()
                    or isinstance(conversion_selection, int)):
                for num, f in enumerate(file_list):
                    if (int(conversion_selection) - 1) == num:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        message("Converting only " + f[:-4])
                        file = [f]
                        settings.fileList = file
            else:
                message("\nUser input did not match expected. \n\n\tError. \n\nPlease try again.")
                if os.path.exists(settings.path_to_playlist_downloads):
                    file_list = os.listdir(settings.path_to_playlist_downloads)

    def playlist_extraction(file_name):
        """_summary_

        Args:
            file_name (_type_): _description_

        Returns:
            _type_: _description_
        """
        logger.debug("Playlist extracting with args: %s, %s, %s",
                    settings.path_to_playlist_downloads, settings.path_to_music, file_name)
        file_name = file_name.strip()
        try:
            download_time = os.path.getmtime(settings.path_to_playlist_downloads + file_name)
            convert_time = os.path.getmtime(settings.converted_playlists + file_name.replace("txt", "m3u"))
            if download_time < convert_time:
                with open(settings.path_to_playlist_downloads + file_name, encoding="utf-8") as file_1:
                    with open(settings.converted_playlists + file_name.replace("txt", "m3u"),
                                encoding="utf-8") as file_2:
                        count = sum(1 for _ in file_1) - 2
                        count -= sum(0.5 for _ in file_2)
                        if count == 0:
                            logger.info("Playlist %s is already fully converted, skipping", file_name)
                            return int(count), int(count)
        except FileNotFoundError:
            pass
        playlist = []
        playlist.append(file_name)
        artist_dirs = os.listdir(settings.path_to_music)
        artist_dirs.sort()
        missing = 0
        with open(settings.path_to_playlist_downloads + file_name, encoding="utf-8") as file:
            count = sum(1 for _ in file)
            file.seek(0)
            for num, line in enumerate(file, start=-1):
                if not ",," in line or "snapshot" in line:
                    pass
                else:
                    message(f"{int((num/count)*100)}%", 'percentage')
                    split_line = line.split(",,")
                    if split_line[1] == 'restricted':
                        artist_name = split_line[2]
                        album_name = split_line[3]
                        song_name = split_line[4].replace("\n","")
                        to_append = m4a_finder(artist_name, album_name, song_name, artist_dirs)
                        to_append = to_append if (not to_append is None) else 'restricted'
                    else:
                        artist_name = split_line[1]
                        album_name = split_line[2]
                        song_name = split_line[3].replace("\n","")
                        to_append = m4a_finder(artist_name, album_name, song_name, artist_dirs)
                    if to_append is None:
                        logger.error("Missing music: %s / %s / %s\n\n", artist_name, album_name, song_name)
                        missing+=1
                    else:
                        playlist.append(settings.path_to_music + to_append)
                        playlist.append(settings.non_local_music_path + to_append)

        return playlist, missing
