import os
import logging
from time import sleep

def m4aFinder(artist, album, name, pathToMusic):

    logging.info("Searching for Artist: " + artist + " Album: " + album + " Song: " + name + "\n")

    artistDirs = os.listdir(pathToMusic)

    artist = artist.replace(" ", "")
    print(len(artistDirs))
    sleep(5)
    for num, i in enumerate(artistDirs):
        i = i.replace(" ", "")
        artistDirs[num] = i

    for i in artistDirs:
        if not i.startswith(artist[0:2]):
            artistDirs.remove(i)
    print(len(artistDirs))

    logging.info("\n\n\n None found \n\n\n")
    return None