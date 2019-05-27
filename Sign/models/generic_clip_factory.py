from ClipQueue.clips.text_clip import TextClip
from ClipQueue.clips.image_clip import ImageClip
from datetime import *
from db_service import DatabaseService
import random


class GenericClipFactory:

    def __init__(self):
        self.clips = [self.get_time_to_shambs_clip,
                      self.get_owl_image,
                      self.get_generic_phrase]

    def get_clip(self):
        return random.choice(self.clips)()

    def get_time_to_shambs_clip(self):
        today = date.today()
        future = date(2019, 8, 9)

        diff = future - today

        return TextClip("{} days til Shambhala!!".format(diff.days))

    def get_generic_phrase(self):
        phrase = DatabaseService().get_generic_phrase()
        return TextClip(phrase)

    def get_owl_image(self):
        return ImageClip("/home/pi/ShambhalaSign/images/owl.png", True)
