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
    for num, i in enumerate(dirList):
        if not i.startswith(artist[0:1]):
            del dirList[num]

    for i in dirList:
        x = len(artistToFind)
        while i is not None:
            if x < (0.55 * len(artistToFind)) :
                break
            if not i.startswith(artistToFind[0:int(0.5*len(artistToFind))]):
                # logging.info("Not " + i)
                break
            logging.info("Searching in " + i)
            logging.info("Searching for " + artistToFind[0:x])
            if (i.lower().startswith(artistToFind[0:x].lower())):
                logging.info("Found artist " + i + "\n")

                albumDirs = os.listdir(pathToMusic + "/" + i)
                logging.info(albumDirs)
                for j in albumDirs:
                    logging.info("next album is: " + j)
                    y = len(album)
                    while j is not None:
                        if y < (2):
                            albumDirs.remove(j)
                            break
                        logging.info("Searching through " + j)
                        if not j.lower().startswith(album[0:1].lower()):
                            logging.info("Ignoring album; " + j)
                            break
                        logging.info("Searching in " + j)
                        logging.info("Searching for " + album[0:y])

                        if (j.lower().startswith(album[0:y].lower())):
                            logging.info("Found album " + j + "\n\n")
                            songDir = os.listdir(pathToMusic + "/" + i + "/" + j)
                            for k in songDir:
                                z = 0
                                while k is not None:
                                    if z > (0.5 * len(name)):
                                        break
                                    logging.info("Searching in " + k)
                                    logging.info("Searching for " + name[z:len(name)])
                                    if os.path.isfile(pathToMusic + "/" + i + "/" + j + "/" + k):
                                        if (k.lower().endswith(name[z:len(name)].lower())):
                                            logging.info("Found song " + pathToMusic + "/" + i + "/" + j + "/" + k + "\n\n")
                                            return (pathToMusic + "/" + i + "/" + j + "/" + k)
                                    elif os.path.isdir(pathToMusic + "/" + i + "/" + j + "/" + k):
                                        cdDir = os.listdir(pathToMusic + "/" + i + "/" + j + "/" + k)
                                        for l in cdDir:
                                            a = 0
                                            while l is not None:
                                                if a > (0.5 * len(name)):
                                                    break

                                                logging.info("Searching in " +  k + "/" + l)
                                                logging.info("Searching for " + l)
                                                if l.lower().startswith(name[a:len(name)].lower()):
                                                    logging.info("Found song " + pathToMusic + "/" + i + "/" + j + "/" + k + "/" + l + "\n\n")
                                                    return (pathToMusic + "/" + i + "/" + j + "/" + k + "/" + l)

                                                a += 1

                                    z += 1

                        y -= 1



            x -= 1


    logging.info("\n\n\n None found \n\n\n")
    return None