# --------------------------------------------------------------
# Author: Zhao Mengfei
# Date: 2021-06-25 15:00:48
# LastEditTime: 2021-07-19 15:00:52
# LastEditors: Zhao Mengfei
# Description: This file is the top file which contains GUI and my codes
# FilePath:
# --------------------------------------------------------------


from gui_showReadData import GUI_ShowReadData
from gui_ctrl import GUI_Ctrl
import sys
import threading
import time
# PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QButtonGroup, QMainWindow, \
    QMessageBox, QInputDialog, QFileDialog
from Ui_win import Ui_MainWindow
from gui_init import GUI_Init
from multicurrent10 import Multicurrent10
from serialPortRxDataParser import SerialPortRxDataParser


class MyMainWin(QMainWindow, Ui_MainWindow, GUI_Init, GUI_Ctrl, GUI_ShowReadData):
    """The class that control GUI window"""

    def __init__(self, multi, parent=None):
        super(MyMainWin, self).__init__(parent)
        self.setupUi(self)  # initialize the windows
        self.setFixedSize(self.width(), self.height()
                          )  # fix the size of window
        self.multi = multi
        self.serialPortRxDataParser = SerialPortRxDataParser(multi)
        self.gi_guiInit()  # initialize the GUI
        self.gc_setCurrEnterFinishEvent()
        self.gc_setSwitchChangeEvent()
        time.sleep(0.5)  # seconds
        self.gsrd_readDataBackendStart()

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


# ---- main function----------------------------------------------------
def main():
    multi = Multicurrent10()
    try:
        multi.open_serial_port('COM6')
    except AttributeError:
        print('[Error]: The serial port is occupied!')
    print('[Info]: Multicurrent10 has been connected successfully.')
    readData_thread = threading.Thread(
        target=multi.read_serial_port_data, name="readData_thread")
    readData_thread.setDaemon(True)  # 当主线程结束后，该子线程也结束
    readData_thread.start()  # 启动该线程

    # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，\
    # 确保程序可以双击运行
    app = QApplication(sys.argv)

    # # 初始化
    myWin = MyMainWin(multi)
    # myWin.showMaximized()  # maximize the window

    # 显示界面
    myWin.show()

    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
