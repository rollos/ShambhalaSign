from ClipQueue.ClipQueue import  ClipQueue
from ClipQueue.clips.text_clip import TextClip
import queue



if __name__ == "__main__":
    q = ClipQueue()

    print("test")
    test1 = TextClip("First Clip", q)
    test2 = TextClip("Second Clip", q)

    #test.run()



    q.push(test1)
    q.push(test2)

    q.pop_first_and_run()





    # clip_queue = ClipQueue()
    #
    # clip_queue.push(TextClip(clip_queue, "FIRST CLIP"))
    # clip_queue.push(TextClip(clip_queue, "SECOND CLIP"))
    #
    # clip_queue.pop_first_and_run()
