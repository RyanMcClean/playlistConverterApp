import spotipy
import pytest
import settings

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

@pytest.fixture
def expected():
    userName = 'Ryan Urquhart'
    return userName

def test_spotify_connection(args, expected):
    settings.init(args)
    spOauth = spotipy.SpotifyOAuth(client_id=settings.clientId, client_secret=settings.clientSecret, scope=settings.scope, cache_path=settings.cachePath, redirect_uri=settings.redirectURI)
    accessToken = spOauth.get_access_token(as_dict=False)

    sp = spotipy.Spotify(accessToken, requests_timeout=10, retries=0)
    assert sp.current_user()['display_name'] == expected
