import os
from findAlgo import m4aFinder
import settings
from time import sleep

if settings.globalArgs.q:
    from settings import messageQuiet as message
else:
    from settings import messageLoud as message

logger = settings.mainLog


def selection(args):
    if os.path.exists(settings.pathToPlaylistDownloads):
        pass
    else:
        os.makedirs(settings.pathToPlaylistDownloads)
        message("Playlist dir didn't exist. Waiting for playlist downloads")
        while len(os.listdir(settings.pathToPlaylistDownloads)) < 100:
            sleep(30)
    fileList = os.listdir(settings.pathToPlaylistDownloads)
    file = ""
    fileList.sort()
    while len(settings.fileList) < 1:
        for num, f in enumerate(fileList):
            message(str(num + 1) + ". " + f)
        if args.select == 0:
            selection = "all" if args.a else input("\nPlease input a playlist number to convert,"
                          "\n\tif you wish to convert all files,"
                          "\n\tplease type 'all'\n")
        else:
            selection = args.select
        if isinstance(selection, str) and selection.lower() == "all":
            os.system('cls' if os.name == 'nt' else 'clear')
            message("Converting " + str(len(fileList)) + " files")
            settings.fileList = fileList
        elif isinstance(selection, str) and selection.isdigit() or isinstance(selection, int):
            for num, f in enumerate(fileList):
                if (int(selection) - 1) == num:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    message("Converting only " + f[:-4])
                    file = [f]
                    settings.fileList = file
        else:
            message("\nUser input did not match expected. \n\n\tError. \n\nPlease try again.")
            if os.path.exists(settings.pathToPlaylistDownloads):
                fileList = os.listdir(settings.pathToPlaylistDownloads)

def Playlist_Extraction(fileName):
    logger.debug(f"Playlist extracting with args: {settings.pathToPlaylistDownloads}, {settings.pathToMusic}, {fileName}")
    fileName = fileName.strip()
    try:
        downloadTime = os.path.getmtime(settings.pathToPlaylistDownloads + fileName)
        convertTime = os.path.getmtime(settings.convertedPlaylists + fileName.replace("txt", "m3u"))
        if downloadTime < convertTime:
            with open(settings.pathToPlaylistDownloads + fileName) as thing1:
                with open(settings.convertedPlaylists + fileName.replace("txt", "m3u")) as thing2:
                    count = sum(1 for _ in thing1) - 2
                    count -= sum(0.5 for _ in thing2)
                    if count == 0:
                        logger.info(f"Playlist {fileName} is already fully converted, skipping")
                        return int(count), int(count)
    except:
        pass
    playlist = []
    playlist.append(fileName)
    artistDirs = os.listdir(settings.pathToMusic)
    artistDirs.sort()
    missing = 0
    with open(settings.pathToPlaylistDownloads + fileName) as file:
        count = sum(1 for _ in file)
        file.seek(0)
        for num, line in enumerate(file, start=-1):
            if not ",," in line or "snapshot" in line:
                pass
            else:
                message(f"{int((num/count)*100)}%", 'percentage')
                splitLine = line.split(",,")
                if splitLine[1] == 'restricted':
                    artistName = splitLine[2]
                    albumName = splitLine[3]
                    songName = splitLine[4].replace("\n","")
                    toAppend = m4aFinder(artistName, albumName, songName, artistDirs)
                    toAppend = toAppend if (not toAppend is None) else 'restricted'
                else:
                    artistName = splitLine[1]
                    albumName = splitLine[2]
                    songName = splitLine[3].replace("\n","")
                    toAppend = m4aFinder(artistName, albumName, songName, artistDirs)
                if toAppend is None: 
                    logger.error(f"Missing music: %s / %s / %s\n\n", artistName, albumName, songName)
                    missing+=1
                else: 
                    playlist.append(settings.pathToMusic + toAppend)
                    playlist.append(settings.nonLocalMusicPath + toAppend)

    return playlist, missing
