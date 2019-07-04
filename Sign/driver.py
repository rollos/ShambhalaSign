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
    run = False

    def __init__(self):
        self.bleno.on('stateChange', self.on_state_change)
        self.bleno.on('advertisingStart', self.on_advertising_start)
        self.bleno.start()

        # DatabaseService().select_all_phrases()
        #


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

        decoded = CommandParser.decode(data)

        print("DECODE")
        print(decoded)
        if decoded == "POWER-ON":
            if not self.clipQueue.running:
                print("starting...")
                self.run = True

            return

        elif decoded == "POWER-OFF":
            power_off()
            return


        if self.clipQueue.running:
            text = CommandParser.parse_data(decoded, self.clipQueue.clip_factory)

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


def power_off():
    command = "/usr/bin/sudo /sbin/shutdown -r now"
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print(output)

if __name__ == "__main__":
    driver = Driver()

    while True:
        if driver.run:
            driver.clipQueue.running = True
            driver.clipQueue.generate_and_run()
            driver.run = False
