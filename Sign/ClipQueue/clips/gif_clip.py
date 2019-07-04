#!/usr/bin/env python
import time
import random

from .base_clip import BaseClip
from PIL import Image
from ..color_factory import ColorFactory

from .constants import MAX_CLIP_LENGTH, FRAME_LENGTH, MAX_LOOP_COUNT


class GifClip(BaseClip):
    def __init__(self, image_path, offset=0, frames_per_frame=1, *args, **kwargs):
        super(GifClip, self).__init__(*args, **kwargs)
        self.image = Image.open(image_path)
        self.offset = offset
        self.frames_per_frame = frames_per_frame

    def run(self):
        print("Run")

        runtime = random.randrange(MAX_CLIP_LENGTH)
        frames = int(runtime / FRAME_LENGTH)

        loop_count = int (frames / self.image.n_frames)

        if loop_count == 0:
            loop_count = 1

        if loop_count > MAX_LOOP_COUNT:
            loop_count = MAX_LOOP_COUNT

        print(loop_count)

        for loop in range(loop_count):
            for frame in range(0, self.image.n_frames):
                self.image.seek(frame)


                self.matrix.SetImage(self.image.convert('RGB'), self.offset, 0)

                time.sleep(FRAME_LENGTH * self.frames_per_frame)

        self.matrix.Clear()

