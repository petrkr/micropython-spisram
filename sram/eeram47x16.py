from sram.eeram47xxx import EERAM47XXX

class EERAM47X16(EERAM47XXX):
    def __init__(self, i2c, address=0x18):
        super().__init__(i2c, address)
        self._size = 2048  # 0x0000 - 0x07FF
