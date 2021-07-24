# --------------------------------------------------------------
# Author: Zhao Mengfei
# Date: 2021-06-25 15:00:48
# LastEditTime: 2021-07-19 15:00:52
# LastEditors: Zhao Mengfei
# Description: This file is the top file which contains GUI and my codes
# FilePath:
# --------------------------------------------------------------


from gui_getParam import GUI_GetParam
from gui_file import GUI_File
from gui_showReadData import GUI_ShowReadData
from gui_ctrl import GUI_Ctrl
from gui_loadParam import GUI_LoadParam
import sys
import threading
# PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_win import Ui_MainWindow
from gui_init import GUI_Init
from multicurrent10 import Multicurrent10
from serialPortRxDataParser import SerialPortRxDataParser


class MyMainWin(QMainWindow, Ui_MainWindow, GUI_Init, GUI_Ctrl, GUI_ShowReadData, GUI_File, GUI_GetParam, GUI_LoadParam):
    """The class that control GUI window"""

    def __init__(self, multi, parent=None):
        super(MyMainWin, self).__init__(parent)
        self.multi = multi
        self.serialPortRxDataParser = SerialPortRxDataParser(multi)
        self.gi_guiInit()  # initialize the GUI

# ---- main function----------------------------------------------------


def main():
    multi = Multicurrent10()
    multi.open_serial_port('COM6')
    # print('[Info]: Multicurrent10 has been connected successfully.')
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
