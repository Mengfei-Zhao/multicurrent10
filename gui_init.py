from PyQt5 import QtGui
from PyQt5.QtWidgets import QButtonGroup, QMessageBox
import time
import webbrowser
from subWin_setMaxCurrentForCha import SubWin_SetMaxCurrentForCha

# The default state of switch
from constants import CHA1_SWITCH, CHA2_SWITCH, CHA3_SWITCH, CHA4_SWITCH, \
    CHA5_SWITCH, CHA6_SWITCH, CHA7_SWITCH, CHA8_SWITCH, CHA9_SWITCH, \
    CHA10_SWITCH, CHA_TOTAL_SWITCH
from constants import DEFAULT_MAX_CURR

from constants import LED_NONCLICKABLE


class GUI_Init(object):
    """Initialize the GUI. 
    The prefix of following methods 'gi_' means GUI_Init, which is the class /name.
    """

    def gi_guiInit(self):
        """Initialize the GUI.
        """
        self.GUI_INIT_FLAG = True
        self.GuiInitUpdateMaxCurr_Flag = True
        # self.subWinSMCFC = None  # No sub-window yet
        self.subWinSMCFC = SubWin_SetMaxCurrentForCha(
            self.multi)  # create the window of set_max_current
        self.setupUi(self)  # initialize the windows
        self._gi_modifyWin
        self._gi_setDefaultSwitchCtrlWord
        self._gi_addUnitForSetCurrent  # add a unit(mA) for SetCurrent
        self._gi_updateMaxCurr()
        self._gi_setRadioButtonGroup
        self._gi_setDefaultSwitchState
        self._gi_setDefaultStateOfLed
        self._gi_showPhoto
        self.gf_init()  # initialize the file handle of GUI
        self.gf_loadParamIntoGuiFromFile()
        self.gc_init()  # initialize the signal and slot
        time.sleep(0.5)  # seconds
        self.gsrd_readDataBackendStart()

    @property
    def _gi_modifyWin(self):
        """some modifications of the window.
        """
        self.setFixedSize(self.width(), self.height()
                          )  # fix the size of window
        self.setWindowIcon(QtGui.QIcon("icons/device.ico"))

    @property
    def _gi_showPhoto(self):
        """Show a photo in GUI.
        """
        img = QtGui.QPixmap("icons/device.jpg")
        self.label_19.setPixmap(img)

    @property
    def _gi_setDefaultSwitchState(self):
        """set the default state of the On-Off switch. 
        """
        self.radioButton.setChecked(True)  # default is off
        self.radioButton_2.setChecked(False)
        self.radioButton_3.setChecked(True)  # default is off
        self.radioButton_4.setChecked(False)
        self.radioButton_5.setChecked(True)  # default is off
        self.radioButton_6.setChecked(False)
        self.radioButton_7.setChecked(True)  # default is off
        self.radioButton_8.setChecked(False)
        self.radioButton_9.setChecked(True)  # default is off
        self.radioButton_10.setChecked(False)
        self.radioButton_11.setChecked(True)  # default is off
        self.radioButton_12.setChecked(False)
        self.radioButton_13.setChecked(True)  # default is off
        self.radioButton_14.setChecked(False)
        self.radioButton_15.setChecked(True)  # default is off
        self.radioButton_16.setChecked(False)
        self.radioButton_17.setChecked(True)  # default is off
        self.radioButton_18.setChecked(False)
        self.radioButton_19.setChecked(True)  # default is off
        self.radioButton_20.setChecked(False)
        self.radioButton_31.setChecked(True)  # the total switch
        self.radioButton_32.setChecked(False)

    @property
    def _gi_setDefaultSwitchCtrlWord(self):
        """set the default switch-ctrl-word. Such as self.CHA1 = 'OFF'
        """
        self.CHA1 = CHA1_SWITCH
        self.CHA2 = CHA2_SWITCH
        self.CHA3 = CHA3_SWITCH
        self.CHA4 = CHA4_SWITCH
        self.CHA5 = CHA5_SWITCH
        self.CHA6 = CHA6_SWITCH
        self.CHA7 = CHA7_SWITCH
        self.CHA8 = CHA8_SWITCH
        self.CHA9 = CHA9_SWITCH
        self.CHA10 = CHA10_SWITCH
        self.CHA_TOTAL = CHA_TOTAL_SWITCH

    @property
    def _gi_setRadioButtonGroup(self):
        """To deal with the group of radio button, the two radioButton in a /
        group are mutual exclusive.
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

        bg_chaTotal = QButtonGroup(self)
        bg_chaTotal.addButton(self.radioButton_31)
        bg_chaTotal.addButton(self.radioButton_32)

        # Indicating led
        bg_Led1 = QButtonGroup(self)
        bg_Led1.addButton(self.radioButton_21)
        bg_Led2 = QButtonGroup(self)
        bg_Led2.addButton(self.radioButton_22)
        bg_Led3 = QButtonGroup(self)
        bg_Led3.addButton(self.radioButton_23)
        bg_Led4 = QButtonGroup(self)
        bg_Led4.addButton(self.radioButton_24)
        bg_Led5 = QButtonGroup(self)
        bg_Led5.addButton(self.radioButton_25)
        bg_Led6 = QButtonGroup(self)
        bg_Led6.addButton(self.radioButton_26)
        bg_Led7 = QButtonGroup(self)
        bg_Led7.addButton(self.radioButton_27)
        bg_Led8 = QButtonGroup(self)
        bg_Led8.addButton(self.radioButton_28)
        bg_Led9 = QButtonGroup(self)
        bg_Led9.addButton(self.radioButton_29)
        bg_Led10 = QButtonGroup(self)
        bg_Led10.addButton(self.radioButton_30)

    @property
    def _gi_addUnitForSetCurrent(self):
        """add an unit 'mA' for the SetCurrent value.
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
    def _gi_setDefaultStateOfLed(self):
        """set the default state of LED indicator
        """
        # Make the led non clickable
        self.radioButton_21.setDisabled(LED_NONCLICKABLE)
        self.radioButton_22.setDisabled(LED_NONCLICKABLE)
        self.radioButton_23.setDisabled(LED_NONCLICKABLE)
        self.radioButton_24.setDisabled(LED_NONCLICKABLE)
        self.radioButton_25.setDisabled(LED_NONCLICKABLE)
        self.radioButton_26.setDisabled(LED_NONCLICKABLE)
        self.radioButton_27.setDisabled(LED_NONCLICKABLE)
        self.radioButton_28.setDisabled(LED_NONCLICKABLE)
        self.radioButton_29.setDisabled(LED_NONCLICKABLE)
        self.radioButton_30.setDisabled(LED_NONCLICKABLE)

    def gi_showSubWin_setMaxCurrForCha(self):
        """show the window of set max current for channels. 
            SMCFC is the acronym.
        """
        if self.subWinSMCFC is None:
            self.subWinSMCFC = SubWin_SetMaxCurrentForCha(
                self.multi)  # create the window of set_max_current
        self.subWinSMCFC.show()  # show the window

    def _gi_updateMaxCurr(self):
        """update the max currents in GUI.
        """
        if self.GuiInitUpdateMaxCurr_Flag == True:
            self.doubleSpinBox.setMaximum(DEFAULT_MAX_CURR)
            self.doubleSpinBox_2.setMaximum(DEFAULT_MAX_CURR)
            self.doubleSpinBox_3.setMaximum(DEFAULT_MAX_CURR)
            self.doubleSpinBox_4.setMaximum(DEFAULT_MAX_CURR)
            self.doubleSpinBox_5.setMaximum(DEFAULT_MAX_CURR)
            self.doubleSpinBox_6.setMaximum(DEFAULT_MAX_CURR)
            self.doubleSpinBox_7.setMaximum(DEFAULT_MAX_CURR)
            self.doubleSpinBox_8.setMaximum(DEFAULT_MAX_CURR)
            self.doubleSpinBox_9.setMaximum(DEFAULT_MAX_CURR)
            self.doubleSpinBox_10.setMaximum(DEFAULT_MAX_CURR)
            self.GuiInitUpdateMaxCurr_Flag = False
        else:
            self.doubleSpinBox.setMaximum(float(self.subWinSMCFC.cha1_maxCurr))
            self.doubleSpinBox_2.setMaximum(
                float(self.subWinSMCFC.cha2_maxCurr))
            self.doubleSpinBox_3.setMaximum(
                float(self.subWinSMCFC.cha3_maxCurr))
            self.doubleSpinBox_4.setMaximum(
                float(self.subWinSMCFC.cha4_maxCurr))
            self.doubleSpinBox_5.setMaximum(
                float(self.subWinSMCFC.cha5_maxCurr))
            self.doubleSpinBox_6.setMaximum(
                float(self.subWinSMCFC.cha6_maxCurr))
            self.doubleSpinBox_7.setMaximum(
                float(self.subWinSMCFC.cha7_maxCurr))
            self.doubleSpinBox_8.setMaximum(
                float(self.subWinSMCFC.cha8_maxCurr))
            self.doubleSpinBox_9.setMaximum(
                float(self.subWinSMCFC.cha9_maxCurr))
            self.doubleSpinBox_10.setMaximum(
                float(self.subWinSMCFC.cha10_maxCurr))

    def gi_openProductWebSite(self):
        """open the product web site
        """
        webbrowser.open('https://luzwavelabs.com/ldc-e-multicurrent10/')

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self, 'Window Close', 'Tips: Do not forget to save the result. \n \nAre you sure you want to close the window?', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            self.gsrd_readDataBackendStop()
            self.multi.is_ReadSerialPortThread_True = False
            event.accept()
            # close the serial port and release the multicurrent10 device
            self.multi.release_device()
        else:  # if click No, cancel closing the window
            event.ignore()
