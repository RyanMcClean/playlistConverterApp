import os
import logging
from time import sleep

def m4aFinder(artist, album, name, pathToMusic):

    logging.info("Searching for Artist: " + artist + " Album: " + album + " Song: " + name + "\n")

    artist = artist.split(", ")
    if artist is list:
        artist = artist[0]
    dirList = os.listdir(pathToMusic)
    dirList.sort()
    x = len(artist)
    logging.info("Searching for " + artist)
    for num, i in enumerate(dirList):
        while i in artist:
            if (i == artist[0:x]):
                logging.info("Found " + i + "\n")
                return ("Found " + i)

            x -= 1

            if x < (0.2 * len(artist)) :
                break

    return None