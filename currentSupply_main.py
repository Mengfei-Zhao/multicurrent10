# --------------------------------------------------------------
# Author: Zhao Mengfei
# Date: 2021-06-25 15:00:48
# LastEditTime: 2021-07-19 15:00:52
# LastEditors: Zhao Mengfei
# Description: This file is the top file which contains GUI and my codes
# FilePath:
# --------------------------------------------------------------


import sys
import threading
import time
# PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QButtonGroup, QMainWindow, \
    QMessageBox, QInputDialog, QFileDialog
from serial import serial_for_url
from Ui_win import Ui_MainWindow
from gui_init import GUI_Init
from multicurrent10 import Multicurrent10
# from dataInterface import DataInterface
from serialPortRxDataParser import SerialPortRxDataParser



class MyMainWin(QMainWindow, Ui_MainWindow, GUI_Init):
    """The class that control GUI window"""

    def __init__(self, multi, parent=None):
        super(MyMainWin, self).__init__(parent)
        self.multi = multi
        self.serialPortRxDataParser = SerialPortRxDataParser(multi)
        self.initGUI()
        # self.DI = DataInterface()
        # self.multi = self.DI.multi
        # self.init_multicurrent10_dev()
        # self.readDataFromSerialPort_thread()
        # multicurrent program interface
        # self.getEnteredSetCurrent()
        # print(self.ch1_setCurrent)

        # self.setWindowIcon(QtGui.QIcon("icon/brain.ico"))
        # self.showPhoto() # show photo in GUI

        # self.OpExlFile = OperateExcelFile()
        # self.OpFile = OperateFile()
        # self.fileNameForResults = 'None'
        # # used for counting the clicked times of Save button
        # self.saveButtonClickedTimes = 1
        # self.initFigureWidgets()  # initialize a figure in the GroupBox of \
        # the GUI
        # self.loadParamIntoGuiFromFile(guiInitFlag='True')

        # Push button
        # self.lineEdit.clicked.connect(
        #     self.runAlgorithm)
