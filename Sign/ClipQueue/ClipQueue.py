from .clips.text_clip import TextClip
import queue

class ClipQueue:
    clip_queue = queue.Queue()

    def push(self, clip):
        self.clip_queue.put(clip)

    def pop_first_and_run(self):
        clip = self.clip_queue.get()
        clip.run()

    def finished(self):
        if not self.clip_queue.empty():
            self.pop_first_and_run()
        else:
            print("EMPTY")

