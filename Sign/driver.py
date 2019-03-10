from ClipQueue.ClipQueue import  ClipQueue
from ClipQueue.clips.text_clip import TextClip



if __name__ == "__main__":

    print("test")
    test = TextClip("First Clip", None)
    test.run()

    # clip_queue = ClipQueue()
    #
    # clip_queue.push(TextClip(clip_queue, "FIRST CLIP"))
    # clip_queue.push(TextClip(clip_queue, "SECOND CLIP"))
    #
    # clip_queue.pop_first_and_run()
