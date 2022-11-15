# This function unzips the spotify_playlist.zip file. It specifically targets that name
# if the name of the file is altered this will not work.
import os
import time
from zipfile import ZipFile


def unzipper(zipFileLocation, unZipFileLocation):
    print("Unzipping file\n")
    # This section makes the directory in which all the csv files will be placed
    for root, dirs, files in os.walk(zipFileLocation):
        for file in files:
            if file.endswith("playlists.zip"):
                zipFileLocation = zipFileLocation + file
                os.makedirs(unZipFileLocation, exist_ok=True)
    # print (zipFileLocation)
    # This unzips the files into the location
    with ZipFile(zipFileLocation, 'r') as zObject:
        zObject.extractall(unZipFileLocation)
    # This checks the directory that the CSV files were unzipped to exists
    check = ""
    for root, dirs, files in os.walk("C:\\Users\\ryan1\\Downloads\\"):
        for dir in dirs:
            # print (dir)
            if dir.endswith("playlists"):
                check = zipFileLocation.replace("spotify_playlists.zip", "") + dir
            else:
                print("Error finding dir")

    if os.path.exists(check):
        print("\nUnzipping successful\n")
        os.remove(zipFileLocation)
    else:
        print("Error unzipping file")

    time.sleep(1)
