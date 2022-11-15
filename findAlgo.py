import os


def m4aFinder(artist, album, name, pathToMusic):
    # print("\nsearching for Artist: " + artist + " Album: " + album + " Song: " + name)
    # declare variables used in search function
    artistShort = artist
    artistCounter = 0
    albumShort = album
    albumCounter = 0
    nameShort = name
    nameCounter = 0
    # declare loop varaibles (these are used to shorten the strings of the path when searching)
    x = 0
    y = 0
    z = 0
    # Check to enable cutting the whole loop early if needed
    check = 1
    while check > 0:
        # Search for the artist name in the dir, if not found on first run through then
        # delete a character from the end of the string and try again
        if artistCounter > ((0.95) * len(artist)):
            print("Artist failure")
            check -= 1
            break
        if x > 0:
            artistShort = artist[:-x]
        x += 1
        artistCounter += 1
        print("artistShort = " + artistShort)
        for i in os.listdir(pathToMusic):
            while i.startswith(artistShort):
                print("Found artist " + i)
                # similar as above with the artist, but searching through the albums now
                if albumCounter > ((0.95) * len(album)):
                    print("Album failure")
                    check -= 1
                    break
                if y > 0:
                    albumShort = album[:- y]
                print("albumShort = " + albumShort)
                y += 1
                albumCounter += 1
                for j in os.listdir(pathToMusic + i + "/"):
                    while j.startswith(albumShort):
                        print("Found album " + j)
                        if nameCounter > ((0.95) * len(name)):
                            print("Name failure")
                            check -= 1
                            break
                        if z > 0:
                            nameShort = name[z:len(name)]
                        print("nameShort = " + nameShort)
                        z += 1
                        nameCounter += 1
                        for k in os.listdir(pathToMusic + i + "/" + j + "/"):
                            if os.path.isfile(pathToMusic + i + "/" + j + "/" + k):
                                if k.endswith(nameShort):
                                    stringToReturn = pathToMusic + i + "/" + j + "/" + k
                                    stringtoReturn = stringToReturn.replace(stringToReturn[:20], '', 1)
                                    return (stringtoReturn)
                            else:
                                for l in os.listdir(pathToMusic + i + "/" + j + "/" + k + "/"):
                                    if os.path.isfile(pathToMusic + i + "/" + j + "/" + k + "/" + l):
                                        if l.endswith(nameShort):
                                            stringToReturn = pathToMusic + i + "/" + j + "/" + k + "/" + l
                                            stringtoReturn = stringToReturn.replace(stringToReturn[:20], '', 1)
                                            return (stringtoReturn)
                        while check > 0:
                            # Search for the artist name in the dir, if not found on first run through then
                            # delete a character from the end of the string and try again
                            if artistCounter > ((0.95) * len(artist)):
                                print("Artist failure")
                                check -= 1
                                break
                            if x > 0:
                                artistShort = artist[:-x]
                            x += 1
                            artistCounter += 1
                            print("artistShort = " + artistShort)
                            for i in os.listdir(pathToMusic):
                                while i.startswith(artistShort):
                                    print("Found artist " + i)
                                    # similar as above with the artist, but searching through the albums now
                                    if albumCounter > ((0.95) * len(album)):
                                        print("Album failure")
                                        check -= 1
                                        break
                                    if y > 0:
                                        albumShort = album[:- y]
                                    print("albumShort = " + albumShort)
                                    y += 1
                                    albumCounter += 1
                                    for j in os.listdir(pathToMusic + i + "/"):
                                        while j.startswith(albumShort):
                                            print("Found album " + j)
                                            if nameCounter > ((0.95) * len(name)):
                                                print("Name failure")
                                                check -= 1
                                                break
                                            if z > 0:
                                                nameShort = name[z:len(name)]
                                            print("nameShort = " + nameShort)
                                            z += 1
                                            nameCounter += 1
                                            for k in os.listdir(pathToMusic + i + "/" + j + "/"):
                                                if os.path.isfile(pathToMusic + i + "/" + j + "/" + k):
                                                    if k.endswith(nameShort):
                                                        stringToReturn = pathToMusic + i + "/" + j + "/" + k
                                                        stringtoReturn = stringToReturn.replace(stringToReturn[:20], '',
                                                                                                1)
                                                        return (stringtoReturn)
                                                else:
                                                    for l in os.listdir(pathToMusic + i + "/" + j + "/" + k + "/"):
                                                        if os.path.isfile(
                                                                pathToMusic + i + "/" + j + "/" + k + "/" + l):
                                                            if l.endswith(nameShort):
                                                                stringToReturn = pathToMusic + i + "/" + j + "/" + k + "/" + l
                                                                stringtoReturn = stringToReturn.replace(
                                                                    stringToReturn[:20], '', 1)
                                                                return (stringtoReturn)

    x = 0
    y = 0
    z = 0
    while check == 0:
        # Search for the artist name in the dir, if not found on first run through then
        # delete a character from the end of the string and try again
        if artistCounter > ((0.95) * len(artist)):
            print("Artist failure")
            check -= 1
            break
        if x > 0:
            artistShort = artist[x:len(artist)]
        x += 1
        artistCounter += 1
        print("artistShort = " + artistShort)
        for i in os.listdir(pathToMusic):
            while i.endsswith(artistShort):
                print("Found artist " + i)
                # similar as above with the artist, but searching through the albums now
                if albumCounter > ((0.95) * len(album)):
                    print("Album failure")
                    check -= 1
                    break
                if y > 0:
                    albumShort = album[y:len(album)]
                print("albumShort = " + albumShort)
                y += 1
                albumCounter += 1
                for j in os.listdir(pathToMusic + i + "/"):
                    while j.startswith(albumShort):
                        print("Found album " + j)
                        if nameCounter > ((0.95) * len(name)):
                            print("Name failure")
                            check -= 1
                            break
                        if z > 0:
                            nameShort = name[z:len(name)]
                        print("nameShort = " + nameShort)
                        z += 1
                        nameCounter += 1
                        for k in os.listdir(pathToMusic + i + "/" + j + "/"):
                            if os.path.isfile(pathToMusic + i + "/" + j + "/" + k):
                                if k.endswith(nameShort):
                                    stringToReturn = pathToMusic + i + "/" + j + "/" + k
                                    stringtoReturn = stringToReturn.replace(stringToReturn[:20], '', 1)
                                    return (stringtoReturn)
                            else:
                                for l in os.listdir(pathToMusic + i + "/" + j + "/" + k + "/"):
                                    if os.path.isfile(pathToMusic + i + "/" + j + "/" + k + "/" + l):
                                        if l.endswith(nameShort):
                                            stringToReturn = pathToMusic + i + "/" + j + "/" + k + "/" + l
                                            stringtoReturn = stringToReturn.replace(stringToReturn[:20], '', 1)
                                            return (stringtoReturn)
                        # for root, dirs, files in os.walk(pathToMusic + i + "/" + j + "/"):
                        #     for file in files:
                        #         if file.endswith(nameShort):
                        #             # print(root + str(file))
                        #             if os.path.isfile(root + str(file)):
                        #                 stringToReturn = root + str(file)
                        #                 stringtoReturn = stringToReturn.replace(stringToReturn[:20], '', 1)
                        #                 return (stringtoReturn)

    # print("ERROR\nERROR\nERROR\n\n\n\n\n\n\n\n\n\n")
    # time.sleep (10)
    # print("None")
    return None
