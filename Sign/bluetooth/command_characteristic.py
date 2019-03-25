from pybleno import Characteristic
import array
import struct
import sys
import traceback
from builtins import str


class CommandCharacteristic(Characteristic):

    def __init__(self, uuid, write_callback):
        Characteristic.__init__(self, {
            'uuid': uuid,
            'properties': ['read', 'write', 'notify'],
            'value': None
        })

        self._value = array.array('B', [0] * 0)
        self._updateValueCallback = write_callback

    def onReadRequest(self, offset, callback):
        print('EchoCharacteristic - %s - onReadRequest: value = %s' % (self['uuid'], [hex(c) for c in self._value]))
        callback(Characteristic.RESULT_SUCCESS, self._value)

    def onWriteRequest(self, data, offset, withoutResponse, callback):
        self._value = data

        #decoded = "".join(map(chr, data))
       # print('EchoCharacteristic - %s - onWriteRequest: value = %s' % (self['uuid'], decoded))

        if self._updateValueCallback:
            #print('EchoCharacteristic - onWriteRequest: notifying');
            self._updateValueCallback(self._value)

        callback(Characteristic.RESULT_SUCCESS)

    def onSubscribe(self, maxValueSize, updateValueCallback):
        print('EchoCharacteristic - onSubscribe')

        self._updateValueCallback = updateValueCallback

    def onUnsubscribe(self):
        print('EchoCharacteristic - onUnsubscribe');

        self._updateValueCallback = None