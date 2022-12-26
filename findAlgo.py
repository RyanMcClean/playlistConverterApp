import os
import logging
from time import sleep

def m4aFinder(artist, album, name, pathToMusic):

    logging.info("Searching for Artist: " + artist + " Album: " + album + " Song: " + name + "\n")

    artistDirs = os.listdir(pathToMusic)

    artist = artist.replace(" ", "")
    sleep(2.5)

    for num, i in enumerate(artistDirs):
        artistCheck = i.replace(" ", "")
        if not artistCheck.startswith(artist[0:1]):
            continue
        elif artistCheck.startswith(artist[0:2]):
            if artistCheck == artist:
                return i



    logging.info("\n\n\n None found \n\n\n")
    return None