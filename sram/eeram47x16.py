# Low level driver for I2C EERAM 47x16 family
# Note: version 47C16 and 47L16 are different only by supply voltage

# Copyright (c) 2022 Petr Kracik

from sram.eeram47xxx import EERAM47XXX

class EERAM47X16(EERAM47XXX):
    def __init__(self, i2c, address=0x18):
        super().__init__(i2c, address)
        self._size = 2048  # 0x0000 - 0x07FF
