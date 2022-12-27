import os
import logging
import subprocess


def musicCopy(musicLoc, musicMoveLoc):
    subprocess.Popen('sudo -s', shell=True, stdout=subprocess.PIPE)
    sentCheck = False
    if not os.path.exists(musicLoc):
        logging.info("Mounting laptop")
        output = subprocess.Popen("mount.cifs //ryan_urq_laptop/c/ /mnt/windows-share/ "
                                      "-o user=ryan_urq,pass=44Glenavna,ip=192.168.50.78",
                                      shell=True, stdout=subprocess.PIPE)
        logging.info(output.communicate()[0].decode("utf-8"))
    print("In background:\nChecking for laptop, then transferring music files")
    musicRAIDLoc = "/export/RAID/PlexMedia/Music/"
    if os.path.exists(musicLoc):
        print("Found laptop, checking for files to move now")
        logging.info("Moving to NAS")
        output = subprocess.Popen("rsync -rpEogvht --delete --update "
                                  "/mnt/windows-share/Users/ryan1/Music/Soggfy/ "
                                  "/export/NAS/Music/", shell=True, stdout=subprocess.PIPE)
        logging.info(output.communicate()[0].decode("utf-8"))
        print("Music dir up-to-date")
        sentCheck = True

    if os.path.exists(musicLoc):
        if os.path.exists(musicRAIDLoc):
            print("\n\nFound RAID")
            logging.info("Moving to RAID")
            output = subprocess.Popen("rsync -rpEogvht --delete --update "
                                          "/mnt/windows-share/Users/ryan1/Music/Soggfy/ /export/RAID/PlexMedia/Music/",
                                          shell=True, stdout=subprocess.PIPE)
            logging.info(output.communicate()[0].decode("utf-8"))
            print("\nRAID up-to-date")
            sentCheck = True

    if not os.path.exists(musicRAIDLoc):
        print("No RAID")

    if not sentCheck:
        print("No music moved")