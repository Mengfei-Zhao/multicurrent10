from PyQt5 import QtCore
from constants import VOLT_DECIMAL_DIGITS, PD_DECIMAL_DIGITS
from constants import READ_DATA_TIME_INTERVAL


class GUI_ShowReadData(object):
    """Contains the methods that show the read data.
    The prefix of following methods 'gsrd_' means GUI_ShowReadData, which is 
    the class name.
    """

    def gsrd_prepareVoltAndPd(self):
        physicalName, cha, value = self.serialPortRxDataParser.rxDataParser
        if physicalName == 'volt':
            if cha == 1 and self.CHA1 == 'ON':
                self.textBrowser.setText(str(VOLT_DECIMAL_DIGITS % value)+' V')
                # print('cha1 voltage is set')
            elif cha == 2 and self.CHA2 == 'ON':
                self.textBrowser_2.setText(
                    str(VOLT_DECIMAL_DIGITS % value)+' V')
            elif cha == 3 and self.CHA3 == 'ON':
                self.textBrowser_3.setText(
                    str(VOLT_DECIMAL_DIGITS % value)+' V')
            elif cha == 4 and self.CHA4 == 'ON':
                self.textBrowser_4.setText(
                    str(VOLT_DECIMAL_DIGITS % value)+' V')
            elif cha == 5 and self.CHA5 == 'ON':
                self.textBrowser_5.setText(
                    str(VOLT_DECIMAL_DIGITS % value)+' V')
            elif cha == 6 and self.CHA6 == 'ON':
                self.textBrowser_6.setText(
                    str(VOLT_DECIMAL_DIGITS % value)+' V')
            elif cha == 7 and self.CHA7 == 'ON':
                self.textBrowser_7.setText(
                    str(VOLT_DECIMAL_DIGITS % value)+' V')
            elif cha == 8 and self.CHA8 == 'ON':
                self.textBrowser_8.setText(
                    str(VOLT_DECIMAL_DIGITS % value)+' V')
            elif cha == 9 and self.CHA9 == 'ON':
                self.textBrowser_9.setText(
                    str(VOLT_DECIMAL_DIGITS % value)+' V')
            elif cha == 10 and self.CHA10 == 'ON':
                self.textBrowser_10.setText(
                    str(VOLT_DECIMAL_DIGITS % value)+' V')
            else:
                pass

        elif physicalName == 'pd':
            if cha == 1 and self.CHA1 == 'ON':
                self.textBrowser_11.setText(
                    str(PD_DECIMAL_DIGITS % value)+' uA')
            elif cha == 2 and self.CHA2 == 'ON':
                self.textBrowser_12.setText(
                    str(PD_DECIMAL_DIGITS % value)+' uA')
            elif cha == 3 and self.CHA3 == 'ON':
                self.textBrowser_13.setText(
                    str(PD_DECIMAL_DIGITS % value)+' uA')
            elif cha == 4 and self.CHA4 == 'ON':
                self.textBrowser_14.setText(
                    str(PD_DECIMAL_DIGITS % value)+' uA')
            elif cha == 5 and self.CHA5 == 'ON':
                self.textBrowser_15.setText(
                    str(PD_DECIMAL_DIGITS % value)+' uA')
            elif cha == 6 and self.CHA6 == 'ON':
                self.textBrowser_16.setText(
                    str(PD_DECIMAL_DIGITS % value)+' uA')
            elif cha == 7 and self.CHA7 == 'ON':
                self.textBrowser_17.setText(
                    str(PD_DECIMAL_DIGITS % value)+' uA')
            elif cha == 8 and self.CHA8 == 'ON':
                self.textBrowser_18.setText(
                    str(PD_DECIMAL_DIGITS % value)+' uA')
            elif cha == 9 and self.CHA9 == 'ON':
                self.textBrowser_19.setText(
                    str(PD_DECIMAL_DIGITS % value)+' uA')
            elif cha == 10 and self.CHA10 == 'ON':
                self.textBrowser_20.setText(
                    str(PD_DECIMAL_DIGITS % value)+' uA')
            else:
                pass
        else:
            pass

    def gsrd_readDataBackendStart(self):
        """backend that reading and parsering data from device 
        """
        self.readData_timer = QtCore.QTimer()
        self.readData_timer.interval = READ_DATA_TIME_INTERVAL
        self.readData_timer.timeout.connect(self.gsrd_prepareVoltAndPd)
        self.readData_timer.start()

    def gsrd_readDataBackendStop(self):
        """backend that reading and parsering data from device 
        """
        self.readData_timer.stop()
