# Streaming Playlist Converter

## Current functionality
Currently the application supports downloading Spotify Playlists as text files.

The app also has the function of matching these playlists to local files and 
creating a `.m3u` file which has the file paths of the songs. Which can then be uploaded to Plex. 

## Future goals
The goal is to expand the functionality of the app to be able to transfer the playlists downloaded from a streaming service into another service. This has been achieved with an upload to a local plex server, but isn't helpful if you don't have a local music collection.

- Step 1. Add ability to upload playlists to Tidal 
- Step 2. Add ability to download playlists from Tidal
- Step 3. Add ability to upload playlists to Spotify (This needs to be possible without a paid spotify account, as I don't have one anymore)

## How to use
- Clone this repository (master branch)
- Copy the `appSettingsTemplate.json` to simply `appSettings.json`
- Fill in the fields in `appSettings.json`, there are comment variables in the json that explain what each field is
- Run `python ./main.py --help`
- Read through the options for main and run what you need

### Use of this might be against some terms of service, use at own risk

## To Do

### Clean up needed
The app needs a clean up, the file structure is a nightmare. Need to split some files into helper functions. Clean up main. 

### Add testing
The app needs testing. Particularly around the find algorithm which is a nightmare. 
