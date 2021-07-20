# -*- coding: utf-8 -*-

from multicurrent10 import Multicurrent10
import time

multi = Multicurrent10('COM6')  # Initialize the serial port and device
time.sleep(1)

# print(multi.read_voltage(1))


multi.turn_on_source(1)
multi.set_current_source(0, 1)
time.sleep(2)

readValue = multi.read_voltage(1)
print('readValue: ', readValue, 'V')
# multi.turn_on_all()
# multi.set_current_source(10, 1)

time.sleep(2)

multi.__del__()

# multi.release_device()

# print(multi.read_voltage(1))
# print('read done')

# del multi
