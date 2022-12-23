import os
import logging

def m4aFinder(artist, album, name, pathToMusic):

    logging.info("\n Searching for Artist: " + artist + " Album: " + album + " Song: " + name)
    # sleep(2)
    # declare variables used in search function
    artistShort = artist
    artistCounter = 0
    albumShort = album
    albumCounter = 0
    nameShort = name
    nameCounter = 0
    # declare loop variables (these are used to shorten the strings of the path when searching)
    x = 0
    y = 0
    z = 0
    # Check to enable cutting the whole loop early if needed
    check = 1
    dirList = os.listdir(pathToMusic)
    dirList.sort()
    dirListCopy = dirList
    while check > 0:
        dirList = dirListCopy
        # Search for the artist name in the dir, if not found on first run through then
        # delete a character from the end of the string and try again
        if artistCounter > (0.95 * len(artist)):
            logging.info("Artist failure, cancelling search\n\n")
            return None
        if x > 0 and x < len(artist):
            artistShort = artist[:- x]
        x += 1
        artistCounter += 0.1
        logging.info("artistShort = " + artistShort)
        for num, i in enumerate(dirList):
            dirLower = i.lower()
            artistShort = artistShort.lower()
            if dirLower.startswith(artistShort):
                del dirListCopy[num]
            logging.info("Found artist " + i)
                # sleep(2)
            while dirLower.startswith(artistShort):
                # similar as above with the artist, but searching through the albums now
                if albumCounter > (0.95 * len(album)):
                    logging.info("Album failure\b")
                    break
                if y > 0:
                    albumShort = album[:- y]
                logging.info("albumShort = " + albumShort)
                y += 1
                albumCounter += 1
                for j, num in enumerate(os.listdir(pathToMusic + i + "/")):
                    dirLower = j.lower()
                    albumShort = albumShort.lower()
                    if dirLower.startswith(albumShort):
                        logging.info("Found album " + j)
                        # sleep(2)
                    while dirLower.startswith(albumShort):
                        if nameCounter > (0.95 * len(name)):
                            logging.info("Name failure\b")
                            break
                        if z > 0:
                            nameShort = name[z:len(name)]
                        # logging.info("nameShort = " + nameShort)
                        z += 1
                        nameCounter += 1
                        for k in os.listdir(pathToMusic + i + "/" + j + "/"):
                            if os.path.isfile(pathToMusic + i + "/" + j + "/" + k):
                                if k.endswith(nameShort):
                                    logging.info("Found song file")
                                    stringToReturn = "/Music/" + i + "/" + j + "/" + k
                                    return stringToReturn
                            else:
                                for l in os.listdir(pathToMusic + i + "/" + j + "/" + k + "/"):
                                    if os.path.isfile(pathToMusic + i + "/" + j + "/" + k + "/" + l):
                                        if l.endswith(nameShort):
                                            logging.info("Found song file")
                                            stringToReturn = "/Music/" + i + "/" + j + "/" + k + "/" + l
                                            return stringToReturn

