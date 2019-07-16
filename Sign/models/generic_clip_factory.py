from ClipQueue.clips.text_clip import TextClip
from ClipQueue.clips.image_clip import ImageClip
from ClipQueue.clips.animated_clips.SunsetClip import SunsetClip
from ClipQueue.clips.animated_clips.MatrixRainClip import MatrixRainClip
from ClipQueue.clips.gif_clip import GifClip
from datetime import *
from db_service import DatabaseService
import random


class GenericClipFactory:

    def __init__(self):
        self.clips = [
            self.get_time_to_shambs_clip,
            self.get_owl_image,
            self.get_generic_phrase,
            self.get_sunset_image,
            self.get_matrix_rain_clip,
            self.get_eye_clip,
            self.get_watering_can_clip,
            self.get_orbit_clip,
            self.get_square_rotator_clip,
            self.get_unraveling_spiral_clip,
            self.get_bouncing_pixel,
            self.get_spiral_ball_clip,
            self.get_hexagons_clip,
            self.get_brainwaves_clip,
            self.get_bird_dance_clip,
            self.get_hex_shift_clip,
            self.get_mesmer_clip,
            self.get_pulse_clip,
            self.get_waveform1_clip,
            self.get_pink_wave_clip,
            self.get_green_loop_clip,
            self.get_color_waves_clip,
            self.get_headspace_clip,
            self.get_polka_dot_clip,
            self.get_rainbow_mandela,
            self.get_dark_mandela,
            self.get_galaxy_spiral,
            self.get_moon_eclipse,
            self.get_art_shit,
            self.get_star_spiral,
            self.get_hexagon_fractal,
            self.get_fur_waves,
            self.get_chicken_run,
            self.get_soundwaves_one,
            self.get_mountain_waves,
            self.get_head_spikes,
            self.get_running_dude,
            self.get_color_ripple,
            self.get_negative_color,
            self.get_all_seeing,
            self.get_motion,
            self.get_television_glitch
                   ]

    def get_clip(self):
        return random.choice(self.clips)()

    def get_time_to_shambs_clip(self):
        today = date.today()
        future = date(2019, 8, 9)

        diff = future - today

        return TextClip("{} days til Shambhala!!".format(diff.days))

    def get_generic_phrase(self):
        phrase = DatabaseService().get_generic_phrase()
        return TextClip(phrase)

    def get_owl_image(self):
        return ImageClip("/home/pi/ShambhalaSign/images/owl.png", color_fade=True)


    def get_sunset_image(self):
        return SunsetClip()

    def get_matrix_rain_clip(self):
        return MatrixRainClip()

    def get_eye_clip(self):
        return GifClip("/home/pi/ShambhalaSign/images/gifs/eye.gif", offset=16, frames_per_frame=5)

    def get_watering_can_clip(self):
        return GifClip("/home/pi/ShambhalaSign/images/gifs/watering-can.gif", offset=16, frames_per_frame=5)

    def get_orbit_clip(self):
        return GifClip("/home/pi/ShambhalaSign/images/gifs/orbit.gif", offset=24, frames_per_frame=5)

    def get_square_rotator_clip(self):
        return GifClip("/home/pi/ShambhalaSign/images/gifs/square-rotator.gif", offset=24)

    def get_unraveling_spiral_clip(self):
        return GifClip("/home/pi/ShambhalaSign/images/gifs/unraveling-spiral.gif")

    def get_bouncing_pixel(self):
        return GifClip("/home/pi/ShambhalaSign/images/gifs/bouncing-pixel.gif", frames_per_frame=1.5)

    def get_spiral_ball_clip(self):
        return GifClip("/home/pi/ShambhalaSign/images/gifs/spiral-ball.gif")

    def get_hexagons_clip(self):
        return GifClip("/home/pi/ShambhalaSign/images/gifs/hexagons.gif")

    def get_brainwaves_clip(self):
            return GifClip("/home/pi/ShambhalaSign/images/gifs/brainwaves.gif", frames_per_frame=1, offset=16)

    def get_bird_dance_clip(self):
        return GifClip("/home/pi/ShambhalaSign/images/gifs/bird-dance.gif", frames_per_frame=3, offset=24)

    def get_hex_shift_clip(self):
        return GifClip("/home/pi/ShambhalaSign/images/gifs/hex-shift.gif", offset=24)

    def get_mesmer_clip(self):
        return GifClip("/home/pi/ShambhalaSign/images/gifs/mesmer.gif", offset=24)

    def get_pulse_clip(self):
        return GifClip("/home/pi/ShambhalaSign/images/gifs/pulse.gif")

    def get_waveform1_clip(self):
        return GifClip("/home/pi/ShambhalaSign/images/gifs/waveform1.gif")

    def get_pink_wave_clip(self):
        return GifClip("/home/pi/ShambhalaSign/images/gifs/pink-wave.gif", frames_per_frame=2)

    def get_green_loop_clip(self):
        return GifClip("/home/pi/ShambhalaSign/images/gifs/green-loop.gif")

    def get_color_waves_clip(self):
        return GifClip("/home/pi/ShambhalaSign/images/gifs/color-waves.gif")

    def get_headspace_clip(self):
        return GifClip("/home/pi/ShambhalaSign/images/gifs/headspace.gif")

    def get_polka_dot_clip(self):
        return GifClip("/home/pi/ShambhalaSign/images/gifs/polka-dot.gif")

    def get_rainbow_mandela(self):
        return GifClip("/home/pi/ShambhalaSign/images/gifs/rainbow-mandela.gif")

    def get_dark_mandela(self):
        return GifClip("/home/pi/ShambhalaSign/images/gifs/dark-mandela.gif", frames_per_frame=2)

    def get_galaxy_spiral(self):
        return GifClip("/home/pi/ShambhalaSign/images/gifs/galaxy-spiral.gif")

    def get_moon_eclipse(self):
        return GifClip("/home/pi/ShambhalaSign/images/gifs/moon-eclipse.gif", offset=24)

    def get_art_shit(self):
        return GifClip("/home/pi/ShambhalaSign/images/gifs/art-shit.gif")

    def get_star_spiral(self):
        return GifClip("/home/pi/ShambhalaSign/images/gifs/star-spiral.gif")

    def get_hexagon_fractal(self):
        return GifClip("/home/pi/ShambhalaSign/images/gifs/hexagon_fractal.gif")

    def get_fur_waves(self):
        return GifClip("/home/pi/ShambhalaSign/images/gifs/fur-waves.gif")

    def get_chicken_run(self):
        return GifClip("/home/pi/ShambhalaSign/images/gifs/chicken-run.gif", offset=24, frames_per_frame=3)

    def get_soundwaves_one(self):
        return GifClip("/home/pi/ShambhalaSign/images/gifs/soundwaves-1.gif")

    def get_mountain_waves(self):
        return GifClip("/home/pi/ShambhalaSign/images/gifs/mountain-waves.gif")

    def get_head_spikes(self):
        return GifClip("/home/pi/ShambhalaSign/images/gifs/head-spikes.gif")

    def get_running_dude(self):
        return GifClip("/home/pi/ShambhalaSign/images/gifs/running-dude.gif", offset=24, frames_per_frame=3)

    def get_color_ripple(self):
        return GifClip("/home/pi/ShambhalaSign/images/gifs/color-ripple.gif")

    def get_negative_color(self):
        return GifClip("/home/pi/ShambhalaSign/images/gifs/negative-color.gif", frames_per_frame=2)

    def get_all_seeing(self):
        return GifClip("/home/pi/ShambhalaSign/images/gifs/all-seeing.gif")

    def get_motion(self):
        return GifClip("/home/pi/ShambhalaSign/images/gifs/motion.gif")

    def get_television_glitch(self):
        return GifClip("/home/pi/ShambhalaSign/images/gifs/television-glitch.gif")
