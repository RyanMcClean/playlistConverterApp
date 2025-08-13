"""Creates converted playlist files
"""

class PlaylistFileCreator:
    """Class to handle .m3u playlist file creation"""

    def __init__(self, converted_playlists_path):
        """Constructor for playlist file creator

        Args:
            converted_playlists_path (String): Path to the converted playlists directory as defined in appSettings.json
        """
        self.converted_playlists_path = converted_playlists_path

    def create_playlist_file(self, playlist):
        """Creates a playlist file (.m3u) from the given playlist.

        Args:
            playlist (string[]): List of songs in the playlist, the first item in the list is the playlist name
        """
        if len(playlist) > 1:
            file_name = self.converted_playlists_path + playlist[0].replace("txt", "m3u")
            # This is how I get around filename length limits
            file_name = file_name if len(file_name) < 143 else file_name[0:143]
            with open(file_name, "w", encoding="utf-8") as fp:
                for num, i in enumerate(playlist):
                    if num == 0:
                        continue
                    if i is not None:
                        fp.write(i + "\n")
