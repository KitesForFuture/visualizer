import threading
import serial
import collections

class Reader:

    '''
    Ringbuffer size should be at least:
        longest combination of (expected buffer + tag length)
    '''
    def __init__(self, port, baudrate, ringbuffer_size):
        self.serialPort = serial.Serial(port=port, baudrate=baudrate, bytesize=8, stopbits=serial.STOPBITS_ONE)
        self.listeners = []
        self.ringbuffer = collections.deque([b'\7' for i in range(ringbuffer_size)], maxlen=ringbuffer_size)
        self.ringbuffer_size = ringbuffer_size

    def _read(self):
        while True:
            # Read
            new_byte = bytes(self.serialPort.read(1))
            self.ringbuffer.append(new_byte)
            # Notify listeners
            ringbuffer_string = b''.join(self.ringbuffer)
            for (tag, buffer_len, listener) in self.listeners:
                '''
                We must ensure to never process a tag twice. Hence we notify ONLY when the
                very last byte of the buffer_len arrives. Not before, not after.
                That implies we only need to check for the given tag at the position:
                end of ringbuffer minus buffer_len
                '''
                tag_start_index = self.ringbuffer_size - (buffer_len + len(tag))
                if ringbuffer_string[tag_start_index:(tag_start_index + len(tag))] == tag:
                    bytes_for_listener = bytes(ringbuffer_string[tag_start_index+len(tag):])
                    listener(bytes_for_listener)

    def register_tag_listener(self, tag, buffer_len, listener):
        self.listeners.append((tag, buffer_len, listener))

    def start(self):
        threading.Thread(target=self._read()).start()
