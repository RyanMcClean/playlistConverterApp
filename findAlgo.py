import os
import logging
from time import sleep

def m4aFinder(artist, album, name, pathToMusic):

    logging.info("Searching for Artist: " + artist + " Album: " + album + " Song: " + name + "\n")

    artistDirs = os.listdir(pathToMusic)

    artist = artist.replace(" ", "")
    print(len(artistDirs))
    sleep(2.5)

    for num, i in artistDirs:
        i = i.replace(" ", "")
        if not i.startswith(artist[0:1]):
            continue
        elif i.startswith(artist[0:2]):
            return i



    print((artistDirs))

    logging.info("\n\n\n None found \n\n\n")
    return None