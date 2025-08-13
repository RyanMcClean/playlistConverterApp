import spotipy
import os
from time import sleep, time
import helpers.settings as settings

if settings.globalArgs.q or settings.threaded:
    from helpers.settings import message_quiet as message
else:
    from helpers.settings import message_loud as message

logger = settings.downloadLog

def main():
    global sp, spOauth, accessToken, currentTime
    logger.debug("Starting download of playlists via Spotify API")
    try:
        spOauth = spotipy.SpotifyOAuth(client_id=settings.clientId, client_secret=settings.clientSecret, scope=settings.scope, cache_path=settings.cachePath, redirect_uri=settings.redirectURI)
        accessToken = spOauth.get_access_token(as_dict=False)

        sp = spotipy.Spotify(accessToken, requests_timeout=10, retries=0)
        currentTime = int(time())
        logger.info(f"Logged into Spotify as: {sp.current_user()['display_name']}")
        getLikedSongs()
        sleep(settings.sleepTime)
        getAllPlaylists()
        logger.info("Finished downloading playlists")
    except Exception as e:
        logger.error(e)
        message(e, 'error')

    

def getAllPlaylists():
    logger.debug('Checking all users playlists')
    playlists = []
    try:
        playlists = sp.current_user_playlists()
    except Exception as e:
        logger.error(e)
        message(e, 'error')
    if os.path.exists(settings.pathToPlaylistDownloads):
        pass
    else:
        os.makedirs(settings.pathToPlaylistDownloads)
    playlistList = os.listdir(settings.pathToPlaylistDownloads)
    modifier = 0
    totalPlaylists = playlists['total']
    message("Downloading playlists from Spotify")
    if not playlists is None:
        while playlists:
            for i, playlist in enumerate(playlists['items'], start=1):
                message(f"Playlists Downloading: {int(((i + modifier)/totalPlaylists)*100)}%", 'percentage')
                if playlist['tracks']['total'] > 0:
                    logger.debug(f"{i + modifier} - {playlist['uri']} - {playlist['name']} - {playlist['snapshot_id']} - Total tracks: {playlist['tracks']['total']}")
                    playlistName = playlist['name']
                    for i in ["/", ".", "\\", "<", ">", "?", "_", ":", "|"]:
                        playlistName = playlistName.replace(i, "")
                    playlistName = playlistName.strip() if len(playlistName) + len(settings.pathToPlaylistDownloads) < 143 else playlistName[0:(143 - len(settings.pathToPlaylistDownloads))].strip()
                    if playlistName + ".txt" in playlistList:
                        with open(settings.pathToPlaylistDownloads + playlistName + ".txt") as fp:
                            logger.debug(f"{playlist['name']} file opened")
                            for line in fp:
                                if line.startswith("snapshot-"):
                                    logger.debug(f"Found snapshot in file: {fp.name}")
                                    if not line[:-1] == f"snapshot-{playlist['snapshot_id']}":
                                        logger.debug(f"Snapshots did not match: Found {line[:-1]} compared to snapshot-{playlist['snapshot_id']}")
                                        fp.close()
                                        os.remove(fp.name)
                                        logger.debug(f"Deleting file: {fp.name}")
                                        getSongsOfPlaylist(playlist['uri'], playlistName, playlist['snapshot_id'])
                                        break 
                                    else:
                                        logger.debug("Snapshots matched")
                                    break
                                elif line is None:
                                    logger.debug(f"File {fp.name} does not contain snapshot ID, deleting file")
                                    fp.close()
                                    os.remove(fp.name)  
                                    getSongsOfPlaylist(playlist['uri'], playlistName, playlist['snapshot_id'])
                                    break
                    else:
                        logger.debug(f"File for {playlist['name']} did not exist")
                        getSongsOfPlaylist(playlist['uri'], playlistName, playlist['snapshot_id'])
            if playlists['next']:
                try:
                    sleep(settings.sleepTime)
                    playlists = sp.next(playlists)
                except Exception as e:
                    if spOauth.is_token_expired(spOauth.get_cached_token()):
                        refreshSpotify(sp, spOauth, accessToken)
                        playlists = sp.next(playlists)
                    else:
                        logger.error(e)
                        message(e, 'error')
                modifier += 50
            else:
                playlists = None

