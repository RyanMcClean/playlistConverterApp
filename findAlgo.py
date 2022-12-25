import os
import logging
from time import sleep

def m4aFinder(artist, album, name, pathToMusic):

    logging.info("Searching for Artist: " + artist + " Album: " + album + " Song: " + name + "\n")

    for dirs in os.scandir(pathToMusic):
        if dirs.is_dir():
            print(dirs.path)

    logging.info("\n\n\n None found \n\n\n")
    return None