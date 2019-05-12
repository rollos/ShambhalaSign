#!/usr/bin/env python
import time
import sys
import random

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from .base_clip import BaseClip
from PIL import Image
from ..color_factory import ColorFactory

MAX_IMAGE_LENGTH = 10


class ImageClip(BaseClip):
    def __init__(self, image_path, color_img = False, *args, **kwargs):
        super(ImageClip, self).__init__(*args, **kwargs)
        print(image_path)
        self.image = Image.open(image_path)

        if color_img:
            self.image = ColorFactory.color_img(self.image)


    def run(self):
        print("Run")

        self.matrix.SetImage(self.image.convert('RGB'))

        time.sleep(random.randrange(MAX_IMAGE_LENGTH))
