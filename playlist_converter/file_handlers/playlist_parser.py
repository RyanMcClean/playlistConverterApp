"""_summary_

    Returns:
        _type_: _description_
    """
import os
from time import sleep
from logging import Logger
from argparse import Namespace
from typing import Callable


class PlaylistParser:
    """Class to handle parsing of specific playlists
    """

    def __init__(
            self,
            message: Callable,
            logger: Logger = NotImplemented,
            playlist_downloads_path: str = "",
            path_to_music: str = "",
            converted_playlists_path: str = "",
            path_to_non_local_music: str = ""
    ):
        """_summary_

        Args:
            logger (Logger, optional): _description_. Defaults to NotImplemented.
        """
        self.logger = logger
        self.playlist_downloads_path = playlist_downloads_path
        self.message = message
        self.file_list = []
        self.path_to_music = path_to_music
        self.converted_playlists_path = converted_playlists_path
        self.path_to_non_local_music = path_to_non_local_music

    def __selection(self, args: Namespace = NotImplemented):
        """Handles the selection of a playlist to convert
        from the args passed into the application when it
        is run.
        If no args are passed, then it will prompt the
        user to select playlists
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
        while len(file_list) < 1:
            for num, f in enumerate(file_list):
                self.message(str(num + 1) + ". " + f)
            if args.select == 0:
                conversion_selection = "all" if args.a else input(
                    "\nPlease input a playlist number to convert,"
                    "\n\tif you wish to convert all files,"
                    "\n\tplease type 'all'\n")
            else:
                conversion_selection = args.select
            if isinstance(conversion_selection, str) and conversion_selection.lower() == "all":
                os.system('cls' if os.name == 'nt' else 'clear')
                self.message("Converting " + str(len(file_list)) + " files")
                self.file_list = file_list
            elif (isinstance(conversion_selection, str) and conversion_selection.isdigit()
                    or isinstance(conversion_selection, int)):
                for num, f in enumerate(file_list):
                    if (int(conversion_selection) - 1) == num:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        self.message("Converting only " + f[:-4])
                        file = [f]
                        file_list = file
            else:
                self.message(
                    "\nUser input did not match expected. \n\n\tError. \n\nPlease try again.")
                if os.path.exists(self.playlist_downloads_path):
                    file_list = os.listdir(self.playlist_downloads_path)

    def playlist_extraction(self, file_name, args):
        """Extracts artist, album, and song names from a given playlists
        txt file, and returns the playlist as a list of strings

        Args:
            file_name (_type_): _description_

        Returns:
            _type_: _description_
        """
        self.__selection(args)
        self.logger.debug("Playlist extracting with args: %s, %s, %s",
                          self.playlist_downloads_path, self.path_to_music, file_name)
        file_name = file_name.strip()
        try:
            download_time = os.path.getmtime(
                self.playlist_downloads_path + file_name)
            convert_time = os.path.getmtime(
                self.converted_playlists_path + file_name.replace("txt", "m3u"))
            if download_time < convert_time:
                with open(self.playlist_downloads_path + file_name, encoding="utf-8") as file_1:
                    with open(self.converted_playlists_path + file_name.replace("txt", "m3u"),
                              encoding="utf-8") as file_2:
                        count = sum(1 for _ in file_1) - 2
                        count -= sum(0.5 for _ in file_2)
                        if count == 0:
                            self.logger.info(
                                "Playlist %s is already fully converted, skipping", file_name)
                            return int(count), int(count)
        except FileNotFoundError:
            pass
        playlist = []
        playlist.append(file_name)
        artist_dirs = os.listdir(self.path_to_music)
        artist_dirs.sort()
        with open(self.playlist_downloads_path + file_name, encoding="utf-8") as file:
            count = sum(1 for _ in file)
            file.seek(0)
            for num, line in enumerate(file, start=-1):
                if ",," not in line or "snapshot" in line:
                    pass
                else:
                    self.message(f"{int((num / count) * 100)}%", 'percentage')
                    split_line = line.split(",,")
                    if split_line[1] == 'restricted':
                        artist_name = split_line[2]
                        album_name = split_line[3]
                        song_name = split_line[4].replace("\n", "")
                    else:
                        artist_name = split_line[1]
                        album_name = split_line[2]
                        song_name = split_line[3].replace("\n", "")
                    to_append = f"${artist_name} - ${album_name} - ${song_name}"

                    playlist.append(f"${self.path_to_music} - ${to_append}")
                    playlist.append(f"${self.path_to_non_local_music} - ${to_append}")

        return playlist
