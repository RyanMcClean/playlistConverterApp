import os
import logging
from time import sleep

def m4aFinder(artist, album, name, pathToMusic):

    logging.info("\n Searching for Artist: " + artist + " Album: " + album + " Song: " + name)

    dirList = os.listdir(pathToMusic)
    dirList.sort()

    print(artist[1:len(artist)])
    sleep(10)

    for i in dirList:
        if not i.startswith(artist[0:len(artist)]):
            dirList.remove(i)
            print("removed " + i )

    for i in dirList:
        print("What's left " + i)