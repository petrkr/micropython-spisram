# Low level driver for I2C FRAM MB85RCxxx family
# Copyright (c) 2022 Petr Kracik

from sram import SRAM

class FRAMMB85RCXXX(SRAM):
    def __init__(self, i2c, address):
        super().__init__()
        self._i2c = i2c
        self._addr = address


    def _read(self, address, count):
        return self._i2c.readfrom_mem(self._addr, address, count, addrsize=16)
    

    def _write(self, address, data):
        self._i2c.writeto_mem(self._addr, address, data, addrsize=16)
