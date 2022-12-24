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
    y = len(album)
    logging.info("Searching for " + artistToFind + "\n")
    for i in dirList:
        while i in artist:
            logging.info(i)
            logging.info(artistToFind[0:x])
            if (i.startswith(artistToFind[0:x])):
                logging.info("Found artist " + i + "\n")
                albumDirs = os.listdir(pathToMusic + "/" + i)
                for j in albumDirs:
                    while j in album:
                        logging.info(j)
                        logging.info(album[0:y])
                        if (j.startswith(album[0:y])):
                            logging.info("Found album " + j + "\n\n")
                            return ("Found " + i + "/" + j)

                        y -= 1
                        if y < 1:
                            break
            x -= 1
            if x < 1 :
                break

    return None