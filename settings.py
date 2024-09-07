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
    global wd, globalArgs
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
        
        # App arguments
        globalArgs = appArgs

        if globalArgs.v:
            mainLog = setup_logger("Main logger", "./playlistConverterLog.log", logging.DEBUG)
            mainLog.debug("Logging set to debug\n\n")
            downloadLog = setup_logger("Downloader logger", "./playlistDownloaderLog.log", logging.DEBUG)
            downloadLog.debug("Logging set to debug\n\n")
        else:
            mainLog = setup_logger("Main logger", "./playlistConverterLog.log", logging.INFO)
            mainLog.info("Logging set to info\n\n")
            downloadLog = setup_logger("Downloader logger", "./playlistDownloaderLog.log", logging.INFO)
            downloadLog.debug("Logging set to debug\n\n")

class color:
    PURPLE = '\033[1;35;48m'
    CYAN = '\033[1;36;48m'
    BOLD = '\033[1;37;48m'
    BLUE = '\033[1;34;48m'
    GREEN = '\033[1;32;48m'
    YELLOW = '\033[1;33;48m'
    RED = '\033[1;31;48m'
    BLACK = '\033[1;30;48m'
    UNDERLINE = '\033[4;37;48m'
    END = '\033[1;37;0m'



def messageLoud(text, type='text'):
    if type == 'text':
        print(text)
    elif type == 'percentage':
        print(text, end='\r')
    elif type == 'error':
        print(color.RED + text + color.END)

def messageQuiet(text, type=None):
    pass