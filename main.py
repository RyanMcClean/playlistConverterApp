#!/usr/local/bin/python

import os
from collections import OrderedDict
import argparse
from time import sleep
import threading

from PlaylistParser import Playlist_Extraction, selection
from fileCreator import playlistFileCreation
from playlistDownloader import main as downloadPlaylists
from plexPlaylistHandler import updateMusic, main as uploadPLaylistsToPlex
import settings


playlist = []


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Convert some playlists.')
    parser.add_argument('-v', action='store_true', help='set application to verbose mode')
    parser.add_argument('-a', action='store_true', help='Convert all playlists')
    parser.add_argument('-d', action='store_false', help='Download all playlists')
    parser.add_argument('select', metavar='N', type=int, nargs='?', default=0, help='Number of playlist to be converted, will override "-a" option')
    args = parser.parse_args()
    
    settings.init(args.v)
    logger = settings.mainLog
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    x = threading.Thread(target=downloadPlaylists, args=(args.v,))
    x.daemon = args.d
    try:
        x.start()
        updateMusic()
    except Exception as e:
        logger.error("Playlist download has errored, chances are it's just a rate-limit")
        logger.error(e)
        
    selection(args)
    counter = 0
    
    os.system('cls' if os.name == 'nt' else 'clear')
    counterAdder = 0
    for num, i in enumerate(settings.fileList, start=0):
        if len(settings.fileList) > 1: print("%2d" % (((num)/len(settings.fileList))*100) + "%")
        print("Converting " + i[:-4])
        playlist, counterAdder = Playlist_Extraction(i)
        if isinstance(playlist, int):
            counterAdder += playlist
        else:
            playlistFileCreation(playlist)
        if counterAdder > 0:
            settings.filesMissingPerPlaylist.update({counterAdder: "songs missing from:\t" + i})
        counter += counterAdder
        logger.info(f"Converted:\t\"%s\"\tMissing %s songs\n\n", i, counterAdder)
        if len(settings.fileList) > 1:
            os.system('cls' if os.name == 'nt' else 'clear')
        

    if len(settings.fileList) > 1:
        logger.info(f"%s total missing songs from library", str(counter))
        print(f"{str(counter)} total missing songs from library")

    settings.filesMissingPerPlaylist = OrderedDict(sorted(settings.filesMissingPerPlaylist.items()))
    if len(settings.filesMissingPerPlaylist) > 0:
        for key, value in settings.filesMissingPerPlaylist.items():
            print(f"{key} {value}")
            logger.info(f"{key} {value}")

    print("\nUploading playlists to plex")
    uploadPLaylistsToPlex()    
    print("Playlists uploaded to plex\n")
    
    if not x.daemon:
        while x.is_alive():
            print("Waiting on thread to finish")
            sleep(1)
            
    logger.info("Application finished")
    print("Application finished")
