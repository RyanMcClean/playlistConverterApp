import os
import settings

def m4aFinder(artist, album, name, artistDirs):
    logger = settings.mainLog
    pathToMusic = settings.pathToMusic
    prefix = ""
    logger.debug("Searching for Artist: " + artist + " Album: " + album + " Song: " + name + "\n")
    
    logger.debug("Searching for artist")
    check = len(pathToMusic)
    for i in artistDirs:        
        if matchStrings(i, artist, "artist"):
            logger.debug(f"Found artist \"%s\"", i)
            
            pathToMusic += i + "/"
            prefix += i + "/"
            logger.debug(pathToMusic)
            break
        
    if check < len(pathToMusic):
        check = len(pathToMusic)
    else:
        return None
    logger.debug("Searching for album")
    for j in os.listdir(pathToMusic):
        if matchStrings(j, album, "album"):
            logger.debug(f"Found album \"%s\"", j)
                
            pathToMusic += j + "/"
            prefix += j + "/"
            logger.debug(pathToMusic)
            break
    
    if check < len(pathToMusic):
        check = len(pathToMusic)
    else:
        return None
    logger.debug("Searching for song or CD")
    songOrCDPath = sorted(os.listdir(pathToMusic), key=len, reverse=True)
    for k in songOrCDPath:
        logger.debug(f"Checking %s%s", pathToMusic, k)
        if os.path.isfile(pathToMusic + "/" + k) and k.endswith(('.ogg','.m4a','.mp3')):
            logger.debug(f"Path to file: %s%s", pathToMusic, k)
            songCheck = k.split(".", 1)[1].rsplit('.', 1)[0]
            if matchStrings(songCheck, name, "song"):
                logger.debug(f"Found song \"%s/%s/%s\"", i, j, k)
                return prefix + k
                
        elif os.path.isdir(pathToMusic + "/" + k):
            logger.debug(f"Path to directory: %s%s", pathToMusic, k)

            logger.debug("Searching for song in CD")
            for l in os.listdir(pathToMusic + "/" + k):
                logger.debug(f"Checking {pathToMusic}/{k}/{l}")
                songCheck = l.split(".", 1)[1].rsplit('.', 1)[0]

                if matchStrings(songCheck, name, "song"):
                    logger.debug(f"Found song \"%s/%s/%s/%s\"", i, j, k, l)
                    return prefix + k + "/" + l

    return None    

def sanatiseInput(input):
    input = input.replace(" ", "")
    input = input.replace("：", ":")
    input = input.replace("／", "/")
    input = input.replace("．", ".")
    input = input.replace("？", "?")
    input = input.replace("＂", "\"")
    input = input.replace("￤", "|")
    input = input.replace("＊", "*")
    input = input.replace("＞", ">")
    input = input.replace("＜", "<")
    return input

def matchStrings(input, matchAgainst, type):
    logger = settings.mainLog
    input1 = sanatiseInput(input).lower()
    input2 = sanatiseInput(matchAgainst).lower()
    ans = False
    if len(input1) > 0 and len(input2) > 0 and not input1[0] == input2[0]:
        if type == "album":
            logger.debug(f"\"%s\" does not match: \"%s\"", input, matchAgainst)
            logger.debug(f"\"%s\" does not match: \"%s\"", input1, input2)
        pass
    elif input2 == input1:
        logger.debug(f"\"%s\" matches \"%s\"\n\n", input, matchAgainst)
        ans = True
    else:
        logger.debug(f"\"%s\" does not match: \"%s\"", input, matchAgainst)
        logger.debug(f"\"%s\" does not match: \"%s\"", input1, input2)
    return ans
