from plexapi.server import PlexServer
from plexapi.playlist import Playlist
import os
import settings

def main():
    global plex
    logger = settings.mainLog
    plex = PlexServer(settings.plexBaseURL, settings.plexToken)
    playlistList = os.listdir(settings.convertedPlaylists)
    playlistList.sort()
    currentPlaylists = plex.playlists(playlistType='audio', sectionId=3)

    for num, i in enumerate(playlistList):
        for j in currentPlaylists:
         if i == j.title:
            toDelete = plex.playlist(title=j.title)
            logger.info(f"Deleting playlist {j.title} off of Plex")
            toDelete.delete()
        print(f"{int((num/len(playlistList))*100)}%", end="\r")
        Playlist.create(server=plex, title=i[:-4], section='Music',m3ufilepath=settings.convertedPlaylists + i)

def updateMusic():
    musicSection = plex.library.sectionByID(3)
    musicSection.update()


if __name__ == "__main__":
    main()
    
