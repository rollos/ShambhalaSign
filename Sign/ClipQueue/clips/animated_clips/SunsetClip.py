
from ..base_clip import BaseClip
from PIL import Image, ImageEnhance, ImageDraw
from ..constants import FRAME_LENGTH, MAX_CLIP_LENGTH
import random
from ...color_factory import ColorFactory
import math

from rgbmatrix import graphics
import time

class SunsetClip(BaseClip):

    def __init__(self, *args, **kwargs):
        super(SunsetClip, self).__init__(*args, **kwargs)
        self.image = Image.open("/home/pi/ShambhalaSign/images/sunset.png")

    def run(self):

        runtime = random.randrange(MAX_CLIP_LENGTH)

        offscreen_canvas = self.matrix.CreateFrameCanvas()

        frame_width, frame_height = self.matrix.width, self.matrix.height

        image_size = frame_width

        self.image.thumbnail((image_size, image_size))

        enhancer = ImageEnhance.Brightness(self.image)
        self.image = enhancer.enhance(.5)

        sun_start_color = (255, 255, 0)
        sun_end_color = (112, 40, 22)

        sun_top = -8

        # Move vertically down the image until it reaches the bottom
        for i in range(image_size - frame_height):
            offscreen_canvas.Clear()

            # Copy the image
            frame = self.image.copy()

            left, right = 0, self.matrix.width

            # Frame starts at top of image
            upper = i
            lower = upper + frame_height

            frame_rec = (left, upper, right, lower)

            frame = frame.crop(frame_rec)

            draw = ImageDraw.Draw(frame)

            # Calculate the color of the sun, which is going to be part way between
            # Two colors depending on the distance through the frame
            percent = i / (image_size - frame_height)
            sun_color = ColorFactory.fade_between_colors(sun_start_color, sun_end_color, (math.sqrt(percent)))

            sun_top += .3

            draw.ellipse((28, int(sun_top), 36, int(sun_top) + 8), fill= sun_color)

            offscreen_canvas.SetImage(frame.convert('RGB'))

            time.sleep(runtime / (image_size - frame_height))

            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)



        # self.matrix.SetImage(self.image.convert('RGB'))
        #
        # time.sleep(random.randrange(MAX_CLIP_LENGTH))

