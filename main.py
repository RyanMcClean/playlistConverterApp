import os
import threading

from CSVtoArray import CSV_Extraction, selection
from fileCreator import playlistFileCreation
from musicMover import musicCopy
from playlistDownloader import playlistdownloader
from unZipper import unzipper

downloadsPath = "/home/ryan_urq/Downloads/"
namePlaylistsDir = "spotify_playlists/"
pathToMusic = "//Openmediavault/nas/Music/"
pathToFinalPlaylist = "//Openmediavault/nas/Playlists/"
pathToOriginalMusic = "/mnt/windows-share/Users/ryan1/Music/Soggfy/"
playlist = []

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')

    # move music from laptop to NAS
    x = threading.Thread(target=musicCopy, args=(pathToOriginalMusic, pathToMusic))
    x.start()

    # Download zipped file of spotify playlists
    playlistdownloader(downloadsPath)

    # unzip playlists file
    unzipper(downloadsPath, downloadsPath + namePlaylistsDir)

    fileList = selection(downloadsPath + namePlaylistsDir)

    if isinstance(fileList, str):
        playlist = CSV_Extraction(downloadsPath + namePlaylistsDir, pathToMusic, fileList)
        playlistFileCreation(pathToFinalPlaylist, playlist)

    else:
        for i in fileList:
            print("converting " + i)
            playlist = CSV_Extraction(downloadsPath + namePlaylistsDir, pathToMusic, i)
            playlistFileCreation(pathToFinalPlaylist, playlist)
