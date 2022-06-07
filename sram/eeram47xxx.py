# Low level driver for I2C EERAM 47xxx family
# Copyright (c) 2022 Petr Kracik

from sram import SRAM

class EERAM47XXX(SRAM):
    STATUS_REGISTER = 0x00
    STATUS_ASE_BIT = 0x02

    def __init__(self, i2c, address=0x18):
        super().__init__()
        self._i2c = i2c
        self._addrcontrol = address & 0x18 | 0x08  # set bits 1010XX0
        self._addrsram = address & 0x56 | 0x40  # set bits 0011XX0


    def _read(self, address, count):
        return self._i2c.readfrom_mem(self._addrsram, address, count, addrsize=16)
    

    def _write(self, address, data):
        self._i2c.writeto_mem(self._addrsram, address, data, addrsize=16)


    @property
    def auto_store(self):
        return self._i2c.readfrom_mem(self._addrcontrol, self.STATUS_REGISTER, 1)[0] & self.STATUS_ASE_BIT == self.STATUS_ASE_BIT


    @auto_store.setter
    def auto_store(self, store):
        reg = self._i2c.readfrom_mem(self._addrcontrol, self.STATUS_REGISTER, 1)[0]
        tmp = bytearray(1)
        tmp[0] = reg
        if store:
            tmp[0] |= self.STATUS_ASE_BIT  # Set ASE
        else:
            tmp[0] &= ~(self.STATUS_ASE_BIT)  # Clear ASE

        self._i2c.writeto_mem(self._addrcontrol, self.STATUS_REGISTER, tmp)
