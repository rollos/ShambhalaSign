from clip_factory import ClipFactory

import queue

class ClipQueue:
    clip_queue = queue.Queue()
    clip_factory = ClipFactory()
    running = False

    def __init__(self):
        self.current_clip = None

    def push(self, clip):
        self.clip_queue.put(clip)

    def stop_current(self):
        print("Stopping Current Clip")
        self.current_clip.cutoff = True


    def pop_first_and_run(self):
        self.current_clip = self.clip_queue.get()
        self.current_clip.run()

    def finished(self):
        self.generate_and_run()

    def generate_and_run(self):
        while True:
            if self.clip_queue.qsize() < 1:
                clip = self.clip_factory.generate_clip()
                self.push(clip)

            self.pop_first_and_run()
