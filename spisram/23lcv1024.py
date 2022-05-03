# Low level driver for SPI Serial SRAM 23LCV1024
# Copyright (c) 2022 Petr Kracik

from spisram import SRAM

class SRAM23LCV1024(SRAM):
    INSTRUCTION_READ = 0x03
    INSTRUCTION_WRITE = 0x02
    INSTRUCTION_RDMR = 0x05
    INSTRUCTION_WRMR = 0x01

    def __init__(spi, cs):
        self._spi = spi
        self._cs = cs


    def read(count = 1, address = 0):
        tmp = bytearray(4)
        tmp[0] = self.INSTRUCTION_READ
        tmp[1] = ( address >> 16 ) & 0xFF
        tmp[2] = ( address >> 8 ) & 0xFF
        tmp[3] = ( address ) & 0xFF

        self._cs.value(0)
        self._spi.write(tmp)
        data = self._spi.read(count)
        self._cs.value(1)

        return data


    def write(data, address, check=True):
        tmp = bytearray(4)
        tmp[0] = self.INSTRUCTION_READ
        tmp[1] = ( address >> 16 ) & 0xFF
        tmp[2] = ( address >> 8 ) & 0xFF
        tmp[3] = ( address ) & 0xFF

        self._cs.value(0)
        self.write(tmp)
        self.write(data)
        self._cs.value(1)

        if check:
            check = self.read(len(data), address)
            return check == data
        else:
            return True