# ------- My initialization setting ------------------------------------

    def initGUI(self):
        """initialize the GUI
        """
        self.CHA1 = 'OFF'
        self.CHA2 = 'OFF'
        self.CHA3 = 'OFF'
        # self.CHA1 = 'OFF'
        # self.CHA1 = 'OFF'
        # self.CHA1 = 'OFF'
        # self.CHA1 = 'OFF'
        # self.CHA1 = 'OFF'
        # self.CHA1 = 'OFF'
        # self.CHA1 = 'OFF'
        self.setupUi(self)  # initialize the windows
        self.setFixedSize(self.width(), self.height()
                          )  # fix the size of window

        self.addUnitForSetCurrent()  # add a unit(mA) for SetCurrent
        self.setRadioButtonGroup()
        self.gi_setDefaultSwitchState()
        self.readData_freshTime = 5000  # ms
        self.SWITCH_OFF_TAIL_DELAY = 0.1  # seconds

        self.setCurrEnterFinish_event()
        self.setSwitchChange_event()
        time.sleep(0.5)
        self.readData_backend_start()

    def setCurrEnterFinish_event(self):
        """when the SetCurrent is enter finished, I will run setCurrent_cha \
            function.
        """
        self.doubleSpinBox.editingFinished.connect(self.setCurrent_cha1)
        self.doubleSpinBox_2.editingFinished.connect(self.setCurrent_cha2)
        self.doubleSpinBox_3.editingFinished.connect(self.setCurrent_cha3)
        self.doubleSpinBox_4.editingFinished.connect(self.setCurrent_cha4)
        self.doubleSpinBox_5.editingFinished.connect(self.setCurrent_cha5)
        self.doubleSpinBox_6.editingFinished.connect(self.setCurrent_cha6)
        self.doubleSpinBox_7.editingFinished.connect(self.setCurrent_cha7)
        self.doubleSpinBox_8.editingFinished.connect(self.setCurrent_cha8)
        self.doubleSpinBox_9.editingFinished.connect(self.setCurrent_cha9)
        self.doubleSpinBox_10.editingFinished.connect(self.setCurrent_cha10)

    def setSwitchChange_event(self):
        """when the On-Off switch changes, I will run setOnOff_cha function.
        """
        self.radioButton.toggled.connect(self.setOnOff_cha1)
        self.radioButton_3.toggled.connect(self.setOnOff_cha2)
        self.radioButton_5.toggled.connect(self.setOnOff_cha3)
        self.radioButton_7.toggled.connect(self.setOnOff_cha4)
        self.radioButton_9.toggled.connect(self.setOnOff_cha5)
        self.radioButton_11.toggled.connect(self.setOnOff_cha6)
        self.radioButton_13.toggled.connect(self.setOnOff_cha7)
        self.radioButton_15.toggled.connect(self.setOnOff_cha8)
        self.radioButton_17.toggled.connect(self.setOnOff_cha9)
        self.radioButton_19.toggled.connect(self.setOnOff_cha10)

    def setRadioButtonGroup(self):
        """to deal with the group of radio button
        """
        bg_cha1 = QButtonGroup(self)
        bg_cha1.addButton(self.radioButton)
        bg_cha1.addButton(self.radioButton_2)

        bg_cha2 = QButtonGroup(self)
        bg_cha2.addButton(self.radioButton_3)
        bg_cha2.addButton(self.radioButton_4)

        bg_cha3 = QButtonGroup(self)
        bg_cha3.addButton(self.radioButton_5)
        bg_cha3.addButton(self.radioButton_6)

        bg_cha4 = QButtonGroup(self)
        bg_cha4.addButton(self.radioButton_7)
        bg_cha4.addButton(self.radioButton_8)

        bg_cha5 = QButtonGroup(self)
        bg_cha5.addButton(self.radioButton_9)
        bg_cha5.addButton(self.radioButton_10)

        bg_cha6 = QButtonGroup(self)
        bg_cha6.addButton(self.radioButton_11)
        bg_cha6.addButton(self.radioButton_12)

        bg_cha7 = QButtonGroup(self)
        bg_cha7.addButton(self.radioButton_13)
        bg_cha7.addButton(self.radioButton_14)

        bg_cha8 = QButtonGroup(self)
        bg_cha8.addButton(self.radioButton_15)
        bg_cha8.addButton(self.radioButton_16)

        bg_cha9 = QButtonGroup(self)
        bg_cha9.addButton(self.radioButton_17)
        bg_cha9.addButton(self.radioButton_18)

        bg_cha10 = QButtonGroup(self)
        bg_cha10.addButton(self.radioButton_19)
        bg_cha10.addButton(self.radioButton_20)

    # def set_default_switch_state(self):
    #     """set the default state of the On-Off switch
    #     """
    #     self.radioButton.setChecked(True)  # default is off
    #     self.radioButton_2.setChecked(False)
    #     self.radioButton_3.setChecked(True)  # default is off
    #     self.radioButton_4.setChecked(False)
    #     self.radioButton_5.setChecked(True)  # default is off
    #     self.radioButton_6.setChecked(False)
    #     self.radioButton_7.setChecked(True)  # default is off
    #     self.radioButton_8.setChecked(False)
    #     self.radioButton_9.setChecked(True)  # default is off
    #     self.radioButton_10.setChecked(False)
    #     self.radioButton_11.setChecked(True)  # default is off
    #     self.radioButton_12.setChecked(False)
    #     self.radioButton_13.setChecked(True)  # default is off
    #     self.radioButton_14.setChecked(False)
    #     self.radioButton_15.setChecked(True)  # default is off
    #     self.radioButton_16.setChecked(False)
    #     self.radioButton_17.setChecked(True)  # default is off
    #     self.radioButton_18.setChecked(False)
    #     self.radioButton_19.setChecked(True)  # default is off
    #     self.radioButton_20.setChecked(False)

    # def init_multicurrent10_dev(self):
    #     """initialize the serial port and device
    #     """
    #     try:
    #         self.multi = multi
    #         # self.multi.open_serial_port('COM6')
    #         time.sleep(0.5)
    #     except AttributeError:
    #         QMessageBox.error(self, 'Error', 'The serial port is occupied!')
        # QMessageBox.information(
        #     self, 'Message', 'Multicurrent10 has been connected successfully.  ')
# ------- Set showing format --------------------------------------------

    def addUnitForSetCurrent(self):
        mA = ' mA'
        self.doubleSpinBox.setSuffix(mA)
        self.doubleSpinBox_2.setSuffix(mA)
        self.doubleSpinBox_3.setSuffix(mA)
        self.doubleSpinBox_4.setSuffix(mA)
        self.doubleSpinBox_5.setSuffix(mA)
        self.doubleSpinBox_6.setSuffix(mA)
        self.doubleSpinBox_7.setSuffix(mA)
        self.doubleSpinBox_8.setSuffix(mA)
        self.doubleSpinBox_9.setSuffix(mA)
        self.doubleSpinBox_10.setSuffix(mA)

# ------- Set param for device -----------------------------------------------------
    def getEnteredAlias(self):
        """get the entered alias
        """
        self.ch1_alias = self.lineEdit.text()
        self.ch2_alias = self.lineEdit_2.text()
        self.ch3_alias = self.lineEdit_3.text()
        self.ch4_alias = self.lineEdit_4.text()
        self.ch5_alias = self.lineEdit_5.text()
        self.ch6_alias = self.lineEdit_6.text()
        self.ch7_alias = self.lineEdit_7.text()
        self.ch8_alias = self.lineEdit_8.text()
        self.ch9_alias = self.lineEdit_9.text()
        self.ch10_alias = self.lineEdit_10.text()

    # def getEnteredSetCurrent(self):
    #     """get the entered set current
    #     """

    #     self.ch2_setCurrent = self.doubleSpinBox_2.cleanText()
    #     self.ch3_setCurrent = self.doubleSpinBox_3.cleanText()
    #     self.ch4_setCurrent = self.doubleSpinBox_4.cleanText()
    #     self.ch5_setCurrent = self.doubleSpinBox_5.cleanText()
    #     self.ch6_setCurrent = self.doubleSpinBox_6.cleanText()
    #     self.ch7_setCurrent = self.doubleSpinBox_7.cleanText()
    #     self.ch8_setCurrent = self.doubleSpinBox_8.cleanText()
    #     self.ch9_setCurrent = self.doubleSpinBox_9.cleanText()
    #     self.ch10_setCurrent = self.doubleSpinBox_10.cleanText()
