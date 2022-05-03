# Driver for SPI Serial SRAM
# Copyright (c) 2022 Petr Kracik

__version__ = "0.0.1"
__license__ = "MIT"
__author__ = "Petr Kracik"


class SRAM:
    def __init__(self):
        pass


    def read(self, address, count = 1):
        raise NotImplementedError()


    def write(self, data, address, check=True):
        raise NotImplementedError()

