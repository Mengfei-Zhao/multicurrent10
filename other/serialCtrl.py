# -*- coding: utf-8 -*-

import serial
import time


ser = serial.Serial('COM6')
ser.write('y'.encode())
print('Multicurrent created')
time.sleep(1)
# cmd = 'a_' + str(1) + '\n'
# ser.write(cmd.encode())
# print('cmd done')

# time.sleep(3)
cmd = "b\n"
ser.write(cmd.encode())
print('cmd done')

time.sleep(1)
cmd = "d\n"
ser.write(cmd.encode())
print('cmd done')
# ser.write('a_1\n')
# print(read_voltage(1))
