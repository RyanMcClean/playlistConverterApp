import os
import threading

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
    os.system('cls' if os.name == 'nt' else 'clear')

    # move music from laptop to NAS
    x = threading.Thread(target=musicCopy, args=(pathToOriginalMusic, pathToMusic))
    x.start()

    # Download zipped file of spotify playlists
    playlistdownloader(downloadsPath)

    # unzip playlists file
    unzipper(downloadsPath, downloadsPath + namePlaylistsDir)

    fileList = selection(downloadsPath + namePlaylistsDir)
    counter = 0
    loopCounter = 0
    filesMissingPerPlaylist = []

    if isinstance(fileList, str):
        playlist = CSV_Extraction(downloadsPath + namePlaylistsDir, pathToMusic, fileList)
        counter += playlistFileCreation(pathToFinalPlaylist, playlist)

    else:
        for i in fileList:
            counterAdder = 0
            loopCounter += 1
            print("%2d" % ((loopCounter/len(os.listdir(downloadsPath + namePlaylistsDir)))*100) + "%")
            print("Converting " + i)
            playlist = CSV_Extraction(downloadsPath + namePlaylistsDir, pathToMusic, i)
            counterAdder  += playlistFileCreation(pathToFinalPlaylist, playlist)
            if counterAdder > 0:
                filesMissingPerPlaylist.append((str(i) + "-" + str(counterAdder)))
            counter += counterAdder
            os.system('cls' if os.name == 'nt' else 'clear')

    print(str(counter) + " total missing songs from library")

    for i in range(len(filesMissingPerPlaylist)):
        print(filesMissingPerPlaylist[i])
