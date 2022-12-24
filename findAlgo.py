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
        if x > 0 & x < len(artist):
            artistShort = artist[:- x]

        x += 1
        artistCounter += 1

        logging.info("artistShort = " + artistShort)

        for num, i in enumerate(artistList):
            dirLower = i.lower()
            artistShort = artistShort.lower()


            if dirLower.startswith(artistShort):
                del artistListCopy[num]
                logging.info("Found artist " + i)

            while dirLower.startswith(artistShort):


                # similar as above with the artist, but searching through the albums now
                if albumCounter > len(album) - 1:
                    logging.info("Album failure")
                    albumcounter = 0
                    albumShort = album
                    y = 0
                    artistCounter = 0
                    artistShort = artist
                    x = 0
                    break

                if y > 0 & y < len(album):
                    albumShort = album[:- y]

                logging.info("albumShort = " + albumShort)
                y += 1
                albumCounter += 1

                for j in os.listdir(pathToMusic + "/" + i + "/"):

                    if j.lower().startswith(albumShort.lower()):
                        logging.info("Found album " + j)
                        # sleep(2)
                    while j.lower().startswith(albumShort.lower()):
                        if nameCounter > (0.95 * len(name)):
                            logging.info("Name failure")
                            nameCounter = 0
                            nameShort = name
                            z = 0
                            albumcounter = 0
                            albumShort = album
                            y = 0
                            artistCounter = 0
                            artistShort = artist
                            x = 0
                            break
                        if z > 0 & z < len(name):
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

