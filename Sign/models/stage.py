from db_service import DatabaseService
from ClipQueue.clips.text_clip import TextClip

class Stage:
    def __init__(self, id):
        self.id = id
        self.name = DatabaseService().stage_from_id(id)

    def get_clip(self):
        return TextClip("Stage: {}".format(self.name))