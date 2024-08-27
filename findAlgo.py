import os
import logging

def m4aFinder(artist, album, name, artistDirs, pathToMusic):
    
    prefix = "\\\\Omv\\nas\\Music\\"

    logging.debug("Searching for Artist: " + artist + " Album: " + album + " Song: " + name + "\n")
    
    artist = artist.split(",", 1)[0]
    logging.debug("Searching for artist")
    check = len(pathToMusic)
    for i in artistDirs:        
        if matchStrings(i, artist):
            logging.debug(f"Found artist \"%s\"", i)
            
            pathToMusic += i + "/"
            prefix += i + "\\"
            logging.debug(pathToMusic)
            break
        
    if check < len(pathToMusic):
        check = len(pathToMusic)
    else:
        return None
    logging.debug("Searching for album")
    for j in os.listdir(pathToMusic):
        if matchStrings(j, album):
            logging.debug(f"Found album \"%s\"", j)
                
            pathToMusic += j + "/"
            prefix += j + "\\"
            logging.debug(pathToMusic)
            break
    
    if check < len(pathToMusic):
        check = len(pathToMusic)
    else:
        return None
    logging.debug("Searching for song or CD")
    for k in os.listdir(pathToMusic):
        logging.debug(f"Checking %s%s", pathToMusic, k)
        if os.path.isfile(pathToMusic + "/" + k) and k.endswith(('.ogg','.m4a','.mp3')):
            logging.debug(f"Path to file: %s%s", pathToMusic, k)
            songCheck = k.split(".", 1)[1].rsplit('.', 1)[0]
            if matchStrings(songCheck, name):
                logging.debug(f"Found song \"%s/%s/%s\"", i, j, k)
                return prefix + k
                
        elif os.path.isdir(pathToMusic + "/" + k):
            logging.debug(f"Path to directory: %s%s", pathToMusic, k)
            pathToMusic += k + "/"
            prefix += k + "\\"
            logging.debug(pathToMusic)
            break

    if check < len(pathToMusic):
        check = len(pathToMusic)
    else:
        return None
    logging.debug("Searching for song")
    for l in os.listdir(pathToMusic):
        logging.debug(f"Checking %s/%s", pathToMusic, l)
        songCheck = l.split(".", 1)[1].rsplit('.', 1)[0]

        if matchStrings(songCheck, name):
            logging.debug(f"Found song \"%s/%s/%s/%s\"", i, j, k, l)
            return prefix + l
    
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

def matchStrings(input, matchAgainst):
    input1 = sanatiseInput(input).lower()
    input2 = sanatiseInput(matchAgainst).lower()
    ans = False
    if len(input1) > 0 and len(input2) > 0 and not input1[0] is input2[0]:
        pass
    elif input2 == input1:
        logging.debug(f"\"%s\" matches \"%s\"\n\n", input, matchAgainst)
        ans = True
    # elif input2 in input1:
    #     logging.debug(f"\"%s\" matches \"%s\"\n\n", input, matchAgainst)
    #     ans = True
    else:
        logging.debug(f"\"%s\" does not match: \"%s\"", input, matchAgainst)
        logging.debug(f"\"%s\" does not match: \"%s\"", input1, input2)
    return ans
