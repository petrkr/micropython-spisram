# Low level driver for I2C FRAM MB85RC256V
# Note: version 47C16 and 47L16 are different only by supply voltage

# Copyright (c) 2022 Petr Kracik

from sram.frammb85rcxxx import FRAMMB85RCXXX

class FRAMMB85RC256V(FRAMMB85RCXXX):
    def __init__(self, i2c, address = 0x50):
        super().__init__(i2c, address)
        self._size = 32*1024  # 0x0000 - 0x7FFF
