import os
import logging

def m4aFinder(artist, album, name, pathToMusic):

    logging.info("\n Searching for Artist: " + artist + " Album: " + album + " Song: " + name)

    dirList = os.listdir(pathToMusic)
    dirList.sort()

    while True:
        listToSearch = dirList

        for i in listToSearch:
            if i == artist:
                print("Found " + i)