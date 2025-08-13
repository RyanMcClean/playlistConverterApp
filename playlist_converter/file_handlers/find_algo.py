"""This contains the finding algorithm for music files, 'tis a mess"""

import os
from logging import Logger

class SearchAlgorithm:
    """Class to handle searching for music files"""

    def __init__(self, music_root_path: str="", logger: Logger=NotImplemented):
        """Constructor for the search algorithm

        Args:
            music_root_path (str, optional): _description_. Defaults to None.
        """
        self.music_root_path = music_root_path
        self.logger = logger

    def sanatise_input(self, input_string: str):
        """Sanatise input of string, artists use weird names for themselves and songs"""
        input_string = input_string.replace(" ", "")
        input_string = input_string.replace("：", ":")
        input_string = input_string.replace("／", "/")
        input_string = input_string.replace("．", ".")
        input_string = input_string.replace("？", "?")
        input_string = input_string.replace("＂", "\"")
        input_string = input_string.replace("￤", "|")
        input_string = input_string.replace("＊", "*")
        input_string = input_string.replace("＞", ">")
        input_string = input_string.replace("＜", "<")
        return input_string

    def match_strings(self, input_string: str, match_against: str, string_type:str):
        """Match two strings, returns true if they match, 
        use differing rules based on the type of strings to match"""
        logger = self.logger
        input_string_1 = self.sanatise_input(input_string).lower()
        input_string_2 = self.sanatise_input(match_against).lower()
        ans = False
        if (len(input_string_1) > 0 and len(input_string_2) > 0
        and not input_string_1[0] == input_string_2[0]):
            if string_type == "album":
                logger.debug("\"%s\" does not match: \"%s\"", input_string, match_against)
                logger.debug("\"%s\" does not match: \"%s\"", input_string_1, input_string_2)
        elif input_string_2 == input_string_1:
            logger.debug("\"%s\" matches \"%s\"\n\n", input_string, match_against)
            ans = True
        else:
            logger.debug("\"%s\" does not match: \"%s\"", input_string, match_against)
            logger.debug("\"%s\" does not match: \"%s\"", input_string_1, input_string_2)
        return ans

    def m4a_finder(self, artist, album, name, static_artist_dirs):
        """Find music file using artist, album, and name"""
        logger = self.logger
        path_to_music = self.music_root_path
        prefix = ""
        logger.debug("Searching for Artist: %s Album: %s Song: %s\n", artist, album, name)

        artist_dirs = [item for item in static_artist_dirs if len(item) > 0
                    and len(artist) > 0 and artist[0].lower() == item[0].lower()]

        logger.debug("Searching for artist")
        for i in artist_dirs:
            if self.match_strings(i, artist, "artist"):
                logger.debug("Found artist \"%s\"", i)

                path_to_music += i + "/"
                prefix += i + "/"
                logger.debug(path_to_music)

                logger.debug("Searching for album")
                for j in os.listdir(path_to_music):
                    if self.match_strings(j, album, "album"):
                        logger.debug("Found album \"%s\"", j)

                        path_to_music += j + "/"
                        prefix += j + "/"
                        logger.debug(path_to_music)

                        logger.debug("Searching for song or CD")
                        song_or_cd_path = sorted(os.listdir(path_to_music), key=len, reverse=True)
                        for k in song_or_cd_path:
                            logger.debug("Checking %s%s", path_to_music, k)
                            if (os.path.isfile(path_to_music + "/" + k)
                                and k.endswith(('.ogg','.m4a','.mp3'))):
                                logger.debug("Path to file: %s%s", path_to_music, k)
                                song_check = k.split(".", 1)[1].rsplit('.', 1)[0]
                                if self.match_strings(song_check, name, "song"):
                                    logger.debug("Found song \"%s/%s/%s\"", i, j, k)
                                    return prefix + k

                            elif os.path.isdir(path_to_music + "/" + k):
                                logger.debug("Path to directory: %s%s", path_to_music, k)

                                logger.debug("Searching for song in CD")
                                for l in os.listdir(path_to_music + "/" + k):
                                    logger.debug("Checking {pathToMusic}/{k}/{l}")
                                    song_check = l.split(".", 1)[1].rsplit('.', 1)[0]

                                    if self.match_strings(song_check, name, "song"):
                                        logger.debug("Found song \"%s/%s/%s/%s\"", i, j, k, l)
                                        return prefix + k + "/" + l
                        prefix = prefix.replace(j + "/", "")
                        path_to_music = path_to_music.replace(j + "/", "")
            prefix = ""
            path_to_music = self.music_root_path

        return None
