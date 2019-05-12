from db_service import DatabaseService
from ClipQueue.clips.text_clip import TextClip

class Takeover:
    def __init__(self, name_key):
        self.name_key = name_key
        self.name = DatabaseService().takeover_from_name_key(name_key)


    def get_clip(self):
        return TextClip("{} takeover".format(self.name))