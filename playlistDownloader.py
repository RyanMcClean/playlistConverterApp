from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
from dotenv import load_dotenv


# This is the function to download a zip file of all the spotify playlists in a given account.
# It takes advantage of selenium to run exportify.
def playlistdownloader(downloadsPath):
    os.environ['MOZ_HEADLESS'] = '1'
    load_dotenv()
    USERNAME = os.getenv("SPOTIFY_USERNAME")
    PASSWORD = os.getenv("SPOTIFY_PASSWORD")
    # Open web browser and clear downloads folder of zipped file (important for checks later on)
    driver = webdriver.Firefox()
    action = ActionChains(driver)
    zippedFile = "spotify_playlists.zip"
    # try:
    #     os.remove(downloadsPath + zippedFile)
    # except:
    #     print("")
    # Maxamise window and navigate to exportify and click login
    driver.get("https://watsonbox.github.io/exportify/")
    exportifyLogin = driver.find_element(By.ID, "loginButton")
    action.move_to_element(exportifyLogin).click(exportifyLogin).perform()
    time.sleep(1)
    # Login to spotify
    spotifyUsername = driver.find_element(By.ID, "login-username")
    spotifyPassword = driver.find_element(By.ID, "login-password")
    spotifyLoginButton = driver.find_element(By.ID, "login-button")
    spotifyUsername.send_keys(USERNAME)
    spotifyPassword.send_keys(PASSWORD)
    action.move_to_element(spotifyLoginButton).click(spotifyLoginButton).perform()
    time.sleep(2.5)
    # TAB to appropriate button and press enter (this exports all users playlists)
    i = 8
    while i > 0:
        action.send_keys(Keys.TAB).perform()
        i -= 1
    action.send_keys(Keys.ENTER).perform()
    print("\nStarting download of playlists\n")
    # Check to close browser only after the file exists and has had a few seconds to download.
    # On a slow connection this may be an issue
    # fileExists = False
    # while not fileExists:
    #     fileExists = os.path.exists(downloadsPath + zippedFile)
    #     time.sleep(15)
    # print("Playlists downloaded\n\n")
    # Close window
    time.sleep(200)
    driver.close()
