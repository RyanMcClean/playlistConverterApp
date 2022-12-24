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
        while True:
            if not i.startswith(artistToFind[0:int(0.4*len(artistToFind))]):
                # logging.info("Not " + i)
                break
            logging.info("Searching in " + i)
            logging.info("Searching for " + artistToFind[0:x])
            if (i.startswith(artistToFind[0:x])):
                logging.info("Found artist " + i + "\n")
                albumDirs = os.listdir(pathToMusic + "/" + i)
                y = len(album)
                for j in albumDirs:

                    while True:
                        # if not j.startswith(album[0:int(0.1*len(album))]):
                        #     break
                        logging.info("Searching in " + j)
                        logging.info("Searching for " + album[0:y])
                        if (j.lower().startswith(album[0:y].lower())):
                            logging.info("Found album " + j + "\n\n")
                            return ("Found " + i + "/" + j)
                        y -= 1
                        if y < (0.85 * len(album)):
                            break


            x -= 1
            if x < (0.5 * len(artistToFind)) :
                break

    return None