import os
import logging
from time import sleep
from pathlib import Path

def m4aFinder(artist, album, name, pathToMusic):

    logging.info("Searching for Artist: " + artist + " Album: " + album + " Song: " + name + "\n")

    for path in Path(pathToMusic).iterdir():
        if path.is_dir():
            print(path)

    logging.info("\n\n\n None found \n\n\n")
    return None