# ---   setCurrent_cha---------------------------------------------
    def setCurrent_cha1(self):
        """load the setting current to device
        """
        self.ch1_setCurrent = self.doubleSpinBox.cleanText()
        self.multi.set_current_source(self.ch1_setCurrent, 1)

    def setCurrent_cha2(self):
        """load the setting current to device
        """
        self.ch2_setCurrent = self.doubleSpinBox_2.cleanText()
        self.multi.set_current_source(self.ch2_setCurrent, 2)

    def setCurrent_cha3(self):
        """load the setting current to device
        """
        self.ch3_setCurrent = self.doubleSpinBox_3.cleanText()
        self.multi.set_current_source(self.ch3_setCurrent, 3)

    def setCurrent_cha4(self):
        """load the setting current to device
        """
        self.ch4_setCurrent = self.doubleSpinBox_4.cleanText()
        self.multi.set_current_source(self.ch4_setCurrent, 4)

    def setCurrent_cha5(self):
        """load the setting current to device
        """
        self.ch5_setCurrent = self.doubleSpinBox_5.cleanText()
        self.multi.set_current_source(self.ch5_setCurrent, 5)

    def setCurrent_cha6(self):
        """load the setting current to device
        """
        self.ch6_setCurrent = self.doubleSpinBox_6.cleanText()
        self.multi.set_current_source(self.ch6_setCurrent, 6)

    def setCurrent_cha7(self):
        """load the setting current to device
        """
        self.ch7_setCurrent = self.doubleSpinBox_7.cleanText()
        self.multi.set_current_source(self.ch7_setCurrent, 7)

    def setCurrent_cha8(self):
        """load the setting current to device
        """
        self.ch8_setCurrent = self.doubleSpinBox_8.cleanText()
        self.multi.set_current_source(self.ch8_setCurrent, 8)

    def setCurrent_cha9(self):
        """load the setting current to device
        """
        self.ch9_setCurrent = self.doubleSpinBox_9.cleanText()
        self.multi.set_current_source(self.ch9_setCurrent, 9)

    def setCurrent_cha10(self):
        """load the setting current to device
        """
        self.ch10_setCurrent = self.doubleSpinBox_10.cleanText()
        self.multi.set_current_source(self.ch10_setCurrent, 10)


