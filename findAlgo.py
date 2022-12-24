import os
import logging
from time import sleep

def m4aFinder(artist, album, name, pathToMusic):

    logging.info("Searching for Artist: " + artist + " Album: " + album + " Song: " + name + "\n")

    artist = artist.split(", ")

    for i in artist:
        artistToFind = i
        break

    dirList = os.listdir(pathToMusic)
    dirList.sort()
    x = len(artist)
    logging.info("Searching for " + artistToFind + "\n\n")
    for num, i in enumerate(dirList):
        while i in artistToFind:
            if (i == artistToFind[0:x]):
                logging.info("Found " + i + "\n")
                return ("Found " + i)

            x -= 1

            if x < 1 :
                break

    return None