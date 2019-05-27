#!/usr/bin/env python
import time
import random

from .base_clip import BaseClip
from PIL import Image
from ..color_factory import ColorFactory

from .constants import MAX_CLIP_LENGTH, FRAME_LENGTH


class ImageClip(BaseClip):
    def __init__(self, image_path, color_img=False, color_fade=False, *args, **kwargs):
        super(ImageClip, self).__init__(*args, **kwargs)
        self.image = Image.open(image_path)
        self.color_fade = color_fade

        if color_img:
            self.image = ColorFactory.color_image(self.image)

    def run(self):
        print("Run")

        if self.color_fade:
            self.color_fade_run()

        else:
            self.matrix.SetImage(self.image.convert('RGB'))

            time.sleep(random.randrange(MAX_CLIP_LENGTH))

    def color_fade_run(self):

        runtime = random.randrange(MAX_CLIP_LENGTH)
        frames = int(runtime / FRAME_LENGTH)

        start_point = random.randrange(360)
        saturation = random.randrange(50, 100)

        fade_speed = random.randrange(25, 200) / 100

        for i in range(frames):
            colored_image = ColorFactory.fade_image(self.image, start_point + (i * fade_speed), saturation)

            self.matrix.SetImage(colored_image.convert('RGB'))

            time.sleep(FRAME_LENGTH)
