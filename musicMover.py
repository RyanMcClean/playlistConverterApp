import os
import shutil
import time


def musicCopy(musicLoc, musicMoveLoc):
    if not os.path.exists(musicLoc):
        os.system("sudo mount.cifs //ryan_urq_laptop/c/ /mnt/windows-share/ -o user=ryan_urq,pass=44Glenavna,ip=192.168.50.78")
    print("In background:\nChecking for laptop, then transferring music files")
    musicRAIDLoc = "/export/RAID/PlexMedia/Music/"
    if os.path.exists(musicLoc):
        for artists in os.listdir(musicLoc):
            try:
                # try to move files, if directory exists then move on
                shutil.copytree(musicLoc + "/" + artists, musicMoveLoc + artists)
            except:
                for albums in os.listdir(musicLoc + "/" + artists):
                    try:
                        # try to move album, if dir exists move on
                        shutil.copytree(musicLoc + "/" + artists + "/" + albums,
                                              musicMoveLoc + artists + "/" + albums)
                    except:
                        for songs in os.listdir(musicLoc + "/" + artists + "/" + albums):
                            if os.path.isfile(musicLoc + "/" + artists + "/" + albums + "/" + songs):
                                try:
                                    # try to move songs (if they are files and not directories) if song exists move on
                                    shutil.copytree(musicLoc + "/" + artists + "/" + albums + "/" + songs,
                                                          musicMoveLoc + artists + "/" + albums + "/" + songs)
                                except:
                                    pass
                            else:
                                try:
                                    # if song was a directory then try to move it, if it exists then move on
                                    shutil.copytree(musicLoc + "/" + artists + "/" + albums + "/" + songs,
                                                          musicMoveLoc + artists + "/" + albums + "/" + songs)
                                except:
                                    for song in os.listdir(musicLoc + "/" + artists + "/" + albums + "/" + songs):
                                        try:
                                            # try to move the final files, if they already exist then give up
                                            shutil.copytree(
                                                musicLoc + "/" + artists + "/" + albums + "/" + songs + "/" + song,
                                                musicMoveLoc + artists + "/" + albums + "/" + songs + "/" + song)
                                        except:
                                            pass
    if os.path.exists(musicRAIDLoc):
        if os.path.exists(musicLoc):
            for artists in os.listdir(musicLoc):
                try:
                    # try to move files, if directory exists then move on
                    shutil.copytree(musicLoc + "/" + artists, musicRAIDLoc + artists)
                except:
                    for albums in os.listdir(musicLoc + "/" + artists):
                        try:
                            # try to move album, if dir exists move on
                            shutil.copytree(musicLoc + "/" + artists + "/" + albums,
                                                  musicRAIDLoc + artists + "/" + albums)
                        except:
                            for songs in os.listdir(musicLoc + "/" + artists + "/" + albums):
                                if os.path.isfile(musicLoc + "/" + artists + "/" + albums + "/" + songs):
                                    try:
                                        # try to move songs (if they are files and not directories) if song exists move on
                                        shutil.copytree(musicLoc + "/" + artists + "/" + albums + "/" + songs,
                                                              musicRAIDLoc + artists + "/" + albums + "/" + songs)
                                    except:
                                        pass
                                else:
                                    try:
                                        # if song was a directory then try to move it, if it exists then move on
                                        shutil.copytree(musicLoc + "/" + artists + "/" + albums + "/" + songs,
                                                              musicRAIDLoc + artists + "/" + albums + "/" + songs)
                                    except:
                                        for song in os.listdir(
                                                musicLoc + "/" + artists + "/" + albums + "/" + songs):
                                            try:
                                                # try to move the final files, if they already exist then give up
                                                shutil.copytree(
                                                    musicLoc + "/" + artists + "/" + albums + "/" + songs + "/" + song,
                                                    musicRAIDLoc + artists + "/" + albums + "/" + songs + "/" + song)
                                            except:
                                                pass
    if not os.path.exists(musicRAIDLoc):
        print("No RAID")
    print("Music dir up-to-date")
    time.sleep(1)