# ---- setOnOff_cha --------------------------------------------------------------------------


    def setOnOff_cha1(self):
        """set the switch state of channel 1
        """
        if self.radioButton.isChecked() == True and self.radioButton_2.isChecked() == False:
            self.multi.turn_off_source(1)
            self.CH1 = 'OFF'
            # self.readData_backend_stop()
            time.sleep(self.SWITCH_OFF_TAIL_DELAY)
            self.textBrowser.setText(
                str('%.4f' % 0.0000)+' V')  # the default state
            print('cha1 is off, and voltage is 0')
            # self.readData_backend_stop()
            # self.readData_thread
        elif self.radioButton.isChecked() == False and self.radioButton_2.isChecked() == True:
            self.multi.turn_on_source(1)

            self.CHA1 = 'ON'
            # self.readData_backend_start()
            # self.readData_backend_start()
            # self.readData_thread = threading.Thread(
            # target=self.multi.read_voltage(1), name="readData_thread")
            # self.readData_thread.setDaemon(True)  # 当主线程结束后，该子线程也结束
            # self.readData_thread.start()
            # self.readVoltCha1()

    def setOnOff_cha2(self):
        """set the switch state of channel 2
        """
        if self.radioButton_3.isChecked() == True and self.radioButton_4.isChecked() == False:
            self.multi.turn_off_source(2)
            # self.readData2_backend_stop()
            # self.readData_backend_stop()
            # self.CHA2 = 'OFF'
            time.sleep(self.SWITCH_OFF_TAIL_DELAY)
            self.textBrowser_2.setText(
                str('%.4f' % 0.0000)+' V')  # the default state
        elif self.radioButton_3.isChecked() == False and self.radioButton_4.isChecked() == True:
            self.multi.turn_on_source(2)
            # self.readData_backend_start()
            self.CHA2 = 'ON'
            # self.readData2_backend_start()
            # self.readVoltCha2()

    def setOnOff_cha3(self):
        """set the switch state of channel 3
        """
        if self.radioButton_5.isChecked() == True and self.radioButton_6.isChecked() == False:
            self.multi.turn_off_source(3)
            # self.readData3_backend_stop()
            # self.readData_backend_stop()
            # self.CHA3 = 'OFF'
            time.sleep(self.SWITCH_OFF_TAIL_DELAY)
            self.textBrowser_3.setText(
                str('%.4f' % 0.0000)+' V')  # the default state
        elif self.radioButton_5.isChecked() == False and self.radioButton_6.isChecked() == True:
            self.multi.turn_on_source(3)
            # self.readData_backend_start()
            self.CHA3 = 'ON'
            # self.readData3_backend_start()
            # self.readVoltCha3()

    def setOnOff_cha4(self):
        """set the switch state of channel 4
        """
        if self.radioButton_7.isChecked() == True and self.radioButton_8.isChecked() == False:
            self.multi.turn_off_source(4)
            # self.readDataCha4_backend_stop()
        elif self.radioButton_7.isChecked() == False and self.radioButton_8.isChecked() == True:
            self.multi.turn_on_source(4)
            # self.readDataCha4_backend_start()

    def setOnOff_cha5(self):
        """set the switch state of channel 5
        """
        if self.radioButton_9.isChecked() == True and self.radioButton_10.isChecked() == False:
            self.multi.turn_off_source(5)
            self.readDataCha5_backend_stop()
        elif self.radioButton_9.isChecked() == False and self.radioButton_10.isChecked() == True:
            self.multi.turn_on_source(5)
            self.readDataCha5_backend_start()

    def setOnOff_cha6(self):
        """set the switch state of channel 6
        """
        if self.radioButton_11.isChecked() == True and self.radioButton_12.isChecked() == False:
            self.multi.turn_off_source(6)
            self.readDataCha6_backend_stop()
        elif self.radioButton_11.isChecked() == False and self.radioButton_12.isChecked() == True:
            self.multi.turn_on_source(6)
            self.readDataCha6_backend_start()

    def setOnOff_cha7(self):
        """set the switch state of channel 7
        """
        if self.radioButton_13.isChecked() == True and self.radioButton_14.isChecked() == False:
            self.multi.turn_off_source(7)
            self.readDataCha7_backend_stop()
        elif self.radioButton_13.isChecked() == False and self.radioButton_14.isChecked() == True:
            self.multi.turn_on_source(7)
            self.readDataCha7_backend_start()

    def setOnOff_cha8(self):
        """set the switch state of channel 8
        """
        if self.radioButton_15.isChecked() == True and self.radioButton_16.isChecked() == False:
            self.multi.turn_off_source(8)
            self.readDataCha8_backend_stop()
        elif self.radioButton_15.isChecked() == False and self.radioButton_16.isChecked() == True:
            self.multi.turn_on_source(8)
            self.readDataCha8_backend_start()

    def setOnOff_cha9(self):
        """set the switch state of channel 9
        """
        if self.radioButton_17.isChecked() == True and self.radioButton_18.isChecked() == False:
            self.multi.turn_off_source(9)
            self.readDataCha9_backend_stop()
        elif self.radioButton_17.isChecked() == False and self.radioButton_18.isChecked() == True:
            self.multi.turn_on_source(9)
            self.readDataCha9_backend_start()

    def setOnOff_cha10(self):
        """set the switch state of channel 10
        """
        if self.radioButton_19.isChecked() == True and self.radioButton_20.isChecked() == False:
            self.multi.turn_off_source(10)
            self.readDataCha10_backend_stop()
        elif self.radioButton_19.isChecked() == False and self.radioButton_20.isChecked() == True:
            self.multi.turn_on_source(10)
            self.readDataCha10_backend_start()

    def prepareVoltAndPd(self):
        # if self.CHA1 == 'OFF':
        #     self.textBrowser.setText(
        #         str('%.4f' % 0.0000)+' V')  # the default state
        #     print('cha1 is off, and voltage is 0')
        # if self.CHA2 == 'OFF':
        #     self.textBrowser_2.setText(
        #         str('%.4f' % 0.0000)+' V')  # the default state
        # if self.CHA3 == 'OFF':
        #     self.textBrowser_3.setText(
        #         str('%.4f' % 0.0000)+' V')  # the default state
        physicalName, cha, value = self.serialPortRxDataParser.rxDataParser
        if physicalName == 'volt':
            if cha == 1 and self.CHA1 == 'ON':
                self.textBrowser.setText(str('%.4f' % value)+' V')
                print('cha1 voltage is set')
            # else:
            #     self.textBrowser.setText(
            #     str('%.4f' % 0.0000)+' V')  # the default state
            elif cha == 2 and self.CHA2 == 'ON':
                self.textBrowser_2.setText(str('%.4f' % value)+' V')
            # else:
            #     self.textBrowser_2.setText(
            #     str('%.4f' % 0.0000)+' V')  # the default state
            elif cha == 3 and self.CHA3 == 'ON':
                self.textBrowser_3.setText(str('%.4f' % value)+' V')
            else:
                pass
            # else:
            #     self.textBrowser_3.setText(
            #     str('%.4f' % 0.0000)+' V')  # the default state
        # else:
        #     self.textBrowser.setText(
        #         str('%.4f' % 0.0000)+' V')  # the default state
        #     self.textBrowser_2.setText(
        #         str('%.4f' % 0.0000)+' V')  # the default state
        #     self.textBrowser_3.setText(
        #         str('%.4f' % 0.0000)+' V')  # the default state

        # elif physicalName == 'pd':
        #     if cha == 1:
        #         self.textBrowser_11.setText(str('%.2f' % value)+' uA')
        #     elif cha == 2:
        #         self.textBrowser_12.setText(str('%.2f' % value)+' uA')
        #     elif cha == 3:
        #         self.textBrowser_13.setText(str('%.2f' % value)+' uA')
        #     else:
        #         pass
        # else:
        #     pass

    def readData_backend_start(self):
        """backend that reading data from device 
        """
        self.readData_timer = QtCore.QTimer()
        self.readData_timer.interval = self.readData_freshTime
        self.readData_timer.timeout.connect(self.prepareVoltAndPd)
        # self.readData_timer.setInterval = 5000
        self.readData_timer.start()

    # def readData2_backend_start(self):
    #     """backend that reading data from device
    #     """
    #     self.readData2_timer = QtCore.QTimer()
    #     self.readData2_timer.interval = self.readData_freshTime
    #     self.readData2_timer.timeout.connect(self.prepareVoltAndPd)
    #     # self.readData_timer.setInterval = 5000
    #     self.readData2_timer.start()

    # def readData3_backend_start(self):
    #     """backend that reading data from device
    #     """
    #     self.readData3_timer = QtCore.QTimer()
    #     self.readData3_timer.interval = self.readData_freshTime
    #     self.readData3_timer.timeout.connect(self.prepareVoltAndPd)
    #     # self.readData_timer.setInterval = 5000
    #     self.readData3_timer.start()

    # def readData_backend_stop(self):
    #     """stop the backend that reading data from device
    #     """
    #     self.readData_timer.stop()
        # self.textBrowser.setText(
        #         str('%.4f' % 0.0000)+' V')  # the default state

    # def readData2_backend_stop(self):
    #     """stop the backend that reading data from device
    #     """
    #     self.readData2_timer.stop()
    #     self.textBrowser_2.setText(
    #             str('%.4f' % 0.0000)+' V')  # the default state
    # def readData3_backend_stop(self):
    #     """stop the backend that reading data from device
    #     """
    #     self.readData3_timer.stop()
    #     self.textBrowser_3.setText(
    #             str('%.4f' % 0.0000)+' V')  # the default state
        # self.textBrowser.setText(
        #     str('%.4f' % 0.0000)+' V')  # the default state
        # self.textBrowser_11.setText(' '+str('%.2f' % 0.00)+' uA')
        # self.textBrowser_2.setText(
        #     str('%.4f' % 0.0000)+' V')  # the default state
        # self.textBrowser_12.setText(' '+str('%.2f' % 0.00)+' uA')
        # self.textBrowser_3.setText(
        #     str('%.4f' % 0.0000)+' V')  # the default state
        # self.textBrowser_13.setText(' '+str('%.2f' % 0.00)+' uA')

