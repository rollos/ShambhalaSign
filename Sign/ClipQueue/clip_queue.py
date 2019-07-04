from clip_factory import ClipFactory

import queue

class ClipQueue:
    clip_queue = queue.Queue()
    clip_factory = ClipFactory()
    running = False

    def push(self, clip):
        self.clip_queue.put(clip)

    def pop_first_and_run(self):
        clip = self.clip_queue.get()
        clip.run()

    def finished(self):
        self.generate_and_run()

    def generate_and_run(self):
        while True:
            if self.clip_queue.qsize() < 1:
                clip = self.clip_factory.generate_clip()
                self.push(clip)

            self.pop_first_and_run()
