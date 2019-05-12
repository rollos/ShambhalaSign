from rgbmatrix import graphics
import random

class ColorFactory:
    @staticmethod
    def get_color():
        return graphics.Color(random.randrange(255), random.randrange(255), random.randrange(255))