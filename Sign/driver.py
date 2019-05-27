from ClipQueue.clip_queue import  ClipQueue
from ClipQueue.clips.text_clip import TextClip
from pybleno import *
from bluetooth.command_characteristic import CommandCharacteristic
import sys
from command_parser import CommandParser
import cProfile
from db_service import DatabaseService



class Driver:
    clipQueue = ClipQueue()
    bleno = Bleno()



    def __init__(self):
        self.bleno.on('stateChange', self.on_state_change)
        self.bleno.on('advertisingStart', self.on_advertising_start)
        self.bleno.start()

        DatabaseService().select_all_phrases()



        # print('Hit <ENTER> to disconnect')
        #
        # input()
        #
        # self.bleno.stopAdvertising()
        # self.bleno.disconnect()
        #
        # print('terminated.')
        # sys.exit(1)


    def write_request_recieved(self, data):
        text = CommandParser.parse_data(data, self.clipQueue.clip_factory)

        if text is not None:
            print(text)
            clip = TextClip(text)

            self.clipQueue.push(clip)

            #self.clipQueue.pop_first_and_run()

    def on_state_change(self, state):
        print('on -> stateChange: ' + state);

        if state == 'poweredOn':
            self.bleno.startAdvertising('echo', ['ec00'])
        else:
            self.bleno.stopAdvertising()

    def on_advertising_start(self, error):
        print('on -> advertisingStart: ' + ('error ' + error if error else 'success'));

        if not error:
            self.bleno.setServices([
                BlenoPrimaryService({
                    'uuid': 'ec00',
                    'characteristics': [
                        CommandCharacteristic('ec0F', self.write_request_recieved)
                    ]
                })
            ])


if __name__ == "__main__":
    driver = Driver()
    driver.clipQueue.generate_and_run()


    # q = ClipQueue()
    #
    # print("test")
    # test1 = TextClip("First Clip", q)
    # test2 = TextClip("Second Clip", q)
    #
    # test3 = TextClip("DAD?", q)
    #
    # #test.run()
    #
    #
    #
    # q.push(test1)
    # q.push(test2)
    # q.push(test3)
    #
    # q.pop_first_and_run()





    # clip_queue = ClipQueue()
    #
    # clip_queue.push(TextClip(clip_queue, "FIRST CLIP"))
    # clip_queue.push(TextClip(clip_queue, "SECOND CLIP"))
    #
    # clip_queue.pop_first_and_run()