def getLikedSongs():
    logger.debug("Checking Liked Songs")
    if not os.path.exists(settings.pathToPlaylistDownloads + sp.current_user()['display_name'] + 
                          " Liked Songs" + ".txt") or (currentTime - int(os.path.getmtime(settings.pathToPlaylistDownloads + sp.current_user()['display_name'] + 
                                                                                          " Liked Songs" + ".txt"))) > 3600 * 48:
        likedSongs = sp.current_user_saved_tracks()    
        count = 1
        toFile = [sp.current_user()['display_name'] + ' Liked Songs']
        while likedSongs:
            for track in likedSongs['items']:
                try:
                    if track['track'] is None:
                        continue
                    toAppend = str(count) + ",," 
                    if track['track'] is None or 'is_local' in track.keys() and track['track']['is_local']:
                        continue
                    if 'restrictions' in track['track'].keys(): 
                        logger.error(track)
                        toAppend += 'restricted' + ",,"
                    if track['track']['type'] == 'episode':
                        toAppend += "Podcast" + ",,"
                        if 'show' in track['track'].keys():
                            toAppend += track['track']['show']['name'] + ",,"
                        else:
                            toAppend += track['track']['album']['name'] + ",,"
                        toAppend +=  track['track']['name'] 
                    elif track['track']['type'] == "track":
                        for i in track['track']['artists']:
                            if len(i['name']) > 0 and not "Various Artists" in i['name']:
                                toAppend += f"{i['name']}"
                                break
                        toAppend += ",," + track['track']['album']['name']
                        toAppend += ",," + track['track']['name']
                    if toFile:
                        toFile.append(toAppend)
                        count += 1
                    if "Various Artists" in toAppend:
                        logger.error(track)
                        exit(1)
                except Exception as e:
                    import traceback;
                    logger.error(e)
                    logger.error(traceback.format_exc())
                    logger.error("Error on adding this track to list")
                    logger.error(track)
                    exit(1)
            if likedSongs['next']:
                try:
                    sleep(settings.sleepTime)
                    likedSongs = sp.next(likedSongs)
                except Exception as e:
                    if spOauth.is_token_expired(spOauth.get_cached_token()):
                        refreshSpotify(sp, spOauth, accessToken)
                        likedSongs = sp.next(likedSongs)
                    else:
                        logger.error(e)
                        message(e, 'error')
            else:
                likedSongs = None
        makeFile(toFile)    
    else:
        logger.debug("Liked songs file is too young to update")
    
def makeFile(fileContents):
    if os.path.exists(settings.pathToPlaylistDownloads):
        pass
    else:
        os.makedirs(settings.pathToPlaylistDownloads)
    if len(fileContents) > 2:
        logger.debug(f"Making file: {fileContents[0]}.txt")
        fp = open(settings.pathToPlaylistDownloads + fileContents[0] + ".txt", 'w')
        for i in fileContents:
            fp.write(i)
            fp.write("\n")
        fp.close()
        sleep(settings.sleepTime)
    else:
        logger.error(f"Not creating a null file of: {fileContents[0]}.txt")
    

def getSongsOfPlaylist(playlistID, playlistName, playlistSnapshotId):
    try:
        playlistSongs = sp.playlist_items(playlistID, market="IE")
        count = 1
        toFile = [playlistName, f"snapshot-{playlistSnapshotId}"]
        while playlistSongs:
            for track in playlistSongs['items']:
                try:
                    toAppend = str(count) + ",,"
                    if track['track'] is None:
                            continue
                    if 'is_local' in track['track'].keys():
                        if track['track']['is_local']:
                            continue
                    if 'restrictions' in track['track'].keys(): 
                        logger.error(track)
                        toAppend += 'restricted' + ",,"
                    if track['track']['type'] == 'episode':
                        toAppend += "Podcast" + ",," if (len(toAppend) > 0) else str(count) + ",," + "Podcast" + ",,"
                        if 'show' in track['track'].keys():
                            toAppend += track['track']['show']['name'] + ",,"
                        else:
                            toAppend += track['track']['album']['name'] + ",,"
                        toAppend +=  track['track']['name'] 
                    elif track['track']['type'] == "track":
                        for i in track['track']['artists']:
                            if len(i['name']) > 0 and not "Various Artists" in i['name']:
                                toAppend += f"{i['name']}"
                                break
                        toAppend += ",," + track['track']['album']['name']
                        toAppend += ",," + track['track']['name']
                    if toFile:
                        toFile.append(toAppend)
                        count += 1
                    if "Various Artists" in toAppend:
                        logger.error(track)
                        exit(1)
                except Exception as e:
                    import traceback;
                    logger.error(e)
                    logger.error(traceback.format_exc())
                    logger.error("Error on adding this track to list")
                    logger.error(track)

            if playlistSongs['next']:
                try:
                    sleep(settings.sleepTime)
                    playlistSongs = sp.next(playlistSongs)
                except Exception as e:
                    if spOauth.is_token_expired(spOauth.get_cached_token()):
                        refreshSpotify(sp, spOauth, accessToken)
                        playlistSongs = sp.next(playlistSongs)
                    else:
                        logger.error(e)
                        message(e, 'error')
            else:
                playlistSongs = None
        makeFile(toFile) 
    except Exception as e:
        logger.error(e)
        
def refreshSpotify():
    spOauth = spotipy.SpotifyOAuth(client_id=settings.clientId, client_secret=settings.clientSecret, scope=settings.scope, cache_path=settings.cachePath, redirect_uri=settings.redirectURI)
    accessToken = spOauth.get_access_token(as_dict=False)
    sp = spotipy.Spotify(accessToken, requests_timeout=10)

if __name__ == "__main__":
    main()