# ------- Read Cha1 --------------------------------------------

#     # def showVolt(self):
#     #     self.textBrowser.setText(str('%.4f' % self.multi.rdVolt)+' V')

#     def readVoltCha1(self):
#         """readback voltage from device
#         """
#         cha1_volt = self.multi.read_voltage(1)
#         self.textBrowser.setText(str('%.4f' % cha1_volt)+' V')
#         time.sleep(0.005)

#     def readPhotodiodeCurrCha1(self):
#         """readback the photodiode current from device.
#         """
#         cha1_pdCurr = self.multi.read_photodiode(1)
#         if cha1_pdCurr >= 0.00:
#             text = ' ' + str('%.2f' % cha1_pdCurr)
#         else:
#             text = str('%.2f' % cha1_pdCurr)
#         self.textBrowser_11.setText(text+' uA')

#     def readDataCha1(self):
#         """read voltage and photodiode from device.
#         """
#         self.readVoltCha1()
#         time.sleep(0.005)
#         self.readPhotodiodeCurrCha1()

#     def readDataCha1_backend_start(self):
#         """backend that reading data from device
#         """
#         self.cha1ReadData_timer = QtCore.QTimer()
#         self.cha1ReadData_timer.interval = self.readData_freshTime
#         self.cha1ReadData_timer.start()
#         self.cha1ReadData_timer.timeout.connect(self.readDataCha1)

#     def readDataCha1_backend_stop(self):
#         """stop the backend that reading data from device
#         """
#         self.cha1ReadData_timer.stop()
#         self.textBrowser.setText(
#             str('%.4f' % 0.0000)+' V')  # the default state
#         self.textBrowser_11.setText(' '+str('%.2f' % 0.00)+' uA')

#     # def readPhotodiodeCha1_backend_start(self):
#     #     """backend that reading voltage from device
#     #     """
#     #     self.cha1ReadPdCurr_timer = QtCore.QTimer()
#     #     self.cha1ReadPdCurr_timer.interval = self.readPdCurr_freshTime
#     #     self.cha1ReadPdCurr_timer.start()
#     #     self.cha1ReadPdCurr_timer.timeout.connect(self.readVoltCha1)

