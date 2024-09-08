import settings
import os
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


def test_selection(args):
    settings.init(args)
    import PlaylistParser
    PlaylistParser.selection(args)
    expectedList = os.listdir(settings.pathToPlaylistDownloads)
    expectedList.sort()
    for num, i in enumerate(settings.fileList, start=0):
        assert i == expectedList[num]

