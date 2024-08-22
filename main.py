#!/usr/bin/python3

import os
import logging
import threading
from time import sleep
from collections import OrderedDict

from CSVtoArray import CSV_Extraction, selection
from fileCreator import playlistFileCreation
from musicMover import musicCopy
from playlistDownloader import playlistdownloader
from unZipper import unzipper

downloadsPath = "/home/ryan_urq/Downloads/"
namePlaylistsDir = "spotify_playlists/"
pathToMusic = "/export/NAS/Music/"
pathToFinalPlaylist = "/export/NAS/Playlists/"
pathToOriginalMusic = "/mnt/windows-share/Users/ryan1/Music/Soggfy"
playlist = []



if __name__ == "__main__":
    # TODO Change logging levels so verbose mode changes logging level, would remove all the dumb if statements
    logging.basicConfig(filename = "/home/ryan_urq/playlistCSVConverterApp/playlistConverterLog.txt", filemode = "w",
                        format = "%(name)s - %(levelname)s - %(message)s", level = logging.DEBUG)
    os.system('cls' if os.name == 'nt' else 'clear')

    # move music from laptop to NAS
    x = threading.Thread(target=musicCopy, args=(pathToOriginalMusic, pathToMusic))
    x.start()
    #musicCopy(pathToOriginalMusic, pathToMusic)

    sleep(0.5)
    v = input("\nVerbose? y/n\n\n")

    # # Download zipped file of spotify playlists
    # y = threading.Thread(target=playlistdownloader, args=(downloadsPath,))
    # y.start()
    # playlistdownloader(downloadsPath)

    # unzip playlists file
    unzipper(downloadsPath, downloadsPath + namePlaylistsDir)


    fileList = selection(downloadsPath + namePlaylistsDir)
    counter = 0
    loopCounter = 0
    filesMissingPerPlaylist = {}

    if isinstance(fileList, str):
        playlist = CSV_Extraction(downloadsPath + namePlaylistsDir, pathToMusic, fileList, v)
        counter += playlistFileCreation(pathToFinalPlaylist, playlist)
        filesMissingPerPlaylistString = (fileList + "\t-\t" + str(counter))

    else:
        for i in fileList:
            loopCounter += 1
            print("%2d" % ((loopCounter/len(os.listdir(downloadsPath + namePlaylistsDir)))*100) + "%")
            print("Converting " + i)
            playlist = CSV_Extraction(downloadsPath + namePlaylistsDir, pathToMusic, i, v)
            counterAdder = playlistFileCreation(pathToFinalPlaylist, playlist)
            if counterAdder > 0:
                filesMissingPerPlaylist.update({counterAdder: "songs missing from:\t" + i})
            counter += counterAdder
            os.system('cls' if os.name == 'nt' else 'clear')

    print(str(counter) + " total missing songs from library")
    logging.info(str(counter) + " total missing songs from library")

    filesMissingPerPlaylist = OrderedDict(sorted(filesMissingPerPlaylist.items()))


    if len(filesMissingPerPlaylist) > 0:

        for key, value in filesMissingPerPlaylist.items():
            print(f"{key} {value}")
            logging.info(f"{key} {value}")

    else:
        for key, value in filesMissingPerPlaylist.items():
            print(f"{key} {value}")
            logging.info(f"{key} {value}")
