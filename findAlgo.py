import os
import logging
from time import sleep

def m4aFinder(artist, album, name, pathToMusic):

    logging.info("Searching for Artist: " + artist + " Album: " + album + " Song: " + name + "\n")

    musicPaths = os.scandir(pathToMusic)

    for dirs in musicPaths:
        if dirs.is_dir():
            print(dirs.path)

    logging.info("\n\n\n None found \n\n\n")
    return None