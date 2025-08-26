"""Main entry point for the playlist conversion application."""

import os
from collections import OrderedDict
import argparse
import threading
from helpers.settings import AppSettings
from file_handlers.file_creator import PlaylistFileCreator
from file_handlers.playlist_parser import PlaylistParser

playlist = []

if __name__ == "__main__":

    # Set up for app
    parser = argparse.ArgumentParser(description='Convert some playlists.')
    parser.add_argument('-v', action='store_true', help='Set application to verbose mode, '
                        'does not affect print amount')
    parser.add_argument('-a', action='store_true', help='Convert all playlists')
    parser.add_argument('-d', action='store_false', help='Download all playlists, must be run '
                        'with -t, or will have no effect')
    parser.add_argument('select', metavar='N', type=int, nargs='?', default=0, help='Number of '
                        'playlist to be converted, will override "-a" option')
    parser.add_argument('-q', action='store_true', help='Set application in quiet mode, does '
                        'not affect log level')
    parser.add_argument('-t', action='store_true', help='Set application to download '
                        'playlists from Spotify as a separate thread')
    args = parser.parse_args()

    settings = AppSettings(args)
    settings.setup_app_args()
    file_creator = PlaylistFileCreator(settings.converted_playlists)
    playlist_parser = PlaylistParser(
        logger=settings.main_log,
        playlist_downloads_path=settings.path_to_playlist_downloads,
        message=settings.message,
        path_to_music=settings.path_to_music,
        converted_playlists_path=settings.converted_playlists
    )
    from spotify.playlistDownloader import main as downloadPlaylists
    from plex.plexPlaylistHandler import updateMusic, main as uploadPLaylistsToPlex

    logger = settings.main_log

    os.system('cls' if os.name == 'nt' else 'clear')

    # Start main app
    settings.message("Starting playlist app...")

    if settings.threaded:
        x = threading.Thread(target=downloadPlaylists)
        x.daemon = args.d
        try:
            x.start()
            updateMusic()
        except RuntimeError as e:
            logger.error("Playlist download has errored, chances are it's just a rate-limit")
            logger.error(e)
    else:
        updateMusic()
        downloadPlaylists()

    COUNTER = 0

    os.system('cls' if os.name == 'nt' else 'clear')
    COUNTER_ADDER = 0
    for num, i in enumerate(settings.file_list, start=0):
        if len(settings.file_list) > 1:
            settings.message(f"{(((num) / len(settings.file_list)) * 100)}%")
        settings.message(f"Converting {i[:-4]}")
        playlist, COUNTER_ADDER = playlist_parser.playlist_extraction(i, args)
        if isinstance(playlist, int):
            COUNTER_ADDER += playlist
        else:
            file_creator.create_playlist_file(playlist)
        if COUNTER_ADDER > 0:
            settings.files_missing_per_playlist.update({COUNTER_ADDER: "songs missing from:\t" + i})
        COUNTER += COUNTER_ADDER
        logger.info("Converted:\t\"%s\"\tMissing %s songs\n\n", i, COUNTER_ADDER)
        if len(settings.file_list) > 1:
            os.system('cls' if os.name == 'nt' else 'clear')

    if len(settings.file_list) > 1:
        logger.info("%s total missing songs from library", str(COUNTER))
        settings.message(f"{str(COUNTER)} total missing songs from library")

    settings.files_missing_per_playlist = OrderedDict(sorted(settings.files_missing_per_playlist.items()))
    if len(settings.files_missing_per_playlist) > 0:
        for key, value in settings.files_missing_per_playlist.items():
            settings.message(f"{key} {value}")
            logger.info("%s %s", key, value)

    settings.message("\nUploading playlists to plex")
    uploadPLaylistsToPlex()
    settings.message("Playlists uploaded to plex\n")

    # if not x.daemon:
    #     while x.is_alive():
    #         message("Waiting on thread to finish")
    #         sleep(1)

    logger.info("Application finished")
    settings.message("Application finished")
