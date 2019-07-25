from models.artist import Artist
from models.stage import Stage
from models.takeover import Takeover
from models.generic_clip_factory import GenericClipFactory
import random

class ClipFactory:
    artist = None
    stage = None
    takeover = None
    generic_clip_factory = GenericClipFactory()


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
        self.artist = Artist(name_key)


    def set_stage(self, id):
        if self.stage is None:
            if id == "none":
                return False
            else:
                self.stage = Stage(id)
                return True
        else:
            if self.stage.id == id:
                return False
            else:
                self.stage = Stage(id)
                return True


    def set_takeover(self, name_key):
        self.takeover = Takeover(name_key)

    def generate_clip(self):

        clip_types = ["generic"]

        if self.stage is not None:
            clip_types.append("stage")

        if self.artist is not None:
            clip_types.append("artist")

        if self.takeover is not None:
            clip_types.append("takeover")

        print(clip_types)
        choice = random.choice(clip_types)
        print("choice: {}".format(choice))

        if choice == "stage":
            return self.stage.get_clip()

        elif choice == "artist":
            return self.artist.get_clip()

        elif choice == "takeover":
            return self.takeover.get_clip()

        elif choice == "generic":

            if self.stage is None:
                return self.generic_clip_factory.get_owl_image()
            else:
                return self.generic_clip_factory.get_clip()