#     # def readPhotodiodeCha1_backend_stop(self):
#     #     """stop the backend that reading voltage from device
#     #     """
#     #     self.cha1ReadPdCurr_timer.stop()
#     #     self.textBrowser_11.setText(str('%.2f' % 0.00)+' uA') # the default state

# # ------- Read Cha2 ---------------------------

#     def readVoltCha2(self):
#         """readback voltage from device
#         """
#         cha2_volt = self.multi.read_voltage(2)
#         self.textBrowser_2.setText(str('%.4f' % cha2_volt)+' V')

#     def readPhotodiodeCurrCha2(self):
#         """readback the photodiode current from device.
#         """
#         cha2_pdCurr = self.multi.read_photodiode(2)
#         if cha2_pdCurr >= 0.00:
#             text = ' ' + str('%.2f' % cha2_pdCurr)
#         else:
#             text = str('%.2f' % cha2_pdCurr)
#         self.textBrowser_12.setText(text+' uA')

#     def readDataCha2(self):
#         """read voltage and photodiode from device.
#         """
#         self.readVoltCha2()
#         time.sleep(0.005)
#         self.readPhotodiodeCurrCha2()

#     def readDataCha2_backend_start(self):
#         """backend that reading data from device
#         """
#         self.cha2ReadData_timer = QtCore.QTimer()
#         self.cha2ReadData_timer.interval = self.readData_freshTime
#         self.cha2ReadData_timer.start()
#         self.cha2ReadData_timer.timeout.connect(self.readDataCha2)

#     def readDataCha2_backend_stop(self):
#         """stop the backend that reading data from device
#         """
#         self.cha2ReadData_timer.stop()
#         self.textBrowser.setText(
#             str('%.4f' % 0.0000)+' V')  # the default state
#         self.textBrowser_12.setText(' '+str('%.2f' % 0.00)+' uA')

# # ------- Read Cha3 ---------------------------

#     def readVoltCha3(self):
#         """readback voltage from device
#         """
#         cha3_volt = self.multi.read_voltage(3)
#         self.textBrowser_3.setText(str('%.4f' % cha3_volt)+' V')

#     def readPhotodiodeCurrCha3(self):
#         """readback the photodiode current from device.
#         """
#         cha3_pdCurr = self.multi.read_photodiode(3)
#         if cha3_pdCurr >= 0.00:
#             text = ' ' + str('%.2f' % cha3_pdCurr)
#         else:
#             text = str('%.2f' % cha3_pdCurr)
#         self.textBrowser_13.setText(text+' uA')

#     def readDataCha3(self):
#         """read voltage and photodiode from device.
#         """
#         self.readVoltCha3()
#         time.sleep(0.005)
#         self.readPhotodiodeCurrCha3()

#     def readDataCha3_backend_start(self):
#         """backend that reading data from device
#         """
#         self.cha3ReadData_timer = QtCore.QTimer()
#         self.cha3ReadData_timer.interval = self.readData_freshTime
#         self.cha3ReadData_timer.start()
#         self.cha3ReadData_timer.timeout.connect(self.readDataCha3)

#     def readDataCha3_backend_stop(self):
#         """stop the backend that reading data from device
#         """
#         self.cha3ReadData_timer.stop()
#         self.textBrowser_3.setText(
#             str('%.4f' % 0.0000)+' V')  # the default state
#         self.textBrowser_13.setText(' '+str('%.2f' % 0.00)+' uA')

# # ------- Read Cha4 ---------------------------

#     def readVoltCha4(self):
#         """readback voltage from device
#         """
#         cha4_volt = self.multi.read_voltage(4)
#         self.textBrowser_4.setText(str('%.4f' % cha4_volt)+' V')

#     def readPhotodiodeCurrCha4(self):
#         """readback the photodiode current from device.
#         """
#         cha4_pdCurr = self.multi.read_photodiode(4)
#         if cha4_pdCurr >= 0.00:
#             text = ' ' + str('%.2f' % cha4_pdCurr)
#         else:
#             text = str('%.2f' % cha4_pdCurr)
#         self.textBrowser_14.setText(text+' uA')

#     def readDataCha4(self):
#         """read voltage and photodiode from device.
#         """
#         self.readVoltCha4()
#         time.sleep(0.005)
#         self.readPhotodiodeCurrCha4()

#     def readDataCha4_backend_start(self):
#         """backend that reading data from device
#         """
#         self.cha4ReadData_timer = QtCore.QTimer()
#         self.cha4ReadData_timer.interval = self.readData_freshTime
#         self.cha4ReadData_timer.start()
#         self.cha4ReadData_timer.timeout.connect(self.readDataCha4)

#     def readDataCha4_backend_stop(self):
#         """stop the backend that reading data from device
#         """
#         self.cha4ReadData_timer.stop()
#         self.textBrowser_4.setText(
#             str('%.4f' % 0.0000)+' V')  # the default state
#         self.textBrowser_14.setText(' '+str('%.2f' % 0.00)+' uA')

# # ------- Read Cha5 ---------------------------

#     def readVoltCha5(self):
#         """readback voltage from device
#         """
#         cha5_volt = self.multi.read_voltage(5)
#         self.textBrowser_5.setText(str('%.4f' % cha5_volt)+' V')

