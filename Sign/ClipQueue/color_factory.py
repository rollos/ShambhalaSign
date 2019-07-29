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

    @staticmethod
    def fade_transparent_image(img, hue_degree, saturation):
        orig_color = (255, 255, 255, 255)
        replacement_color = ColorFactory.hsv_to_rgb(hue_degree, saturation, 50)

        replacement_color = replacement_color + (255,)
        data = np.array(img)

        data[(data == orig_color).all(axis=-1)] = replacement_color
        return Image.fromarray(data, mode='RGBA')

    # Fade between tuple colors by a percent
    @staticmethod
    def fade_between_colors(color1, color2, percent):
        r_dist = color2[0] - color1[0]
        g_dist = color2[1] - color1[1]
        b_dist = color2[2] - color1[2]

        r = color1[0] + (r_dist * percent)
        g = color1[1] + (g_dist * percent)
        b = color1[2] + (b_dist * percent)

        return int(r), int(g), int(b)
