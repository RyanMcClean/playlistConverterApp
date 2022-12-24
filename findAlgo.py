import os
import logging
from time import sleep

def m4aFinder(artist, album, name, pathToMusic):

    logging.info("Searching for Artist: " + artist + " Album: " + album + " Song: " + name + "\n")

    artist = artist.split(", ")
    if artist is list:
        for i in artist:
            artistToFind = i
            break
    else:
        artistToFind = str(artist)
    dirList = os.listdir(pathToMusic)
    dirList.sort()
    x = len(artist)
    logging.info("Searching for " + artistToFind)
    for num, i in enumerate(dirList):
        while i in artistToFind:
            if (i == artistToFind[0:x]):
                logging.info("Found " + i + "\n")
                return ("Found " + i)

            x -= 1

            if x < 1 :
                break

    return None