#     def readPhotodiodeCurrCha5(self):
#         """readback the photodiode current from device.
#         """
#         cha5_pdCurr = self.multi.read_photodiode(5)
#         if cha5_pdCurr >= 0.00:
#             text = ' ' + str('%.2f' % cha5_pdCurr)
#         else:
#             text = str('%.2f' % cha5_pdCurr)
#         self.textBrowser_15.setText(text+' uA')

#     def readDataCha5(self):
#         """read voltage and photodiode from device.
#         """
#         self.readVoltCha5()
#         time.sleep(0.005)
#         self.readPhotodiodeCurrCha5()

#     def readDataCha5_backend_start(self):
#         """backend that reading data from device
#         """
#         self.cha5ReadData_timer = QtCore.QTimer()
#         self.cha5ReadData_timer.interval = self.readData_freshTime
#         self.cha5ReadData_timer.start()
#         self.cha5ReadData_timer.timeout.connect(self.readDataCha5)

#     def readDataCha5_backend_stop(self):
#         """stop the backend that reading data from device
#         """
#         self.cha5ReadData_timer.stop()
#         self.textBrowser_5.setText(
#             str('%.4f' % 0.0000)+' V')  # the default state
#         self.textBrowser_15.setText(' '+str('%.2f' % 0.00)+' uA')

# # ------- Read Cha6 ---------------------------

#     def readVoltCha6(self):
#         """readback voltage from device
#         """
#         cha6_volt = self.multi.read_voltage(6)
#         self.textBrowser_6.setText(str('%.4f' % cha6_volt)+' V')

#     def readPhotodiodeCurrCha6(self):
#         """readback the photodiode current from device.
#         """
#         cha6_pdCurr = self.multi.read_photodiode(6)
#         if cha6_pdCurr >= 0.00:
#             text = ' ' + str('%.2f' % cha6_pdCurr)
#         else:
#             text = str('%.2f' % cha6_pdCurr)
#         self.textBrowser_16.setText(text+' uA')

#     def readDataCha6(self):
#         """read voltage and photodiode from device.
#         """
#         self.readVoltCha6()
#         time.sleep(0.005)
#         self.readPhotodiodeCurrCha6()

#     def readDataCha6_backend_start(self):
#         """backend that reading data from device
#         """
#         self.cha6ReadData_timer = QtCore.QTimer()
#         self.cha6ReadData_timer.interval = self.readData_freshTime
#         self.cha6ReadData_timer.start()
#         self.cha6ReadData_timer.timeout.connect(self.readDataCha6)

#     def readDataCha6_backend_stop(self):
#         """stop the backend that reading data from device
#         """
#         self.cha6ReadData_timer.stop()
#         self.textBrowser_6.setText(
#             str('%.4f' % 0.0000)+' V')  # the default state
#         self.textBrowser_16.setText(' '+str('%.2f' % 0.00)+' uA')

# # ------- Read Cha7 ---------------------------

#     def readVoltCha7(self):
#         """readback voltage from device
#         """
#         cha7_volt = self.multi.read_voltage(7)
#         self.textBrowser_7.setText(str('%.4f' % cha7_volt)+' V')

#     def readPhotodiodeCurrCha7(self):
#         """readback the photodiode current from device.
#         """
#         cha7_pdCurr = self.multi.read_photodiode(7)
#         if cha7_pdCurr >= 0.00:
#             text = ' ' + str('%.2f' % cha7_pdCurr)
#         else:
#             text = str('%.2f' % cha7_pdCurr)
#         self.textBrowser_17.setText(text+' uA')

#     def readDataCha7(self):
#         """read voltage and photodiode from device.
#         """
#         self.readVoltCha7()
#         time.sleep(0.005)
#         self.readPhotodiodeCurrCha7()

#     def readDataCha7_backend_start(self):
#         """backend that reading data from device
#         """
#         self.cha7ReadData_timer = QtCore.QTimer()
#         self.cha7ReadData_timer.interval = self.readData_freshTime
#         self.cha7ReadData_timer.start()
#         self.cha7ReadData_timer.timeout.connect(self.readDataCha7)

#     def readDataCha7_backend_stop(self):
#         """stop the backend that reading data from device
#         """
#         self.cha7ReadData_timer.stop()
#         self.textBrowser_7.setText(
#             str('%.4f' % 0.0000)+' V')  # the default state
#         self.textBrowser_17.setText(' '+str('%.2f' % 0.00)+' uA')

# # ------- Read Cha8 ---------------------------

#     def readVoltCha8(self):
#         """readback voltage from device
#         """
#         cha8_volt = self.multi.read_voltage(8)
#         self.textBrowser_8.setText(str('%.4f' % cha8_volt)+' V')

#     def readPhotodiodeCurrCha8(self):
#         """readback the photodiode current from device.
#         """
#         cha8_pdCurr = self.multi.read_photodiode(8)
#         if cha8_pdCurr >= 0.00:
#             text = ' ' + str('%.2f' % cha8_pdCurr)
#         else:
#             text = str('%.2f' % cha8_pdCurr)
#         self.textBrowser_18.setText(text+' uA')

