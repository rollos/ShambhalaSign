from db_service import DatabaseService
from ClipQueue.clips.text_clip import TextClip
import random


class Artist:
    def __init__(self, name_key):
        self.name_key = name_key
        self.name = DatabaseService().artist_from_name_key(name_key)

        self.clips = [
            self.get_artist_clip
        ]

    def get_clip(self):
        return random.choice(self.clips)()

    def get_artist_clip(self):
        phrase = DatabaseService().get_artist_phrase(self.name_key)


        return TextClip(phrase.format(artist=self.name))
