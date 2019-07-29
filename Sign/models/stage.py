from db_service import DatabaseService
from ClipQueue.clips.text_clip import TextClip
from ClipQueue.clips.image_clip import ImageClip
import random

class Stage:
    def __init__(self, id):
        self.id = id
        self.name = DatabaseService().stage_from_id(id)

        self.clips = [
            # self.get_stage_phrase,
            self.get_stage_logo
        ]

    def get_clip(self):
        return random.choice(self.clips)()

    def get_stage_phrase(self):
        phrase = DatabaseService().get_stage_phrase(self.id)
        return TextClip(phrase.format(stage=self.name))

    def get_stage_logo(self):
        switcher = {
            '1': "pagoda",
            '2': "village",
            '3': "fractal",
            '4': "amp",
            '5': "living-room",
            '6': "grove"
        }

        path_to_image = "/home/pi/ShambhalaSign/images/stages/pixel-{}.png".format(switcher[self.id])

        print(path_to_image)

        return ImageClip(path_to_image, color_fade=True, transparent=True)

