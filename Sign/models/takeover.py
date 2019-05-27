from db_service import DatabaseService
from ClipQueue.clips.text_clip import TextClip
import random

class Takeover:
    def __init__(self, name_key):
        self.name_key = name_key
        self.name = DatabaseService().takeover_from_name_key(name_key)

        self.clips = [
            self.get_takeover_phrase
        ]

    def get_clip(self):
        return random.choice(self.clips)()

    def get_takeover_phrase(self):
        phrase = DatabaseService().get_takeover_phrase(self.name_key)
        return TextClip(phrase.format(takeover=self.name))