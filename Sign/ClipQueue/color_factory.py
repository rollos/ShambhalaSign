from rgbmatrix import graphics
import random
from PIL import Image
import numpy as np
import colorsys

class ColorFactory:
    @staticmethod
    def get_color():
        color = ColorFactory.get_tuple_color()
        return graphics.Color(color[0], color[1], color[2])

    @staticmethod
    def get_tuple_color():
        # Use HSV so that we don't get dull grey colors
        return ColorFactory.hsv_to_rgb(random.randrange(0, 360), random.randrange(50, 100), random.randrange(50, 70))

    @staticmethod
    def color_image(img):
        orig_color = (255, 255, 255)
        replacement_color = ColorFactory.get_tuple_color()
        data = np.array(img)
        data[(data == orig_color).all(axis=-1)] = replacement_color
        return Image.fromarray(data, mode='RGB')

    @staticmethod
    def hsv_to_rgb(h, s, v):
        hue = (h % 360) / 360
        saturation = s / 100
        value = v / 100

        rgb = colorsys.hsv_to_rgb(hue, saturation, value)

        return tuple(255 * x for x in rgb)


    @staticmethod
    def fade_image(img, hue_degree, saturation):
        orig_color = (255, 255, 255)
        replacement_color = ColorFactory.hsv_to_rgb(hue_degree, saturation, 50)

        data = np.array(img)

        data[(data == orig_color).all(axis=-1)] = replacement_color
        return Image.fromarray(data, mode='RGB')
