
class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song 
    
    def is_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """
        print(self.name) # Hello
        print(self.next.name) # E o t
        playlist = {self}
        print(playlist)
        song = self.next
        while song:
            if song in playlist:
                return True
            else:
                playlist.add(song)
                song = song.next
        return False
            
            
first = Song("Hello")
second = Song("Eye of the tiger")
    
first.next_song(second)
second.next_song(first)
    
print(first.is_repeating_playlist())