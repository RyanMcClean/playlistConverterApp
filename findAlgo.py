import os
import logging
from time import sleep

def m4aFinder(artist, album, name, pathToMusic):

    logging.info("Searching for Artist: " + artist + " Album: " + album + " Song: " + name + "\n")

    artistDirs = os.listdir(pathToMusic)

    for num, i in enumerate(artistDirs):
        i.replace(" ", "")
        artistDirs[num] = i

    for i in artistDirs:
        print(i)

    logging.info("\n\n\n None found \n\n\n")
    return None