from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import logging
import time
import os, traceback
from dotenv import load_dotenv


# This is the function to download a zip file of all the spotify playlists in a given account.
# It takes advantage of selenium to run exportify.
def playlistdownloader(downloadsPath):
    logging.info("starting playlist download")
    try:
        os.environ['MOZ_HEADLESS'] = '1'
        logging.info("Accepted headless load")
        load_dotenv()
        USERNAME = os.getenv("SPOTIFY_USERNAME")
        PASSWORD = os.getenv("SPOTIFY_PASSWORD")
        # Open web browser and clear downloads folder of zipped file (important for checks later on)
        driver = webdriver.Firefox()
        action = ActionChains(driver)
        logging.info("Loaded webdriver")
        zippedFile = "spotify_playlists.zip"

        # Maximise window and navigate to exportify and click login
        driver.get("https://watsonbox.github.io/exportify/")
        logging.info("Loaded site")
        driver.set_window_size(2000, 2000)
        exportifyLogin = driver.find_element(By.ID, "loginButton")
        logging.info("Found login button")
        action.move_to_element(exportifyLogin).click(exportifyLogin).perform()
        time.sleep(5)
        logging.info("Pressed login")
        # Login to spotify
        spotifyUsername = driver.find_element(By.ID, "login-username")
        spotifyPassword = driver.find_element(By.ID, "login-password")
        logging.info("Found username and password area")
        spotifyLoginButton = driver.find_element(By.ID, "login-button")
        spotifyUsername.send_keys(USERNAME)
        spotifyPassword.send_keys(PASSWORD)
        logging.info("Filled in username and password")
        action.move_to_element(spotifyLoginButton).click(spotifyLoginButton).perform()
        time.sleep(5)
        logging.info("Pressed login")
        # TAB to appropriate button and press enter (this exports all of the users playlists)
        i = 8
        print("\n\nWaiting for extraction of playlists and subsequent zip file download")
        exportAll = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/table/thead/tr/th[7]/button")
        action.move_to_element(exportAll).click(exportAll).perform()

        # while i > 0:
        #     action.send_keys(Keys.TAB).perform()
        #     i -= 1
        #     time.sleep(1)
        # action.send_keys(Keys.ENTER).perform()
        print("\nStarting download of playlists\n")
        # Check to close browser only after the file exists and has had a few seconds to download.
        # On a slow connection this may be an issue
        try:
            os.remove(downloadsPath + zippedFile)
        except:
            print("")
        fileExists = False
        counter = 0
        while not fileExists:
            fileExists = os.path.exists(downloadsPath + zippedFile)
            time.sleep(1)
            counter += 1
            if counter > 1000:
                fileExists = True


        # Check if zip file downlaoded after timeout
        if os.path.exists(downloadsPath+zippedFile):
            print("Playlists downloaded\n\n")
        # If zip file not found, check for old downloaded playlist data, if not found exit
        elif not (os.path.exists(downloadsPath + zippedFile)):
            print("Checking for old playlist information\n\n")
            for root, dirs, files in os.walk(downloadsPath):
                # print(dirs)
                try:
                    if dirs[0] is not None:
                        for directory in dirs:
                            # print("Directory = " + directory)
                            if directory.contains("playlists"):
                                print("Playlist download timed out. Continuing on old playlist information")
                except:
                    if files is not None:
                        print("Error downloading, using old information.")

        # Close window
        driver.close()

    except Exception:
        print(traceback.format_exc())
        print("Error downloading, moving on with script")
        driver = webdriver.Firefox()
        driver.close()

