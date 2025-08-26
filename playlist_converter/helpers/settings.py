"""_summary_
    """
import json
import os
import logging
import sys
from typing import Callable


def setup_logger(self, name, log_file, level):
    """To setup as many loggers as you want"""
    self.formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    self.handler = logging.FileHandler(log_file, mode='w')
    self.handler.setFormatter(self.formatter)

    self.logger = logging.getLogger(name)
    self.logger.setLevel(level)
    self.logger.addHandler(self.handler)

    return self.logger


class AppSettings:
    """_summary_
    """

    wd = os.getcwd()

    def __init__(self, app_args):
        """_summary_

        Args:
            appArgs (_type_): _description
        """

        try:
            with open("../appSettings.json", encoding="utf-8") as file:
                self.data = json.load(file)

                # Path variables
                self.path_config = self.data['pathConfig']
                self.path_to_music = self.path_config['music']
                self.path_to_playlist_downloads = self.path_config['downloadPlaylists']
                self.converted_playlists = self.path_config['convertPlaylists']
                self.non_local_music_path = self.path_config['nonLocalMusic']
                self.non_local_converted_playlists = self.path_config['nonLocalConvertedPlaylists']

                # Spotify API Variables
                self.spotify_config = self.data['spotifyAPIConfig']
                self.client_id = self.spotify_config['clientId']
                self.client_secret = self.spotify_config['clientSecret']
                self.redirect_uri = self.spotify_config['redirectURI']
                self.scope = self.spotify_config['scope']
                self.cache_path = self.spotify_config['cachePath']
                self.sleep_time = self.spotify_config['sleepTime']

                # Plex variables
                self.plex_config = self.data['plexConfig']
                self.plex_base_url = self.plex_config['baseURL']
                self.plex_token = self.plex_config['token']

                # App variables
                self.file_list = []
                self.files_missing_per_playlist = {}
                self.global_args = app_args
                self.threaded = False
                self.main_log: logging.Logger
                self.download_log: logging.Logger
                self.message: Callable

        except FileNotFoundError:
            print("Error: appSettings.json not found. Please create the file with the required settings.")
            sys.exit(1)

    def setup_app_args(self):
        """_summary_

        Args:
            app_args (_type_): _description_
        """
        # App arguments
        self.threaded = self.global_args.t

        if self.global_args.v:
            self.main_log = setup_logger(self, "Main logger", "./playlistConverterLog.log", logging.DEBUG)
            self.main_log.debug("Logging set to debug\n\n")
            self.download_log = setup_logger(self, "Downloader logger", "./playlistDownloaderLog.log", logging.DEBUG)
            self.download_log.debug("Logging set to debug\n\n")
        else:
            self.main_log = setup_logger(self, "Main logger", "./playlistConverterLog.log", logging.INFO)
            self.main_log.info("Logging set to info\n\n")
            self.download_log = setup_logger(self, "Downloader logger", "./playlistDownloaderLog.log", logging.INFO)
            self.download_log.debug("Logging set to debug\n\n")

        if self.global_args.q:
            self.message = self.message_quiet
        else:
            self.message = self.message_loud

    class Color:
        """_summary_
        """
        PURPLE = '\033[1;35;48m'
        CYAN = '\033[1;36;48m'
        BOLD = '\033[1;37;48m'
        BLUE = '\033[1;34;48m'
        GREEN = '\033[1;32;48m'
        YELLOW = '\033[1;33;48m'
        RED = '\033[1;31;48m'
        BLACK = '\033[1;30;48m'
        UNDERLINE = '\033[4;37;48m'
        END = '\033[1;37;0m'

    def message_loud(self, text, message_type='text'):
        """_summary_

        Args:
            text (_type_): _description_
            type (str, optional): _description_. Defaults to 'text'.
        """
        if message_type == 'text':
            print(text)
        elif message_type == 'percentage':
            print(text, end='\r')
        elif message_type == 'error':
            print(self.Color.RED + str(text) + self.Color.END)

    def message_quiet(self, text, message_type=None):
        """_summary_

        Args:
            text (_type_): _description_
            type (_type_, optional): _description_. Defaults to None.
        """
