import os
import logging
from time import sleep

def m4aFinder(artist, album, name, pathToMusic):

    logging.info("Searching for Artist: " + artist + " Album: " + album + " Song: " + name + "\n")

    dirList = os.listdir(pathToMusic)
    dirList.sort()
    x = 0
    for num, i in enumerate(dirList):
        if i in artist:
            if (i == artist[:-x]):
                logging.info("Found " + i + "\n")
                return ("Found " + i)

        x += 1
