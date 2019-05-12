from db_service import DatabaseService
from ClipQueue.clips.text_clip import TextClip


class Artist:
    def __init__(self, name_key):
        self.name_key = name_key
        self.name = DatabaseService().artist_from_name_key(name_key)


    def get_clip(self):
        return TextClip("Artist: {}".format(self.name))