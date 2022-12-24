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


    logging.info("Searching for " + artistToFind + "\n")
    for i in dirList:
        x = len(artistToFind)
        while i in artist:
            logging.info("Searching in " + i)
            logging.info("Searching for " + artistToFind[0:x])
            if (i.startswith(artistToFind[0:x])):
                logging.info("Found artist " + i + "\n")
                albumDirs = os.listdir(pathToMusic + "/" + i)
                for j in albumDirs:
                    y = len(album)
                    while j in album[0:int(0.8*len(album))]:
                        logging.info("Searching in " + j)
                        logging.info("Searching for " + album[0:y])
                        if (j.startswith(album[0:y])):
                            logging.info("Found album " + j + "\n\n")
                            return ("Found " + i + "/" + j)

                        y -= 1
                        if y < 2:
                            break
            x -= 1
            if x < 2 :
                break

    return None