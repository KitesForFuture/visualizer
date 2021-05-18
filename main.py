from flydata import Flydata
from plot import Plot
from reader import Reader

class Visualizer:

    def __init__(self, port, baudrate, tag, buffer_len):

        self.plot = Plot()

        self.reader = Reader(port, baudrate, len(tag)+buffer_len)
        self.reader.register_tag_listener(tag, buffer_len, self.process_flydata)
        self.reader.start()

    def process_flydata (self, bytes):
        flydata = Flydata(bytes)
        self.plot.update([flydata.x_rotation, flydata.y_rotation, flydata.z_rotation])


Visualizer("/dev/tty.usbserial-0001", 115200, b"FLYDATA", 40)
