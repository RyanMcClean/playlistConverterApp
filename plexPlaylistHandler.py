from plexapi.server import PlexServer
from plexapi.playlist import Playlist
import os
import settings
from time import sleep

if settings.globalArgs.q:
    from settings import messageQuiet as message
else:
    from settings import messageLoud as message

logger = settings.mainLog


def main():
    global plex
    playlistList = os.listdir(settings.convertedPlaylists)
    playlistList = [ playlist for playlist in playlistList if ".m3u" in playlist]
    playlistList.sort()
    currentPlaylists = plex.playlists(playlistType='audio', sectionId=3)

    for num, i in enumerate(playlistList):
        for j in currentPlaylists:
         if i == j.title:
            toDelete = plex.playlist(title=j.title)
            logger.info(f"Deleting playlist {j.title} off of Plex")
            toDelete.delete()
        message(f"{int((num/len(playlistList))*100)}%", 'percentage')
        try:
            Playlist.create(server=plex, title=i[:-4], section='Music', m3ufilepath=settings.convertedPlaylists + i)
        except Exception:
            pass
        sleep(5)

def updateMusic():
    try:
        global plex
        plex = PlexServer(settings.plexBaseURL, settings.plexToken, timeout=60)
        musicSection = plex.library.sectionByID(3)
        musicSection.update()
    except Exception as e:
        logger.error(e)
        message(e, 'error')
