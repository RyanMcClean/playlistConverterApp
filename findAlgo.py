import os
import logging
from time import sleep

def m4aFinder(artist, album, name, pathToMusic):

    logging.info("Searching for Artist: " + artist + " Album: " + album + " Song: " + name + "\n")

    dirList = os.listdir(pathToMusic)
    dirList.sort()

    print(len(dirList))
    sleep(10)

    for num, i in enumerate(dirList):
        if (i[0] != artist[0]):
            del dirList[num]
            print("removed " + i )
        elif (i[0:2] != artist[0:2]):
            del dirList[num]
            print("removed " + i )
        elif (i.startswith(artist[0])):
            del dirList[num]
            print("removed " + i )

    print(len(dirList))
    sleep(10)

    for i in dirList:
        print("What's left " + i)

    print(artist)
    exit()