import json, os, logging



def setup_logger(name, log_file, level):
    """To setup as many loggers as you want"""
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    
    handler = logging.FileHandler(log_file, mode='w')        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

def init(appArgs):
    global pathToMusic, pathToPlaylistDownloads, convertedPlaylists, nonLocalMusicPath
    global clientId, clientSecret, redirectURI, scope, cachePath, sleepTime
    global plexBaseURL, plexToken
    global wd
    global mainLog, downloadLog
    global fileList, filesMissingPerPlaylist
    wd = os.getcwd()
    with open("./appSettings.json") as file:
        data = json.load(file)
        
        # Path variables
        pathConfig = data['pathConfig']
        pathToMusic = pathConfig['music']
        pathToPlaylistDownloads = pathConfig['downloadPlaylists']
        convertedPlaylists = pathConfig['convertPlaylists']
        nonLocalMusicPath = pathConfig['nonLocalMusic']
        
        # Spotify API Variables
        spotifyConfig = data['spotifyAPIConfig']
        clientId = spotifyConfig['clientId']
        clientSecret = spotifyConfig['clientSecret']
        redirectURI = spotifyConfig['redirectURI']
        scope = spotifyConfig['scope']
        cachePath = spotifyConfig['cachePath']
        sleepTime = spotifyConfig['sleepTime']
        
        # Plex variables
        plexConfig = data['plexConfig']
        plexBaseURL = plexConfig['baseURL']
        plexToken = plexConfig['token']
        
        # App variables
        fileList = []
        filesMissingPerPlaylist = {}
        
        if appArgs:
            mainLog = setup_logger("Main logger", "/home/ryan_urq/playlistCSVConverterApp/playlistConverterLog.log", logging.DEBUG)
            mainLog.debug("Logging set to debug\n\n")
            downloadLog = setup_logger("Downloader logger", "/home/ryan_urq/playlistCSVConverterApp/playlistDownloaderLog.log", logging.DEBUG)
            downloadLog.debug("Logging set to debug\n\n")
        else:
            mainLog = setup_logger("Main logger", "/home/ryan_urq/playlistCSVConverterApp/playlistConverterLog.log", logging.INFO)
            mainLog.info("Logging set to info\n\n")
            downloadLog = setup_logger("Downloader logger", "/home/ryan_urq/playlistCSVConverterApp/playlistDownloaderLog.log", logging.INFO)
            downloadLog.debug("Logging set to debug\n\n")
