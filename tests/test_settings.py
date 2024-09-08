import settings
import pytest

@pytest.fixture
def args():
    class args(object):
        pass
    args.a = True
    args.t = False
    args.q = False
    args.v = False
    args.select = 0
    return args

def testInit(args):
    settings.init(args)
    
    # test Path variables
    assert settings.pathToMusic is not None
    assert settings.pathToPlaylistDownloads is not None
    assert settings.convertedPlaylists is not None
    assert settings.nonLocalMusicPath is not None
    
    # test Spotify API variables
    assert settings.clientId is not None
    assert settings.clientSecret is not None
    assert settings.redirectURI is not None
    assert settings.scope is not None
    assert settings.cachePath is not None
    assert settings.sleepTime is not None
    
    # test Plex variables
    assert settings.plexBaseURL is not None
    assert settings.plexToken is not None
    
    # test App variables
    assert settings.fileList is not None
    assert settings.filesMissingPerPlaylist is not None
    assert settings.threaded is not None
    
    # test Logger setup
    assert settings.mainLog is not None
    assert settings.downloadLog is not None
