from ClipQueue.clips.text_clip import TextClip
from db_service import DatabaseService
import random

class ClipFactory:
    artist = None
    stage = "DOWNTOWN"
    takeover = None


    def __str__(self):
        representation = ""

        if self.artist is not None:
            representation += "artist: {}".format(self.artist)

        if self.stage is not None:
            representation += " stage: {}".format(self.stage)

        if self.takeover is not None:
            representation += " takeover: {}".format(self.takeover)

        return representation


    def set_artist(self, name_key):
        self.artist = DatabaseService().artist_from_name_key(name_key)


    def set_stage(self, id):
        self.stage = DatabaseService().stage_from_id(id)

    def set_takeover(self, name_key):
        self.takeover = DatabaseService().takeover_from_name_key(name_key)

    def generate_clip(self):

        clip_types = ["stage"]

        if self.artist is not None:
            clip_types.append("artist")

        if self.takeover is not None:
            clip_types.append("takeover")

        choice = random.choice(clip_types)
        print("choice: {}".format(choice))

        if choice == "stage":
            return TextClip("Stage: {}".format(self.stage))

        elif choice == "artist":
            return TextClip("Artist: {}".format(self.artist))

        elif choice == "takeover":
            return TextClip("Welcome to the {} takeover".format(self.takeover))


