# Display a runtext with double-buffering.

from .base_clip import BaseClip
from rgbmatrix import graphics
import time


class TextClip(BaseClip):
    def __init__(self, text, delegate, *args, **kwargs):
        super(TextClip, self).__init__(delegate, *args, **kwargs)
        self.text = text
       # self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")

    def run(self):
        print("Run")
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()


        font.LoadFont("../fonts/7x13.bdf")
        textColor = graphics.Color(255, 255, 0)
        pos = offscreen_canvas.width
        my_text = self.text

        while True:
            offscreen_canvas.Clear()
            len = graphics.DrawText(offscreen_canvas, font, pos, 10, textColor, my_text)
            pos -= 1
            if (pos + len < 0):
                self.delegate.finished()
                return

            time.sleep(0.05)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


# Main function
if __name__ == "__main__":
    run_text = TextClip("TEST", None)
    if (not run_text.process()):
        run_text.print_help()
