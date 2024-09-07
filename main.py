import os, sys
from collections import OrderedDict
import argparse
from time import sleep
import threading
import settings


playlist = []


if __name__ == "__main__":

    # Set up for app
    parser = argparse.ArgumentParser(description='Convert some playlists.')
    parser.add_argument('-v', action='store_true', help='Set application to verbose mode, does not affect print amount')
    parser.add_argument('-a', action='store_true', help='Convert all playlists')
    parser.add_argument('-d', action='store_false', help='Download all playlists, must be run with -t, or will have no effect')
    parser.add_argument('select', metavar='N', type=int, nargs='?', default=0, help='Number of playlist to be converted, will override "-a" option')
    parser.add_argument('-q', action='store_true', help='Set application in quiet mode, does not affect log level')
    parser.add_argument('-t', action='store_true', help='Set application to download playlists from Spotify as a seperate thread')
    args = parser.parse_args()
    
    settings.init(args)
    from PlaylistParser import Playlist_Extraction, selection
    from fileCreator import playlistFileCreation
    from playlistDownloader import main as downloadPlaylists
    from plexPlaylistHandler import updateMusic, main as uploadPLaylistsToPlex
    
    if args.q:
        from settings import messageQuiet as message
    else:
        from settings import messageLoud as message

    logger = settings.mainLog
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Start main app
    message("Starting playlist app...")
    
    if settings.threaded:
        x = threading.Thread(target=downloadPlaylists)
        x.daemon = args.d
        try:
            x.start()
            updateMusic()
            settings.threaded = True
        except Exception as e:
            logger.error("Playlist download has errored, chances are it's just a rate-limit")
            logger.error(e)
    else:
        updateMusic()
        downloadPlaylists()
        
    selection(args)
    counter = 0
    
    os.system('cls' if os.name == 'nt' else 'clear')
    counterAdder = 0
    for num, i in enumerate(settings.fileList, start=0):
        if len(settings.fileList) > 1: message("%2d" % (((num)/len(settings.fileList))*100) + "%")
        message("Converting " + i[:-4])
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
        message(f"{str(counter)} total missing songs from library")

    settings.filesMissingPerPlaylist = OrderedDict(sorted(settings.filesMissingPerPlaylist.items()))
    if len(settings.filesMissingPerPlaylist) > 0:
        for key, value in settings.filesMissingPerPlaylist.items():
            message(f"{key} {value}")
            logger.info(f"{key} {value}")

    message("\nUploading playlists to plex")
    uploadPLaylistsToPlex()    
    message("Playlists uploaded to plex\n")
    
    # if not x.daemon:
    #     while x.is_alive():
    #         message("Waiting on thread to finish")
    #         sleep(1)
            
    logger.info("Application finished")
    message("Application finished")
