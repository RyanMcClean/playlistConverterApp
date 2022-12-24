import os
import logging
from time import sleep

def m4aFinder(artist, album, name, pathToMusic):

    logging.info("Searching for Artist: " + artist + " Album: " + album + " Song: " + name + "\n")

    splitArtist = artist.split(", ")

    for i in splitArtist:
        artistToFind = i
        break

    dirList = os.listdir(pathToMusic)
    dirList.sort()


    logging.info("Searching for " + artistToFind + "\n")
    for i in dirList:
        x = len(artistToFind)
        while True:
            if not i.startswith(artistToFind[0:int(0.4*len(artistToFind))]):
                # logging.info("Not " + i)
                break
            logging.info("Searching in " + i)
            logging.info("Searching for " + artistToFind[0:x])
            if (i.startswith(artistToFind[0:x])):
                logging.info("Found artist " + i + "\n")

                albumDirs = os.listdir(pathToMusic + "/" + i)
                y = len(album)
                for j in albumDirs:

                    while True:
                        # if not j.startswith(album[0:int(0.1*len(album))]):
                        #     break
                        logging.info("Searching in " + j)
                        logging.info("Searching for " + album[0:y])
                        if (j.lower().startswith(album[0:y].lower())):
                            logging.info("Found album " + j + "\n\n")

                            songDir = os.listdir(pathToMusic + "/" + i + "/" + j)
                            z = 0
                            for k in songDir:

                                while True:

                                    logging.info("Searching in " + k)
                                    logging.info("Searching for " + name[z:len(name)])
                                    if os.path.isfile(pathToMusic + "/" + i + "/" + j + "/" + k):
                                        if (k.endswith(name[0:z])):
                                            logging.info("Found song " + pathToMusic + "/" + i + "/" + j + "/" + k)
                                            return (pathToMusic + "/" + i + "/" + j + "/" + k)
                                    else:
                                        cdDir = os.listdir(pathToMusic + "/" + i + "/" + j + "/" + k)
                                        for l in cdDir:

                                            while True:

                                                logging.info("Searching in " + l)
                                                logging.info("Searching for " + l)
                                                if l.startswith(name[z:len(name)]):
                                                    logging.info("Found song " + pathToMusic + "/" + i + "/" + j + "/" + k + "/" + l)
                                                    return (pathToMusic + "/" + i + "/" + j + "/" + k + "/" + l)

                                        z += 1
                                        if z > (0.5 * len(name)):
                                            break

                        y -= 1
                        if y < (0.15 * len(album)):
                            break
                        elif y < 1:
                            break

            x -= 1
            if x < (0.5 * len(artistToFind)) :
                break

    return None