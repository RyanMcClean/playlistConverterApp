import os
import logging
from time import sleep

def m4aFinder(artist, album, name, pathToMusic):

    logging.info("Searching for Artist: " + artist + " Album: " + album + " Song: " + name + "\n")

    dirList = os.listdir(pathToMusic)
    dirList.sort()
    counter = 1
    for num, i in enumerate(dirList):
        if (i == artist):
            logging.info(str(counter) + " Found " + i + "\n")
            counter += 1
            return ("Found " + i)
