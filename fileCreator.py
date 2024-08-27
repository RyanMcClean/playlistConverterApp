def playlistFileCreation(playlistFinalPath, playlist):
    counter = 0
    with open(playlistFinalPath + playlist[0].replace("txt", "m3u8").replace("|", "-"), "w", encoding="utf-8") as fp:
        for num, i in enumerate(playlist):
            if num == 0:
                continue
            if i is not None:
                fp.write(i + "\n")
            if i is None:
                counter += 1

        return counter

