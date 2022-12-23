import os
import logging
import subprocess


def musicCopy(musicLoc, musicMoveLoc):
    if not os.path.exists(musicLoc):
        logging.info("Mounting laptop")
        logging.info(subprocess.Popen("sudo mount.cifs //ryan_urq_laptop/c/ /mnt/windows-share/ -o user=ryan_urq, "
                                      "pass=44Glenavna,ip=192.168.50.78", shell=True, stdout=subprocess.PIPE).communicate()[0])
    print("In background:\nChecking for laptop, then transferring music files")
    musicRAIDLoc = "/export/RAID/PlexMedia/Music/"
    if os.path.exists(musicLoc):
        print("Found laptop, checking for files to move now")
        logging.info("Moving to NAS")
        logging.info(subprocess.Popen("sudo rsync -rpEogvht --delete --update "
                               "/mnt/windows-share/Users/ryan1/Music/Soggfy/ /export/NAS/Music/", shell=True, stdout=subprocess.PIPE).communicate()[0])

    if os.path.exists(musicRAIDLoc):
        print("\n\nFound RAID")
        logging.info("Moving to RAID")
        logging.info(subprocess.Popen("sudo rsync -rpEogvht --delete --update "
                                "/mnt/windows-share/Users/ryan1/Music/Soggfy/ /export/RAID/PlexMedia/Music/", shell=True, stdout=subprocess.PIPE).communicate()[0])

    if not os.path.exists(musicRAIDLoc):
        print("No RAID")
    print("Music dir up-to-date")