#     def readDataCha8(self):
#         """read voltage and photodiode from device.
#         """
#         self.readVoltCha8()
#         time.sleep(0.005)
#         self.readPhotodiodeCurrCha8()

#     def readDataCha8_backend_start(self):
#         """backend that reading data from device
#         """
#         self.cha8ReadData_timer = QtCore.QTimer()
#         self.cha8ReadData_timer.interval = self.readData_freshTime
#         self.cha8ReadData_timer.start()
#         self.cha8ReadData_timer.timeout.connect(self.readDataCha8)

#     def readDataCha8_backend_stop(self):
#         """stop the backend that reading data from device
#         """
#         self.cha8ReadData_timer.stop()
#         self.textBrowser_8.setText(
#             str('%.4f' % 0.0000)+' V')  # the default state
#         self.textBrowser_18.setText(' '+str('%.2f' % 0.00)+' uA')

# # ------- Read Cha9 ---------------------------

#     def readVoltCha9(self):
#         """readback voltage from device
#         """
#         cha9_volt = self.multi.read_voltage(9)
#         self.textBrowser_9.setText(str('%.4f' % cha9_volt)+' V')

#     def readPhotodiodeCurrCha9(self):
#         """readback the photodiode current from device.
#         """
#         cha9_pdCurr = self.multi.read_photodiode(9)
#         if cha9_pdCurr >= 0.00:
#             text = ' ' + str('%.2f' % cha9_pdCurr)
#         else:
#             text = str('%.2f' % cha9_pdCurr)
#         self.textBrowser_19.setText(text+' uA')

#     def readDataCha9(self):
#         """read voltage and photodiode from device.
#         """
#         self.readVoltCha9()
#         time.sleep(0.005)
#         self.readPhotodiodeCurrCha9()

#     def readDataCha9_backend_start(self):
#         """backend that reading data from device
#         """
#         self.cha9ReadData_timer = QtCore.QTimer()
#         self.cha9ReadData_timer.interval = self.readData_freshTime
#         self.cha9ReadData_timer.start()
#         self.cha9ReadData_timer.timeout.connect(self.readDataCha9)

#     def readDataCha9_backend_stop(self):
#         """stop the backend that reading data from device
#         """
#         self.cha9ReadData_timer.stop()
#         self.textBrowser_9.setText(
#             str('%.4f' % 0.0000)+' V')  # the default state
#         self.textBrowser_19.setText(' '+str('%.2f' % 0.00)+' uA')

# # ------- Read Cha10 ---------------------------

#     def readVoltCha10(self):
#         """readback voltage from device
#         """
#         cha10_volt = self.multi.read_voltage(10)
#         self.textBrowser_10.setText(str('%.4f' % cha10_volt)+' V')

#     def readPhotodiodeCurrCha10(self):
#         """readback the photodiode current from device.
#         """
#         cha10_pdCurr = self.multi.read_photodiode(10)
#         if cha10_pdCurr >= 0.00:
#             text = ' ' + str('%.2f' % cha10_pdCurr)
#         else:
#             text = str('%.2f' % cha10_pdCurr)
#         self.textBrowser_20.setText(text+' uA')

#     def readDataCha10(self):
#         """read voltage and photodiode from device.
#         """
#         self.readVoltCha10()
#         time.sleep(0.005)
#         self.readPhotodiodeCurrCha10()

#     def readDataCha10_backend_start(self):
#         """backend that reading data from device
#         """
#         self.cha10ReadData_timer = QtCore.QTimer()
#         self.cha10ReadData_timer.interval = self.readData_freshTime
#         self.cha10ReadData_timer.start()
#         self.cha10ReadData_timer.timeout.connect(self.readDataCha10)

#     def readDataCha10_backend_stop(self):
#         """stop the backend that reading data from device
#         """
#         self.cha10ReadData_timer.stop()
#         self.textBrowser_10.setText(
#             str('%.4f' % 0.0000)+' V')  # the default state
#         self.textBrowser_20.setText(' '+str('%.2f' % 0.00)+' uA')

# ------read data from serial port in backend-------------------
# def readDataFromSerialPort_thread(self):
#     # 开始读取串口缓存区的子线程，一直在读取数据
#     readData_thread = threading.Thread(
#         target=self.readVoltCha1, name="readData_thread")
#     readData_thread.setDaemon(True)  # 当主线程结束后，该子线程也结束
#     readData_thread.start()  # 启动该线程


def main():
    multi = Multicurrent10()
    multi.open_serial_port('COM6')
    readData_thread = threading.Thread(
        target=multi.read_serial_port_data, name="readData_thread")
    readData_thread.setDaemon(True)  # 当主线程结束后，该子线程也结束
    readData_thread.start()  # 启动该线程

    # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保\
    # 程序可以双击运行
    app = QApplication(sys.argv)

    # # 初始化
    myWin = MyMainWin(multi)
    # myWin.showMaximized()  # maximize the window

    # 显示界面
    myWin.show()

    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())


# -----------------------------------------------------------------------
if __name__ == '__main__':
    main()
