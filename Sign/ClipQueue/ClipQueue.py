from .clips.text_clip import TextClip

class ClipQueue:
    clip_queue = []

    def push(self, clip):
        self.clip_queue.append(clip)

    def pop_first_and_run(self):
        clip = self.clip_queue.pop(0)
        clip.run()

    def finished(self):
        if self.clip_queue:
            self.pop_first_and_run()

