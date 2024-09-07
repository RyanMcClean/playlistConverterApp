import settings

def testInit():
    settings.init()
    assert settings.cachePath is not None
    assert settings.clientId is not None
    assert settings.clientSecret is not None
    assert settings.convertedPlaylists is not None
    assert settings.downloadLog is not None
    assert settings.fileList is not None
    assert settings.filesMissingPerPlaylist is not None
    assert settings.globalArgs is None
    assert settings.mainLog is not None
    assert settings.nonLocalMusicPath is not None
    assert settings.pathToMusic is not None
    assert settings.pathToPlaylistDownloads is not None
    assert settings.scope is not None
