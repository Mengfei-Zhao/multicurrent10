# -*- coding: utf-8 -*-

""" v1.0.0 """
import time
import sys
import serial
from serial.serialutil import SerialException


class Multicurrent10:
    """This is the class about the basic operations of multicurrent10"""

    def open_serial_port(self, COM):
        """Constructor of the class. It takes as argument the serial port at \
            which Multicurrent10 is listenning.

        Args:
            COM (str): such as 'COM6'
        """
        self.ser = serial.Serial(COM)
        self.ser.write('y'.encode())
        
    def turn_on_source(self, source):
        """Turns on one source. It takes as argument an integer from 1 to 10

        Args:
            source (int): such as 1 or 6
        """
        self.ser.write(('a_' + str(source) + '\n').encode())

    def turn_on_all(self):
        """Turns on all the sources
        """
        self.ser.write(('b\n').encode())

    def turn_off_source(self, source):
        """Turns off one source. It takes as argument an integer from 1 to 10.

        Args:
            source (int): such as 1 or 6
        """
        self.ser.write(('c_' + str(source) + '\n').encode())

    def turn_off_all(self):
        """Turns off all the sources
        """
        self.ser.write(('d\n').encode())

    def set_current_source(self, current, source):
        """This method set the current provided by ONE source

        Args:
            current (float): such as 6.18
            source (int): such as 1 or 6
        """
        self.ser.write(('e_' + str(current) + '_' +
                        str(source) + '\n').encode())

    def read_serial_port_data(self):
        """read all of data from serial port
        """
        line1 = " "
        line = " "
        while self.is_ReadSerialPortThread_True:
            self.ser.flushInput()
            line1 = self.ser.readline(256)
            self.line = line1.decode()
            # print('line: ', self.line)
            # time.sleep(0.5)

    def set_max_current_source(self, max_current, source):
        """Set the maximum current that can be provided by one source.

        Args:
            max_current (float): such as 100.00
            source (int): such as 1 or 6
        """
        self.ser.write(('i_' + str(max_current) + '_' +
                        str(source) + '\n').encode())

    def calibration(self):
        """This method performs the calibration of the different sources for the adaptive power management.
        """
        self.ser.write(('9').encode())

    def set_calibration_current(self, current):
        """This method allow to use a different current for the calibration of sources. It is 100 mA by default.

        Args:
            current (float):
        """
        self.ser.write(('j' + str(current) + '\n').encode())

    def off(self):
        """This method turn off Multicurrent10. However it can still be turned on using the reset method.
        """
        self.ser.write(('z\n').encode())

    def reset(self):
        """This method resets Multicurrent10.
        """
        self.ser.write(('y\n').encode())

    def release_device(self):
        """turn off all channels and release the serial port resource
        """
        try:
            try:
                self.ser.write(('z\n').encode()) # turn off all channels
            except serial.serialutil.PortNotOpenError:
                pass 
            self.ser.close()
            print('Multicurrent10 Deleted!')
        except AttributeError as e:
            print('[info]:', e)


if __name__ == '__main__':
    multi = Multicurrent10()
    multi.open_serial_port('COM6')
    time.sleep(1)
    multi.turn_on_source(1)
    multi.turn_on_source(2)
    multi.turn_on_source(3)
    time.sleep(1)
    multi.set_current_source(0, 1)
    multi.set_current_source(0, 2)
    multi.set_current_source(0, 3)
    time.sleep(1)
    # multi.read_voltage(1)
    multi.read_serial_port_data()
    # while True:
    #     cha, volt = multi.read_voltage()
    #     print('cha: ', cha)
    #     print('volt: ', volt)
    # multi.read_voltage()
    # multi.read_voltage()
    time.sleep(2)
