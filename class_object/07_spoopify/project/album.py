from project.song import Song


class Album:

    def __init__(self, name: str, *args):
        self.name = name
        self.songs = args
        self.published = False
        self.songs = []

    def add_song(self, song: Song):
        if self.published:
            return f'Cannot add songs. Album is published.'
        if song.single:
            return f'Cannot add {song.name}. It\'s a single'
        if song in self.songs:
            return f'Song is already in the album.'
        self.songs.append(song)
        return f'Song {song.name} has been added to the album {self.name}.'

    def remove_song(self, song_name: str):
        if not self.published:
            for song in self.songs:
                if song_name == song.name:
                    self.songs.remove(song)
                    return f'Removed song {song_name} from album {self.name}.'
            return f'Song is not in the album.'
        return f'Cannot remove songs. Album is published.'

    def publish(self):
        if not self.published:
            self.published = True
            return f'Album {self.name} has been published.'
        return f'Album {self.name} is already published.'

    def details(self):
        result = f'Album {self.name}\n'
        for song in self.songs:
            result += f'== {song.get_info()}'
        return result
