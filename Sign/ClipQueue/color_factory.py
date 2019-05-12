from rgbmatrix import graphics
import random
from PIL import Image
import numpy as np

class ColorFactory:
    @staticmethod
    def get_color():
        return graphics.Color(random.randrange(255), random.randrange(255), random.randrange(255))

    @staticmethod
    def get_tuple_color():
        return (random.randrange(255), random.randrange(255), random.randrange(255))

    @staticmethod
    def color_img(img):
        orig_color = (255, 255, 255)
        replacement_color = ColorFactory.get_tuple_color()
        data = np.array(img)
        data[(data == orig_color).all(axis=-1)] = replacement_color
        return Image.fromarray(data, mode='RGB')
