#!/usr/local/bin/python

import os
import logging
from collections import OrderedDict
import argparse
from time import sleep

from PlaylistParser import Playlist_Extraction, selection
from fileCreator import playlistFileCreation
from playlistDownloader import main as downloadPlaylists

downloadsPath = "/home/ryan_urq/playlistCSVConverterApp/playlists/"
pathToMusic = "/export/NAS/Music/"
pathToFinalPlaylist = "/export/NAS/Playlists/"
playlist = []

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Convert some playlists.')
    parser.add_argument('-v', action='store_true', help='set application to verbose mode')
    parser.add_argument('-a', action='store_true', help='Convert all playlists')
    parser.add_argument('select', metavar='N', type=int, nargs='?', default=0, help='Number of playlist to be converted, will override "-a" option')
    args = parser.parse_args()
    
    # TODO Change logging levels so verbose mode changes logging level, would remove all the dumb if statements
    if args.v:
        logging.basicConfig(filename = "/home/ryan_urq/playlistCSVConverterApp/playlistConverterLog.txt", filemode="w",
                        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.DEBUG)
        logging.debug("Logging set to debug\n\n")
    else:
        logging.basicConfig(filename = "/home/ryan_urq/playlistCSVConverterApp/playlistConverterLog.txt", filemode="w",
                        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
        logging.info("Logging set to info\n\n")

        
    os.system('cls' if os.name == 'nt' else 'clear')

    downloadPlaylists()
    
    # fileList = selection(downloadsPath, args)
    # counter = 0
    # loopCounter = 0
    # filesMissingPerPlaylist = {}
    
    # if isinstance(fileList, str):
    #     playlist = Playlist_Extraction(downloadsPath, pathToMusic, fileList, pathToFinalPlaylist)
    #     if isinstance(playlist, int):
    #         counter = playlist
    #     else:
    #         counter += playlistFileCreation(pathToFinalPlaylist, playlist)
    #     filesMissingPerPlaylist.update({counter: "songs missing from:\t" + fileList})

    # else:
    #     os.system('cls' if os.name == 'nt' else 'clear')
    #     for i in fileList:
    #         loopCounter += 1
    #         print("%2d" % ((loopCounter/len(os.listdir(downloadsPath)))*100) + "%")
    #         print("Converting " + i)
    #         playlist = Playlist_Extraction(downloadsPath, pathToMusic, i, pathToFinalPlaylist)
    #         if isinstance(playlist, int):
    #             counterAdder = playlist
    #         else:
    #             counterAdder = playlistFileCreation(pathToFinalPlaylist, playlist)
    #         if counterAdder > 0:
    #             filesMissingPerPlaylist.update({counterAdder: "songs missing from:\t" + i})
    #         counter += counterAdder
    #         logging.info(f"Converted:\t\"%s\"\tMissing %s songs", i, counterAdder)
    #         os.system('cls' if os.name == 'nt' else 'clear')

    # logging.info(f"%s total missing songs from library", str(counter))

    # filesMissingPerPlaylist = OrderedDict(sorted(filesMissingPerPlaylist.items()))
    # if len(filesMissingPerPlaylist) > 0:
    #     for key, value in filesMissingPerPlaylist.items():
    #         print(f"{key} {value}")
    #         logging.info(f"{key} {value}")
            
    logging.info("Application finished")
