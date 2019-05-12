from ClipQueue.clips.text_clip import TextClip
from datetime import *


class GenericClipFactory:

    def __init__(self):
        self.clips = [self.get_time_to_shambs_clip]


    def get_clip(self):

        return self.get_time_to_shambs_clip()



    def get_time_to_shambs_clip(self):
        today = date.today()
        future = date(2019, 8, 9)

        diff = future - today

        return TextClip("{} days til Shambhala!!".format(diff.days))

