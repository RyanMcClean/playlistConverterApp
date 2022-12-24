import os
import logging

def m4aFinder(artist, album, name, pathToMusic):

    logging.info("\n Searching for Artist: " + artist + " Album: " + album + " Song: " + name)

    dirList = os.listdir(pathToMusic)
    dirList.sort()

    for i in dirList:
        if not i.startswith(artist[1:len(artist)]):
            dirList.remove(i)
            print("removed" + i )
