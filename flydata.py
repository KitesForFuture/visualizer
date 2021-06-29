import struct

class Flydata():

    def __init__(self, bytes):
        # Cycle-Time (1), Height (1), Gyro-Vector (3), Accel-Vector (3), Rotation-Matrix (9), G-Correction-Axis (3), G-Correction-Angle (1), Position-Matrix (9)
        data = struct.unpack('fffffffffffffffffffffffffffffff', bytes)
        self.cycle_seconds = data[0]
        self.height = data[1]
        self.height_derivative = data[2]
        self.x_rotation = (data[22], data[25], data[28])
        self.y_rotation = (data[23], data[26], data[29])
        self.z_rotation = (data[24], data[27], data[30])
        print("Accel: " + str(data[6:9]))
        #print("Axis / Angle:" + str(data[17:21]))

    @property
    def cycle_seconds(self):
        return self.__cycle_seconds

    @cycle_seconds.setter
    def cycle_seconds(self, cycle_seconds):
        self.__cycle_seconds = cycle_seconds

    @property
    def x_rotation(self):
        return self.__x

    @x_rotation.setter
    def x_rotation(self, x):
        self.__x = x

    @property
    def y_rotation(self):
        return self.__y

    @y_rotation.setter
    def y_rotation(self, y):
        self.__y = y

    @property
    def z_rotation(self):
        return self.__z

    @z_rotation.setter
    def z_rotation(self, z):
        self.__z = z

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height
