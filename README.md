# micropython-ndeflib
SPI Serial SRAM library for micropython

Primary used to work with 23LCV1024 memory which support battery backup and can be used as EEPROM/Flash but with unlimited number of writes. For applications where you need offten writes.


Simple code just use default sequenatial mode and allow to read/write whole SRAM memory, in case of 23LCV1024 it's full 128kB.

Nice2have TODO:
  - IO Stream support
  - Page/Byte access modes (for example to prevent overwritting other data by buffer overflow)
  - Filesystem emulation (? - maybe if there will be IOStream, then someother lib could be used?)
