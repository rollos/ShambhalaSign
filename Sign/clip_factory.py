from ClipQueue.clips.text_clip import TextClip

class ClipFactory:
    artist = None
    stage = "DOWNTOWN"
    takeover = None


    def set_artist(self, name_key):
        self.artist = name_key


    def set_stage(self, id):
        self.stage = id

    def set_takeover(self, name_key):
        self.takeover = name_key



    def generate_clip(self):
        if self.artist is not None:
            return TextClip("Now playing: {}".format(self.artist))
        if self.stage is not None:
            return TextClip("Welcome to: {}".format(self.stage))

        if self.takeover is not None:
            return TextClip("Welcome to the {} takeover".format(self.takeover))
