import os
from findAlgo import m4aFinder
import settings

def selection(args):
    if os.path.exists(settings.pathToPlaylistDownloads):
        fileList = os.listdir(settings.pathToPlaylistDownloads)
    else:
        print("Error, no playlist files found, exiting\n")
        exit(1)
    file = ""
    fileList.sort()
    while len(settings.fileList) < 1:
        for num, f in enumerate(fileList):
            print(str(num + 1) + ". " + f)
        if args.select == 0:
            selection = "all" if args.a else input("\nPlease input a playlist number to convert,"
                          "\n\tif you wish to convert all files,"
                          "\n\tplease type 'all'\n")
        else:
            selection = args.select
        if isinstance(selection, str) and selection.lower() == "all":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Converting " + str(len(fileList)) + " files")
            settings.fileList = fileList
        elif isinstance(selection, str) and selection.isdigit() or isinstance(selection, int):
            for num, f in enumerate(fileList):
                if (int(selection) - 1) == num:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Converting only " + f[:-4])
                    file = [f]
                    settings.fileList = file
        else:
            print("\nUser input did not match expected. \n\n\tError. \n\nPlease try again.")
            if os.path.exists(settings.pathToPlaylistDownloads):
                fileList = os.listdir(settings.pathToPlaylistDownloads)

def Playlist_Extraction(fileName):
    logger = settings.mainLog
    logger.debug(f"Playlist extracting with args: {settings.pathToPlaylistDownloads}, {settings.pathToMusic}, {fileName}")
    fileName = fileName.strip()
    try:
        if os.path.getmtime(settings.pathToPlaylistDownloads + fileName) < os.path.getmtime(settings.convertedPlaylists + fileName.replace("txt", "m3u8")):
            with open(settings.pathToPlaylistDownloads + fileName) as thing1:
                with open(settings.convertedPlaylists + fileName.replace("txt", "m3u8")) as thing2:
                    count = sum(1 for _ in thing1) - 2
                    count -= sum(1 for _ in thing2)
                    if count == 0:
                        return count
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
                print(f"{int((num/count)*100)}%", end="\r")
                splitLine = line.split(",,")
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
