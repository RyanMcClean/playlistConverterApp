import settings

def playlistFileCreation(playlist):
    if len(playlist) > 1:
        fileName = settings.convertedPlaylists + playlist[0].replace("txt", "m3u")
        fileName = fileName if len(fileName) < 143 else fileName[0:143]
        with open(fileName, "w", encoding="utf-8") as fp:
            for num, i in enumerate(playlist):
                if num == 0:
                    continue
                if i is not None:
                    fp.write(i + "\n")



