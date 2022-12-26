import os
import logging
from time import sleep

def m4aFinder(artist, album, name, pathToMusic, v):

    logging.info("Searching for Artist: " + artist + " Album: " + album + " Song: " + name + "\n")

    artistDirs = os.listdir(pathToMusic)
    firstArtist = artist.split(",")
    artist = firstArtist[0].replace(" ", "")
    album = album.replace(" ", "")
    name = name.replace(" ", "")

    artistDirs.sort()
    for num, i in enumerate(artistDirs):
        if v == "y":
            logging.info("Checking artist " + i)
        if not i.startswith(artist[0:1]):
            if v == "y":
                logging.info(i + " Not " + artist)
            continue
        artistCheck = i.replace(" ", "")
        artistCheck = artistCheck.replace("．", ".")
        artistCheck = artistCheck.replace("：", ":")
        artistCheck = artistCheck.replace("／", "/")
        artistCheck = artistCheck.replace("？", "?")
        artistCheck = artistCheck.replace("Æ", "Æ")

        if artistCheck.lower() == artist.lower():
            if v == "y":
                logging.info("\n\nFound artist " + i)
            albumDirs = os.listdir(pathToMusic + "/" + i)

            for num, j in enumerate(albumDirs):
                if v=="y":
                    logging.info("Checking album " + j)
                albumCheck = j.replace(" ", "")
                albumCheck = albumCheck.replace("：", ":")
                albumCheck = albumCheck.replace("／", "/")
                albumCheck = albumCheck.replace("．", ".")
                albumCheck = albumCheck.replace("？", "?")

                if not albumCheck.lower().startswith(album[0:1].lower()):
                    if v =="y":
                        logging.info("Not " + j)
                        logging.info(albumCheck)
                        logging.info(album)
                    continue
                elif albumCheck.lower().startswith(album[0:2].lower()):
                    if v=="y":
                        logging.info("Album starts with " + j)
                    if albumCheck.lower() == album.lower():
                        if v == "y":
                            logging.info("\n\nFound album " + j)
                        songDir = os.listdir(pathToMusic + "/" + i + "/" + j)

                        for num, k in enumerate(songDir):
                            if v == "y":
                                logging.info("Checking song " + k)
                            if os.path.isfile(pathToMusic + "/" + i + "/" + j + "/" + k):
                                songCheck = k.replace(" ", "")
                                songCheck = songCheck.replace("：", ":")
                                songCheck = songCheck.replace("／", "/")
                                songCheck = songCheck.replace("．", ".")
                                songCheck = songCheck.replace("？", "?")

                                if not songCheck.lower().endswith(name[len(name)-1:len(name)].lower()):
                                    if v == "y":
                                        logging.info("Not " + k)
                                    continue
                                elif songCheck.lower().endswith(name[len(name)-2:len(name)].lower()):
                                    if v == "y":
                                        logging.info("Song ends with " + k)
                                    if songCheck.lower().endswith(name.lower()):
                                        if v == "y":
                                            logging.info("\n\nFound song " + k)
                                        return "Music/" + i + "/" + j + "/" + k
                                    elif v == "y":
                                        logging.info("The two songs that didn't match")
                                        logging.info(songCheck)
                                        logging.info(name)
                            elif os.path.isdir(pathToMusic + "/" + i + "/" + j + "/" + k):
                                cdDir = os.listdir(pathToMusic + "/" + i + "/" + j + "/" + k)

                                for num, l in enumerate(cdDir):
                                    if v == "y":
                                        logging.info("Checking song " + l)
                                    songCheck = l.replace(" ", "")
                                    songCheck = songCheck.replace("：", ":")
                                    songCheck = songCheck.replace("／", "/")
                                    songCheck = songCheck.replace("．", ".")
                                    songCheck = songCheck.replace("？", "?")

                                    if not songCheck.lower().endswith(name[len(name)-1:len(name)].lower()):
                                        if v == "y":
                                            logging.info("Not " + l)
                                        continue
                                    elif songCheck.lower().endswith(name[len(name)-2:len(name)].lower()):
                                        if v == "y":
                                            logging.info("Song ends with " + l)
                                        if songCheck.lower().endswith(name.lower()):
                                            if v == "y":
                                                logging.info("\n\nFound song " + k + "/" + l)
                                            return "Music/" + i + "/" + j + "/" + k + "/" + l

                    elif v == "y":
                        logging.info("The two that didn't match")
                        logging.info(albumCheck)
                        logging.info(album)

        elif v == "y":
            logging.info("The two that didn't match")
            logging.info(artistCheck)
            logging.info(artist)

    if v == "y": logging.info("\n\n\n None found \n\n\n")
    return None