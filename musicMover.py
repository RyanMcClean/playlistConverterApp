import os
import logging
import subprocess


def musicCopy(musicLoc, musicMoveLoc):
    # subprocess.Popen('sudo -s', shell=True, stdout=subprocess.PIPE)
    sentCheck = False
    if not os.path.exists(musicLoc):
        logging.info("Mounting laptop")
        output = subprocess.Popen("sudo mount.cifs //ryan_urq_laptop/c/ /mnt/windows-share/ "
                                      "-o user=ryan1328@hotmail.com,pass=A9450CBBAA9EF6E8666B66FCFDCA145A084ADC00F1B1FE2C7EB8E63625640157,ip=192.168.50.150 >/dev/null 2>&1",
                                      shell=True, stdout=subprocess.PIPE)
        logging.info(output.communicate()[0].decode("utf-8"))
    print("In background:\nChecking for laptop, then transferring music files")
    musicRAIDLoc = "/export/RAID1/Music/"
    if os.path.exists(musicLoc):
        print("Found laptop, checking for files to move now")
        logging.info("Moving to NAS")
        output = subprocess.Popen("sudo rsync -rpEogvht --delete --update "
                                  "/mnt/windows-share/Users/ryan1/Music/Soggfy/ "
                                  "/export/NAS/Music/", shell=True, stdout=subprocess.PIPE)
        logging.info(output.communicate()[0].decode("utf-8"))
        print("Music dir up-to-date")
        sentCheck = True

    if os.path.exists(musicLoc):
        if os.path.exists(musicRAIDLoc):
            print("\n\nFound RAID")
            logging.info("Moving to RAID")
            output = subprocess.Popen("sudo rsync -rpEogvht --delete --update "
                                          "/mnt/windows-share/Users/ryan1/Music/Soggfy/ /export/RAID1/Music/",
                                          shell=True, stdout=subprocess.PIPE)
            logging.info(output.communicate()[0].decode("utf-8"))
            print("\nRAID up-to-date")
            sentCheck = True

    if not os.path.exists(musicRAIDLoc):
        print("No RAID")

    if not sentCheck:
        print("No music moved")
