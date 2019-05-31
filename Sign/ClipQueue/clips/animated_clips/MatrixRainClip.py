from ..base_clip import BaseClip
import random

from ..constants import MAX_CLIP_LENGTH, FRAME_LENGTH
import time

class MatrixRainClip(BaseClip):

    def __init__(self, *args, **kwargs):
        super(MatrixRainClip, self).__init__(*args, **kwargs)

    def run(self):
        print("run")
        offscreen_canvas = self.matrix.CreateFrameCanvas()

        columns = []
        for i in range(self.matrix.width // 2):
            columns.append(Column(i * 2, offscreen_canvas))

        runtime = random.randrange(MAX_CLIP_LENGTH)
        frames = int(runtime / FRAME_LENGTH)

        for i in range(frames):
            offscreen_canvas.Clear()

            for column in columns:
                column.move()
                column.update()

            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

            time.sleep(FRAME_LENGTH/5)


class Column:

    row_width = 2

    def __init__(self, x, canvas):
        self.x = x
        self.canvas = canvas

        self.clear_and_restart(400)

    def clear_and_restart(self, start_pos=200):
        # Reset column to black

        self.list = []

        # for i in range(self.canvas.height):
        #     self.canvas.SetPixel(self.x, i, 0, 0, 0)

        self.y = - random.randrange(start_pos)

        self.fade_age = random.randint(2, 4)
        self.fade_speed = 2

    def add_new_symbol(self):
        if 0 < self.y < self.canvas.height:
            self.list.append(Symbol(self, self.canvas))

    def move(self):
        if self.list and self.list[-1].color == (0, 0, 0):
            self.clear_and_restart()

        self.y += 1
        if len(self.list) < 16:
            self.add_new_symbol()

    def update(self):
        for symbol in self.list:
            symbol.update()
            if symbol.x > self.canvas.height:
                del symbol


class Symbol:

    def __init__(self, column, canvas):
        self.x = column.x
        self.y = column.y
        self.canvas = canvas

        self.age = 0
        self.fade_age = column.fade_age
        self.fade_speed = column.fade_speed

    def update(self):
        self.draw()
        self.age += 1

    def draw(self):
        self.color_function()

        if 0 < self.y < self.canvas.height:
            self.canvas.SetPixel(self.x, self.y, self.color[0], self.color[1], self.color[2])



    def color_function(self):
        """
        At 'age' 0-10, the symbol turn from grey (225, 225, 225) to green (0, 155, 0)
        At high 'age' (random value) the symbol turn from green to black over a period
        determined by the fade_speed value.
        """

        if self.age < 11:
            self.color = (225 - self.age * 22, 225 - 7 * self.age, 225 - self.age * 22)

        elif self.age > self.fade_age:
            self.color = (0, max(0, 155 - (self.age - self.fade_age) * self.fade_speed), 0)


