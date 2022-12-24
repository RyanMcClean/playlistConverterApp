import os
import logging
from time import sleep

def m4aFinder(artist, album, name, pathToMusic):

    logging.info("Searching for Artist: " + artist + " Album: " + album + " Song: " + name + "\n")

    splitArtist = artist.split(", ")

    for i in splitArtist:
        artistToFind = i
        break

    dirList = os.listdir(pathToMusic)
    dirList.sort()
    x = len(artistToFind)
    logging.info("Searching for " + artistToFind + "\n")
    for i in dirList:
        while i in artist:
            if (i.startswith(artistToFind[0:x])):
                logging.info("Found " + i + "\n\n")
                albumDirs = os.listdir(pathToMusic + "/" + i)
                for j in albumDirs:
                    while j in album:
                        if (j.startswith(album)):
                            logging.info("Found " + j + "\n\n")
                            return ("Found " + i + "/" + j)

            x -= 1

            if x < 1 :
                break

    return None