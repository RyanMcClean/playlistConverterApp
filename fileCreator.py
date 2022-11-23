import time

def playlistFileCreation(playlistFinalPath, playlist):
    counter = 0
    with open(playlistFinalPath + playlist[0].replace("csv", "m3u8"), "w", encoding="utf-8") as fp:
        for num, i in enumerate(playlist):
            if num == 0:
                continue
            if i is not None:
                fp.write(i + "\n")
            if i is None:
                counter += 1
        print(playlist[0] + " Converted to " + playlist[0].replace("csv", "m3u8") + " missing " + str(counter) +
              " songs from file system.\n\n")
        time.sleep(2)
        return counter

