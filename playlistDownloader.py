import spotipy
import os
from time import sleep, time
import logging

wd = "/home/ryan_urq/playlistCSVConverterApp/RyansPlaylists/"
clientId = "9f4eff74a2b642bf9cd72e7d32703774"
clientSecret = "162dba3c134e4919bc992241618ccf0a"
redirectURI = "https://spotify.com"
scope = "user-library-read playlist-read-private playlist-read-collaborative"
cachePath = "/home/ryan_urq/playlistCSVConverterApp/.cache"
sleepTime = 5
    
def main():
    logging.debug("Starting download of playlists via Spotify API")
    spOauth = spotipy.SpotifyOAuth(client_id=clientId, client_secret=clientSecret, scope=scope, cache_path=cachePath, redirect_uri=redirectURI)
    accessToken = spOauth.get_access_token(as_dict=False)
    global sp, currentTime

    sp = spotipy.Spotify(accessToken, requests_timeout=20)
    currentTime = int(time())
    logging.info(f"Logged into Spotify as: {sp.current_user()['display_name']}")
    getLikedSongs()
    sleep(sleepTime)
    getAllPlaylists()

def getAllPlaylists():
    logging.debug('Checking all users playlists')
    playlists = sp.current_user_playlists()
    playlistList = os.listdir(wd)
    modifier = 0
    while playlists:
        for i, playlist in enumerate(playlists['items']):
            logging.debug(f"{i + 1 + modifier} - {playlist['uri']} - {playlist['name']} - {playlist['snapshot_id']}")
            playlistName = playlist['name'].replace("/"," ").replace(".", "").strip()
            if playlistName + ".txt" in playlistList:
                with open(wd + playlistName + ".txt") as fp:
                    logging.debug(f"{playlist['name']} file opened")
                    for line in fp:
                        if line.startswith("snapshot-"):
                            logging.debug(f"Found snapshot in file: {fp.name}")
                            if not line[:-1] == f"snapshot-{playlist['snapshot_id']}":
                                logging.debug(f"Snapshots did not match: Found {line[:-1]} compared to snapshot-{playlist['snapshot_id']}")
                                fp.close()
                                os.remove(fp.name)
                                logging.debug(f"Deleting file: {fp.name}")
                                getSongsOfPlaylist(playlist['uri'], playlistName, playlist['snapshot_id'])
                                break 
                            else:
                                logging.debug("Snapshots matched")
                            break
                        elif line is None:
                            logging.debug(f"File {fp.name} does not contain snapshot ID, deleting file")
                            fp.close()
                            os.remove(fp.name)  
                            getSongsOfPlaylist(playlist['uri'], playlistName, playlist['snapshot_id'])
                            break
            else:
                logging.debug(f"File for {playlist['name']} did not exist")
                getSongsOfPlaylist(playlist['uri'], playlistName, playlist['snapshot_id'])
        if playlists['next']:
            playlists = sp.next(playlists)
            modifier += 50
        else:
            playlists = None

def getLikedSongs():
    logging.debug("Checking Liked Songs")
    if not os.path.exists(wd + "Liked Songs" + ".txt") or (currentTime - int(os.path.getmtime(wd + "Liked Songs" + ".txt"))) > 3600 * 48:
        likedSongs = sp.current_user_saved_tracks()    
        count = 1
        toFile = ['Liked Songs']
        while likedSongs:
            for track in likedSongs['items']:
                toFile.append(str(count) + ",," + track['track']['name'] + ",," + track['track']['album']['artists'][0]['name'] + ",," + track['track']['album']['name'])
                count += 1
            if likedSongs['next']:
                sleep(sleepTime)
                likedSongs = sp.next(likedSongs)
            else:
                likedSongs = None
        makeFile(toFile)    
    
def makeFile(fileContents):
    logging.debug(f"Making file: {fileContents[0]}.txt")
    fp = open(wd + fileContents[0] + ".txt", 'w')
    for i in fileContents:
        fp.write(i)
        fp.write("\n")
    fp.close()
    sleep(sleepTime)
    

def getSongsOfPlaylist(playlistID, playlistName, playlistSnapshotId):
    playlistSongs = sp.playlist_items(playlistID)
    count = 1
    toFile = [playlistName, f"snapshot-{playlistSnapshotId}"]
    while playlistSongs:
        for track in playlistSongs['items']:
            try:
                if track['track'] is None:
                    continue
                elif track['track']['type'] == 'episode':
                    toAppend = str(count) + ",," + "Podcast" + ",,"
                    if 'show' in track['track'].keys():
                        toAppend += track['track']['show']['name'] + ",,"
                    else:
                        toAppend += track['track']['album']['name'] + ",,"
                    toAppend +=  track['track']['name'] 
                elif track['track']['type'] == "track":
                    toAppend = str(count) + ",,"
                    if len(track['track']['album']['artists']) > 0:
                        toAppend += track['track']['album']['artists'][0]['name']
                    else:
                        toAppend += track['track']['artists'][0]['name']
                    toAppend += ",," + track['track']['album']['name']
                    toAppend += ",," + track['track']['name']
                if toFile:
                    toFile.append(toAppend)
                    count += 1
                # if "Various Artists" in toFile:
                #     logging.error(track)
                #     exit(1)
            except Exception as e:
                import traceback;
                logging.error(e)
                logging.error(traceback.format_exc())
                logging.error("Error on adding this track to list")
                logging.error(track)
                exit(1)

        if playlistSongs['next']:
            sleep(sleepTime)
            playlistSongs = sp.next(playlistSongs)
        else:
            playlistSongs = None
    makeFile(toFile)    
            

if __name__ == "__main__":
    main()
