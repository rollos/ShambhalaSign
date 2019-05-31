# Display a runtext with double-buffering.

from .base_clip import BaseClip
from rgbmatrix import graphics
from ..color_factory import ColorFactory
from .constants import FRAME_LENGTH
import time


class TextClip(BaseClip):
    def __init__(self, text, *args, **kwargs):
        super(TextClip, self).__init__(*args, **kwargs)
        self.text = text
       # self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")

    def run(self):
        print("Run")
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()


        font.LoadFont("../fonts/9x15.bdf")

        text_color = ColorFactory.get_color()
        pos = offscreen_canvas.width
        my_text = self.text

        while True:
            offscreen_canvas.Clear()
            len = graphics.DrawText(offscreen_canvas, font, pos, 10, text_color, my_text)
            pos -= 1
            if (pos + len < 0):
                return

            time.sleep(FRAME_LENGTH)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


# Main function
if __name__ == "__main__":
    run_text = TextClip("TEST", None)
    if (not run_text.process()):
        run_text.print_help()
