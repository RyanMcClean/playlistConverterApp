import os
import time
import pandas as pd
from findAlgo import m4aFinder


def selection(CSVdirLoc):
    if os.path.exists(CSVdirLoc):
        fileList = os.listdir(CSVdirLoc)
    else:
        print("Error, no CSV files found, exiting\n")
        exit()
    file = ""
    fileList.sort()
    while True:
        for num, f in enumerate(fileList):
            print(str(num + 1) + ". " + f)
        selection = input("\nPlease input a playlist number to convert,"
                          "\n\tif you wish to convert all files,"
                          "\n\tplease type 'all'\n")
        if selection.lower() == "all":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Converting " + str(len(fileList)) + " files")
            return fileList
        elif selection.isdigit():
            for num, f in enumerate(fileList):
                if (int(selection) - 1) == num:
                    print("Converting only " + f)
                    file = f
                    return file
        else:
            print("\nUser input did not match expected. \n\n\tError. \n\nPlease try again.")
            time.sleep(2)


def CSV_Extraction(CSVdirLoc, pathToMusic, fileList):
    fields = ["Track Name", "Artist Name(s)", "Album Name"]
    df = ""
    playlist = []
    playlist.append(fileList)
    df = pd.read_csv(CSVdirLoc + playlist[0])
    df = df[fields]
    dfCount = len(df)
    j = 0
    # print (dfCount)
    while j < dfCount:
        print("%2d" %(((j/dfCount)*100)) + "%", end="\r")
        songName = ("*" + str(df.loc[j, fields[0]]) + ".m4a")
        artistName = str(df.loc[j, fields[1]])
        albumName = str(df.loc[j, fields[2]])
        #print(m4aFinder(artistName, albumName, songName, pathToMusic))
        playlist.append(m4aFinder(artistName, albumName, songName, pathToMusic))
        j += 1
        # for i in playlist:
        #     print(i)
        # print("\n\n\n")
    print("Conversion complete, now creating file.\n")
    time.sleep(1)
    return playlist
