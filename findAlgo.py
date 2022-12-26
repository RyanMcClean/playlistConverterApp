import os
import logging
from time import sleep

def m4aFinder(artist, album, name, pathToMusic):

    logging.info("Searching for Artist: " + artist + " Album: " + album + " Song: " + name + "\n")

    artistDirs = os.listdir(pathToMusic)
    firstArtist = artist.split(",")

    artist = firstArtist[0].replace(" ", "")
    album = album.replace(" ", "")
    name = name.replace(" ", "")


    for num, i in enumerate(artistDirs):
        logging.info("Checking artist " + i)
        artistCheck = i.replace(" ", "")
        if not artistCheck.startswith(artist[0:1]):
            logging.info("Not " + i)
            continue
        elif artistCheck.startswith(artist[0:2]):
            logging.info("Artist starts like " + i)
            if artistCheck == artist:
                logging.info("Found " + i)
                albumDirs = os.listdir(pathToMusic + "/" + i)

                for num, j in enumerate(albumDirs):
                    logging.info("Checking album " + j)
                    albumCheck = j.replace(" ", "")
                    if not albumCheck.startswith(album[0:1]):
                        logging.info("Not " + j)
                        continue
                    elif albumCheck.startswith(album[0:2]):
                        logging.info("Album starts with " + j)
                        if albumCheck == album:
                            return (i + "/" + j)

    logging.info("\n\n\n None found \n\n\n")
    return None