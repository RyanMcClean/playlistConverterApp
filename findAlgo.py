import os
import logging
from time import sleep

def m4aFinder(artist, album, name, pathToMusic):

    logging.info("\n Searching for Artist: " + artist + " Album: " + album + " Song: " + name)

    dirList = os.listdir(pathToMusic)
    dirList.sort()

    print(len(dirList))
    sleep(10)

    for i in dirList:
        if not i.startswith(artist[0:int(len(artist)*0.25)]):
            dirList.remove(i)
            print("removed " + i )

    print(len(dirList))
    sleep(10)

    for i in dirList:
        print("What's left " + i)

    print(artist)
    exit()