import struct

class Flydata():

    def __init__(self, bytes):
        data = struct.unpack('ffffffffff', bytes)
        print (data)
        self.x_rotation = (data[0], data[3], data[6])
        self.y_rotation = (data[1], data[4], data[7])
        self.z_rotation = (data[2], data[5], data[8])
        self.height = data[9]

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
