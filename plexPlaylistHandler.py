from plexapi.server import PlexServer
from plexapi.playlist import Playlist
import os
import settings

if settings.globalArgs.q:
    from settings import messageQuiet as message
else:
    from settings import messageLoud as message
    
def main():
    global plex
    logger = settings.mainLog
    playlistList = os.listdir(settings.convertedPlaylists)
    playlistList.sort()
    currentPlaylists = plex.playlists(playlistType='audio', sectionId=3)

    for num, i in enumerate(playlistList):
        for j in currentPlaylists:
         if i == j.title:
            toDelete = plex.playlist(title=j.title)
            logger.info(f"Deleting playlist {j.title} off of Plex")
            toDelete.delete()
        message(f"{int((num/len(playlistList))*100)}%", 'percentage')
        Playlist.create(server=plex, title=i[:-4], section='Music',m3ufilepath=settings.convertedPlaylists + i)

def updateMusic():
    global plex
    plex = PlexServer(settings.plexBaseURL, settings.plexToken)
    musicSection = plex.library.sectionByID(3)
    musicSection.update()

