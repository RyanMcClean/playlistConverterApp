import os
import logging
from time import sleep

def m4aFinder(artist, album, name, pathToMusic):

    logging.info("Searching for Artist: " + artist + " Album: " + album + " Song: " + name + "\n")

    dirList = os.listdir(pathToMusic)
    dirList.sort()
    for num, i in enumerate(dirList):
        if artist in i:
            if (i == artist):
                logging.info("Found " + i + "\n")
                return ("Found " + i)
        print("not found")

