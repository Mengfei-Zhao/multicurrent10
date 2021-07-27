from Ui_subWin_setMaxCurrentForCha import Ui_setMaxCurrentForCha
from PyQt5 import QtGui
# from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

import sys
from constants import DEFAULT_MAX_CURR


class SubWin_SetMaxCurrentForCha(QMainWindow, Ui_setMaxCurrentForCha):
    """the _sw of all the methode means SubWin.
    """

    def __init__(self, multi, parent=None):
        self.multi = multi
        super(SubWin_SetMaxCurrentForCha, self).__init__(parent)
        # initialize the window
        # uic.loadUi('subWin_setMaxCurrentForCha.ui', self)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height()
                          )  # fix the size of window
        self.setWindowIcon(QtGui.QIcon("icons/device.ico"))
        self._sw_addUnitForSetMaxCurr
        self._sw_setDefaultValue
        self.OKButton.clicked.connect(self.sw_OKClicked)
        self.CancelButton.clicked.connect(self.sw_CancelClicked)

    @property
    def _sw_addUnitForSetMaxCurr(self):
        """add an unit 'mA' for the value.
        """
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

    @property
    def _sw_setDefaultValue(self):
        """set deault max value 
        """
        self.doubleSpinBox.setValue(DEFAULT_MAX_CURR)
        self.doubleSpinBox_2.setValue(DEFAULT_MAX_CURR)
        self.doubleSpinBox_3.setValue(DEFAULT_MAX_CURR)
        self.doubleSpinBox_4.setValue(DEFAULT_MAX_CURR)
        self.doubleSpinBox_5.setValue(DEFAULT_MAX_CURR)
        self.doubleSpinBox_6.setValue(DEFAULT_MAX_CURR)
        self.doubleSpinBox_7.setValue(DEFAULT_MAX_CURR)
        self.doubleSpinBox_8.setValue(DEFAULT_MAX_CURR)
        self.doubleSpinBox_9.setValue(DEFAULT_MAX_CURR)
        self.doubleSpinBox_10.setValue(DEFAULT_MAX_CURR)

    @property
    def _sw_getValueOfEnteredMaxCurr(self):
        """get the values of entered max current
        """
        self.cha1_maxCurr = self.doubleSpinBox.cleanText()
        self.cha2_maxCurr = self.doubleSpinBox_2.cleanText()
        self.cha3_maxCurr = self.doubleSpinBox_3.cleanText()
        self.cha4_maxCurr = self.doubleSpinBox_4.cleanText()
        self.cha5_maxCurr = self.doubleSpinBox_5.cleanText()
        self.cha6_maxCurr = self.doubleSpinBox_6.cleanText()
        self.cha7_maxCurr = self.doubleSpinBox_7.cleanText()
        self.cha8_maxCurr = self.doubleSpinBox_8.cleanText()
        self.cha9_maxCurr = self.doubleSpinBox_9.cleanText()
        self.cha10_maxCurr = self.doubleSpinBox_10.cleanText()

    def sw_downloadMaxCurrToDev(self):
        """download max current to device
        """
        self._sw_getValueOfEnteredMaxCurr
        self.multi.set_max_current_source(self.cha1_maxCurr, 1)
        self.multi.set_max_current_source(self.cha2_maxCurr, 2)
        self.multi.set_max_current_source(self.cha3_maxCurr, 3)
        self.multi.set_max_current_source(self.cha4_maxCurr, 4)
        self.multi.set_max_current_source(self.cha5_maxCurr, 5)
        self.multi.set_max_current_source(self.cha6_maxCurr, 6)
        self.multi.set_max_current_source(self.cha7_maxCurr, 7)
        self.multi.set_max_current_source(self.cha8_maxCurr, 8)
        self.multi.set_max_current_source(self.cha9_maxCurr, 9)
        self.multi.set_max_current_source(self.cha10_maxCurr, 10)
        QMessageBox.information(
            self, 'Message', 'The max currents of all channels have been download to device successfully.')

    def sw_OKClicked(self):
        """if OK is clicked, I will call this function
        """
        self.close()  # close this window
        self.sw_downloadMaxCurrToDev()

    def sw_CancelClicked(self):
        """if Cancel is clicked, I will call this function
        """
        self.close()  # close this window


if __name__ == '__main__':
    # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，\
    # 确保程序可以双击运行
    app = QApplication(sys.argv)
    subWin = SubWin_SetMaxCurrentForCha()
    subWin.show()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
