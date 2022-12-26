import os
import logging
from time import sleep

def m4aFinder(artist, album, name, pathToMusic):

    logging.info("Searching for Artist: " + artist + " Album: " + album + " Song: " + name + "\n")

    artistDirs = os.listdir(pathToMusic)
    firstArtist = artist.split(",")

    artist = firstArtist[0].replace(" ", "")
    sleep(2.5)

    for num, i in enumerate(artistDirs):
        logging.info("Checking " + i)
        artistCheck = i.replace(" ", "")
        if not artistCheck.startswith(artist[0:1]):
            logging.info("Not " + i)
            continue
        elif artistCheck.startswith(artist[0:2]):
            logging.info("Artist starts like " + i)
            if artistCheck == artist:
                logging.info("Found " + i)
                return i
            # elif:




    logging.info("\n\n\n None found \n\n\n")
    return None