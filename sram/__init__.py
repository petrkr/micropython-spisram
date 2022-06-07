# Base driver for SRAM
# Copyright (c) 2022 Petr Kracik

__version__ = "0.0.1"
__license__ = "MIT"
__author__ = "Petr Kracik"


class SRAM:
    def __init__(self):
        self._size = 0


    @property
    def size(self):
        return self._size


    def _read(self, address, count):
        raise NotImplementedError()


    def _write(self, address, data):
        raise NotImplementedError()


    def read(self, address, count=1):
        if address > self.size - 1 or address < 0:
            raise ValueError("Attemped to read outside of address range (0--{})".format(self.size - 1))

        return self._read(address, count)


    def write(self, address, data, check=True):
        if address > self.size - 1 or address < 0:
            raise ValueError("Attemped to read outside of address range (0--{})".format(self.size - 1))

        self._write(address, data)

        if not check:
            return True

        return self._read(address, len(data)) == data
