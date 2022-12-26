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

    artistDirs.sort()
    for num, i in enumerate(artistDirs):
        logging.info("Checking artist " + i)
        artistCheck = i.replace(" ", "")
        artistCheck = artistCheck.replace("．", ".")
        if not artistCheck.startswith(artist[0:1]):
            logging.info("Not " + i)
            continue
        elif artistCheck.lower().startswith(artist[0:2].lower()):
            logging.info("Artist starts like " + i)
            if artistCheck.lower() == artist.lower():
                logging.info("\n\nFound artist " + i)
                albumDirs = os.listdir(pathToMusic + "/" + i)

                for num, j in enumerate(albumDirs):
                    logging.info("Checking album " + j)
                    albumCheck = j.replace(" ", "")
                    albumCheck = albumCheck.replace("：", ":")
                    if not albumCheck.lower().startswith(album[0:1].lower()):
                        logging.info("Not " + j)
                        logging.info(albumCheck)
                        logging.info(album)
                        continue
                    elif albumCheck.lower().startswith(album[0:2].lower()):
                        logging.info("Album starts with " + j)
                        if albumCheck.lower() == album.lower():
                            logging.info("\n\nFound album " + j)
                            songDir = os.listdir(pathToMusic + "/" + i + "/" + j)

                            for num, k in enumerate(songDir):
                                logging.info("Checking song " + k)
                                if os.path.isfile(pathToMusic + "/" + i + "/" + j + "/" + k):
                                    songCheck = k.replace(" ", "")
                                    if not songCheck.lower().endswith(name[len(name)-1:len(name)].lower()):
                                        logging.info("Not " + k)
                                        continue
                                    elif songCheck.lower().endswith(name[len(name)-2:len(name)].lower()):
                                        logging.info("Song ends with " + k)
                                        if songCheck.lower().endswith(name.lower()):
                                            logging.info("\n\nFound song " + k)
                                            return i + "/" + j + "/" + k
                                        else:
                                            logging.info("The two songs that didn't match")
                                            logging.info(songCheck)
                                            logging.info(name)
                                elif os.path.isdir(pathToMusic + "/" + i + "/" + j + "/" + k):
                                    cdDir = os.listdir(pathToMusic + "/" + i + "/" + j + "/" + k)

                                    for num, l in enumerate(cdDir):
                                        logging.info("Checking song " + l)
                                        songCheck = l.replace(" ", "")
                                        if not songCheck.lower().endswith(name[len(name)-1:len(name)].lower()):
                                            logging.info("Not " + l)
                                            continue
                                        elif songCheck.lower().endswith(name[len(name)-2:len(name)].lower()):
                                            logging.info("Song ends with " + l)
                                            if songCheck.lower().endswith(name.lower()):
                                                logging.info("\n\nFound song " + k + "/" + l)
                                                return i + "/" + j + "/" + k + "/" + l


                        else:
                            logging.info("The two that didn't match")
                            logging.info(albumCheck)
                            logging.info(album)

            else:
                logging.info("The two that didn't match")
                logging.info(artistCheck)
                logging.info(artist)

    logging.info("\n\n\n None found \n\n\n")
    return None