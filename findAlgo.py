import os
import logging

def m4aFinder(artist, album, name, pathToMusic):

    logging.info("\n Searching for Artist: " + artist + " Album: " + album + " Song: " + name)
    # sleep(2)
    # declare variables used in search function
    artistShort = artist
    artistCounter = 0

    # declare loop variables (these are used to shorten the strings of the path when searching)
    x = 0
    y = 0
    z = 0
    # Check to enable cutting the whole loop early if needed
    check = True
    artistList = os.listdir(pathToMusic)
    artistList.sort()
    artistListCopy = artistList


    while check:

        artistList = artistListCopy

        # Search for the artist name in the dir, if not found on first run through then
        # delete a character from the end of the string and try again
        if artistCounter > (0.95 * len(artist)):
            logging.info("Artist failure, cancelling search")
            return None
        if x > 0:
            artistShort = artist[0:- x]

        x += 1
        artistCounter += 1

        logging.info("artistShort = " + artistShort)

        for num, i in enumerate(artistList):
            dirLower = i.lower()
            artistShort = artistShort.lower()

            # if not i.startswith(artist[1:]):
            #     del artistListCopy[num]
            #     break
            if dirLower.startswith(artistShort):
                del artistListCopy[num]
                logging.info("Found artist " + i)

            albumCounter = (0.95 * len(artist))
            albumShort = album
            y = 0
            while dirLower.startswith(artistShort):


                # similar as above with the artist, but searching through the albums now
                if albumCounter > (0.95 * len(album)) :
                    logging.info("Album failure")
                    artistCounter = (0.1 * len(artist))
                    artistShort = artist
                    x = 0
                    break

                if y > 0:
                    albumShort = album[0:- y]

                logging.info("albumShort = " + albumShort)
                y += 1
                albumCounter += 1

                for j in os.listdir(pathToMusic + "/" + i + "/"):

                    if j.startswith(albumShort):
                        logging.info("Found album " + j)
                        # sleep(2)

                    nameCounter = 0
                    nameShort = name
                    z = 0
                    while j.lower().startswith(albumShort.lower()):
                        if nameCounter > (0.95 * len(name)):
                            logging.info("Name failure")
                            artistCounter = 0
                            artistShort = artist
                            x = 0
                            break
                        if z > 0 & z < len(name) - 2:
                            nameShort = name[z:len(name)]
                        # logging.info("nameShort = " + nameShort)
                        z += 1
                        nameCounter += 1
                        for k in os.listdir(pathToMusic + i + "/" + j + "/"):


                            if os.path.isfile(pathToMusic + i + "/" + j + "/" + k):
                                if k.endswith(nameShort):
                                    logging.info("Found song file " + k)
                                    stringToReturn = "/Music/" + i + "/" + j + "/" + k
                                    return stringToReturn
                            else:
                                for l in os.listdir(pathToMusic + i + "/" + j + "/" + k + "/"):
                                    if os.path.isfile(pathToMusic + i + "/" + j + "/" + k + "/" + l):
                                        if l.endswith(nameShort):
                                            logging.info("Found song file " + k + "/" + l)
                                            stringToReturn = "/Music/" + i + "/" + j + "/" + k + "/" + l
                                            return stringToReturn

