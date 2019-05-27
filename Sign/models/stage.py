from db_service import DatabaseService
from ClipQueue.clips.text_clip import TextClip
import random

class Stage:
    def __init__(self, id):
        self.id = id
        self.name = DatabaseService().stage_from_id(id)

        self.clips = [
            self.get_stage_phrase
        ]

    def get_clip(self):
        return random.choice(self.clips)()

    def get_stage_phrase(self):
        phrase = DatabaseService().get_stage_phrase(self.id)
        return TextClip(phrase.format(stage=self.name))
