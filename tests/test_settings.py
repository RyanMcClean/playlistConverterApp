import settings

def testInit():
    settings.init()
    assert settings.cachePath is not None