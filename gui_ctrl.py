import time
from constants import SWITCH_OFF_TAIL_DELAY
from constants import DEFAULT_VOLT_TEXT, DEFAULT_PD_TEXT


class GUI_Ctrl(object):
    """Contains the methods that have control function.
    The prefix of following methods 'gc_' means GUI_Ctrl, which is the class /
        name.
    """

    def gc_init(self):
        self.gc_setCurrEnterFinishEvent()
        self.gc_setSwitchChangeEvent()
        self.gc_menuBarEvent()

# ---- Event ---------------------------------------------------
    def gc_setCurrEnterFinishEvent(self):
        """when the SetCurrent is enter finished, I will run gc_setCurrent_cha 
            function.
        """
        self.doubleSpinBox.editingFinished.connect(self.gc_setCurrentCha1)
        self.doubleSpinBox_2.editingFinished.connect(self.gc_setCurrentCha2)
        self.doubleSpinBox_3.editingFinished.connect(self.gc_setCurrentCha3)
        self.doubleSpinBox_4.editingFinished.connect(self.gc_setCurrentCha4)
        self.doubleSpinBox_5.editingFinished.connect(self.gc_setCurrentCha5)
        self.doubleSpinBox_6.editingFinished.connect(self.gc_setCurrentCha6)
        self.doubleSpinBox_7.editingFinished.connect(self.gc_setCurrentCha7)
        self.doubleSpinBox_8.editingFinished.connect(self.gc_setCurrentCha8)
        self.doubleSpinBox_9.editingFinished.connect(self.gc_setCurrentCha9)
        self.doubleSpinBox_10.editingFinished.connect(self.gc_setCurrentCha10)

    def gc_setSwitchChangeEvent(self):
        """when the On-Off switch changes, I will run gc_setOnOffCha function.
        """
        self.radioButton.toggled.connect(self.gc_setOnOffCha1)
        self.radioButton_3.toggled.connect(self.gc_setOnOffCha2)
        self.radioButton_5.toggled.connect(self.gc_setOnOffCha3)
        self.radioButton_7.toggled.connect(self.gc_setOnOffCha4)
        self.radioButton_9.toggled.connect(self.gc_setOnOffCha5)
        self.radioButton_11.toggled.connect(self.gc_setOnOffCha6)
        self.radioButton_13.toggled.connect(self.gc_setOnOffCha7)
        self.radioButton_15.toggled.connect(self.gc_setOnOffCha8)
        self.radioButton_17.toggled.connect(self.gc_setOnOffCha9)
        self.radioButton_19.toggled.connect(self.gc_setOnOffCha10)
        self.radioButton_31.toggled.connect(self.gc_setOnOffChaTotal)

    # Menu bar
    def gc_menuBarEvent(self):
        # File
        self.actionSave_entered_param_into_an_init_file.triggered.connect(
            self.gf_saveEnteredParamIntoAnInitFile)
        self.actionLoad_param_into_GUI_from_the_init_file.triggered.connect(
            self.gf_loadParamIntoGuiFromFile)
        # Setting
        self.actionSet_max_current_for_channels.triggered.connect(
            self.gi_showSubWin_setMaxCurrForCha)
        # this signal is connected to two event
        self.subWinSMCFC.OKButton.clicked.connect(self._gi_updateMaxCurr)
        self.actionReconnect_to_multicurrent10.triggered.connect(
            self.gi_restartProgram)
        self.actionInfo_of_connection.triggered.connect(
            self.gi_showInfoOfConnection)
        # Help
        self.actionDocumentation.triggered.connect(
            self.gf_openDocumentation)
        self.actionProduct_web_site.triggered.connect(
            self.gi_openProductWebSite)


# ---- gc_setCurrentCha ---------------------------------------------------


    def gc_setCurrentCha1(self):
        """load the setting current to device
        """
        self.ch1_setCurrent = self.doubleSpinBox.cleanText()
        self.multi.set_current_source(self.ch1_setCurrent, 1)

    def gc_setCurrentCha2(self):
        """load the setting current to device
        """
        self.ch2_setCurrent = self.doubleSpinBox_2.cleanText()
        self.multi.set_current_source(self.ch2_setCurrent, 2)

    def gc_setCurrentCha3(self):
        """load the setting current to device
        """
        self.ch3_setCurrent = self.doubleSpinBox_3.cleanText()
        self.multi.set_current_source(self.ch3_setCurrent, 3)

    def gc_setCurrentCha4(self):
        """load the setting current to device
        """
        self.ch4_setCurrent = self.doubleSpinBox_4.cleanText()
        self.multi.set_current_source(self.ch4_setCurrent, 4)

    def gc_setCurrentCha5(self):
        """load the setting current to device
        """
        self.ch5_setCurrent = self.doubleSpinBox_5.cleanText()
        self.multi.set_current_source(self.ch5_setCurrent, 5)

    def gc_setCurrentCha6(self):
        """load the setting current to device
        """
        self.ch6_setCurrent = self.doubleSpinBox_6.cleanText()
        self.multi.set_current_source(self.ch6_setCurrent, 6)

    def gc_setCurrentCha7(self):
        """load the setting current to device
        """
        self.ch7_setCurrent = self.doubleSpinBox_7.cleanText()
        self.multi.set_current_source(self.ch7_setCurrent, 7)

    def gc_setCurrentCha8(self):
        """load the setting current to device
        """
        self.ch8_setCurrent = self.doubleSpinBox_8.cleanText()
        self.multi.set_current_source(self.ch8_setCurrent, 8)

    def gc_setCurrentCha9(self):
        """load the setting current to device
        """
        self.ch9_setCurrent = self.doubleSpinBox_9.cleanText()
        self.multi.set_current_source(self.ch9_setCurrent, 9)

    def gc_setCurrentCha10(self):
        """load the setting current to device
        """
        self.ch10_setCurrent = self.doubleSpinBox_10.cleanText()
        self.multi.set_current_source(self.ch10_setCurrent, 10)

# ---- gc_setOnOffCha ------------------------------------------------------
    def gc_setOnOffCha1(self):
        """set the switch state of channel 1
        """
        if self.radioButton.isChecked() == True and \
                self.radioButton_2.isChecked() == False:
            self.multi.turn_off_source(1)
            self.CHA1 = 'OFF'
            time.sleep(SWITCH_OFF_TAIL_DELAY)
            self.textBrowser.setText(DEFAULT_VOLT_TEXT)
            self.textBrowser_11.setText(DEFAULT_PD_TEXT)
        elif self.radioButton.isChecked() == False and \
                self.radioButton_2.isChecked() == True:
            self.multi.turn_on_source(1)
            self.CHA1 = 'ON'

    def gc_setOnOffCha2(self):
        """set the switch state of channel 2
        """
        if self.radioButton_3.isChecked() == True and \
                self.radioButton_4.isChecked() == False:
            self.multi.turn_off_source(2)
            self.CHA2 = 'OFF'
            time.sleep(SWITCH_OFF_TAIL_DELAY)
            self.textBrowser_2.setText(DEFAULT_VOLT_TEXT)
            self.textBrowser_12.setText(DEFAULT_PD_TEXT)
        elif self.radioButton_3.isChecked() == False and \
                self.radioButton_4.isChecked() == True:
            self.multi.turn_on_source(2)
            self.CHA2 = 'ON'

    def gc_setOnOffCha3(self):
        """set the switch state of channel 3
        """
        if self.radioButton_5.isChecked() == True and \
                self.radioButton_6.isChecked() == False:
            self.multi.turn_off_source(3)
            self.CHA3 = 'OFF'
            time.sleep(SWITCH_OFF_TAIL_DELAY)
            self.textBrowser_3.setText(DEFAULT_VOLT_TEXT)
            self.textBrowser_13.setText(DEFAULT_PD_TEXT)
        elif self.radioButton_5.isChecked() == False and \
                self.radioButton_6.isChecked() == True:
            self.multi.turn_on_source(3)
            self.CHA3 = 'ON'

    def gc_setOnOffCha4(self):
        """set the switch state of channel 4
        """
        if self.radioButton_7.isChecked() == True and \
                self.radioButton_8.isChecked() == False:
            self.multi.turn_off_source(4)
            self.CHA4 = 'OFF'
            time.sleep(SWITCH_OFF_TAIL_DELAY)
            self.textBrowser_4.setText(DEFAULT_VOLT_TEXT)
            self.textBrowser_14.setText(DEFAULT_PD_TEXT)
        elif self.radioButton_7.isChecked() == False and \
                self.radioButton_8.isChecked() == True:
            self.multi.turn_on_source(4)
            self.CHA4 = 'ON'

    def gc_setOnOffCha5(self):
        """set the switch state of channel 5
        """
        if self.radioButton_9.isChecked() == True and \
                self.radioButton_10.isChecked() == False:
            self.multi.turn_off_source(5)
            self.CHA5 = 'OFF'
            time.sleep(SWITCH_OFF_TAIL_DELAY)
            self.textBrowser_5.setText(DEFAULT_VOLT_TEXT)
            self.textBrowser_15.setText(DEFAULT_PD_TEXT)
        elif self.radioButton_9.isChecked() == False and \
                self.radioButton_10.isChecked() == True:
            self.multi.turn_on_source(5)
            self.CHA5 = 'ON'

    def gc_setOnOffCha6(self):
        """set the switch state of channel 6
        """
        if self.radioButton_11.isChecked() == True and \
                self.radioButton_12.isChecked() == False:
            self.multi.turn_off_source(6)
            self.CHA6 = 'OFF'
            time.sleep(SWITCH_OFF_TAIL_DELAY)
            self.textBrowser_6.setText(DEFAULT_VOLT_TEXT)
            self.textBrowser_16.setText(DEFAULT_PD_TEXT)
        elif self.radioButton_11.isChecked() == False and \
                self.radioButton_12.isChecked() == True:
            self.multi.turn_on_source(6)
            self.CHA6 = 'ON'

    def gc_setOnOffCha7(self):
        """set the switch state of channel 7
        """
        if self.radioButton_13.isChecked() == True and \
                self.radioButton_14.isChecked() == False:
            self.multi.turn_off_source(7)
            self.CHA7 = 'OFF'
            time.sleep(SWITCH_OFF_TAIL_DELAY)
            self.textBrowser_7.setText(DEFAULT_VOLT_TEXT)
            self.textBrowser_17.setText(DEFAULT_PD_TEXT)
        elif self.radioButton_13.isChecked() == False and \
                self.radioButton_14.isChecked() == True:
            self.multi.turn_on_source(7)
            self.CHA7 = 'ON'

    def gc_setOnOffCha8(self):
        """set the switch state of channel 8
        """
        if self.radioButton_15.isChecked() == True and \
                self.radioButton_16.isChecked() == False:
            self.multi.turn_off_source(8)
            self.CHA8 = 'OFF'
            time.sleep(SWITCH_OFF_TAIL_DELAY)
            self.textBrowser_8.setText(DEFAULT_VOLT_TEXT)
            self.textBrowser_18.setText(DEFAULT_PD_TEXT)
        elif self.radioButton_15.isChecked() == False and \
                self.radioButton_16.isChecked() == True:
            self.multi.turn_on_source(8)
            self.CHA8 = 'ON'

    def gc_setOnOffCha9(self):
        """set the switch state of channel 9
        """
        if self.radioButton_17.isChecked() == True and \
                self.radioButton_18.isChecked() == False:
            self.multi.turn_off_source(9)
            self.CHA9 = 'OFF'
            time.sleep(SWITCH_OFF_TAIL_DELAY)
            self.textBrowser_9.setText(DEFAULT_VOLT_TEXT)
            self.textBrowser_19.setText(DEFAULT_PD_TEXT)
        elif self.radioButton_17.isChecked() == False and \
                self.radioButton_18.isChecked() == True:
            self.multi.turn_on_source(9)
            self.CHA9 = 'ON'

    def gc_setOnOffCha10(self):
        """set the switch state of channel 10
        """
        if self.radioButton_19.isChecked() == True and \
                self.radioButton_20.isChecked() == False:
            self.multi.turn_off_source(10)
            self.CHA10 = 'OFF'
            time.sleep(SWITCH_OFF_TAIL_DELAY)
            self.textBrowser_10.setText(DEFAULT_VOLT_TEXT)
            self.textBrowser_20.setText(DEFAULT_PD_TEXT)
        elif self.radioButton_19.isChecked() == False and \
                self.radioButton_20.isChecked() == True:
            self.multi.turn_on_source(10)
            self.CHA10 = 'ON'

    def gc_setOnOffChaTotal(self):
        """set the switch state of all 10 channels at the time.
        """
        if self.radioButton_31.isChecked() == True and \
                self.radioButton_32.isChecked() == False:
            self._gc_setAllRadioButtonsState('OFF')
        elif self.radioButton_31.isChecked() == False and \
                self.radioButton_32.isChecked() == True:
            self._gc_setAllRadioButtonsState('ON')

    def _gc_setAllRadioButtonsState(self, switchCtrlWord):
        """set all radioButtons on.

        Args:
            switchCtrlWord (str): 'OFF', 'ON'
        """
        if switchCtrlWord == 'OFF':
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
        elif switchCtrlWord == 'ON':
            self.radioButton.setChecked(False)
            self.radioButton_2.setChecked(True)
            self.radioButton_3.setChecked(False)
            self.radioButton_4.setChecked(True)
            self.radioButton_5.setChecked(False)
            self.radioButton_6.setChecked(True)
            self.radioButton_7.setChecked(False)
            self.radioButton_8.setChecked(True)
            self.radioButton_9.setChecked(False)
            self.radioButton_10.setChecked(True)
            self.radioButton_11.setChecked(False)
            self.radioButton_12.setChecked(True)
            self.radioButton_13.setChecked(False)
            self.radioButton_14.setChecked(True)
            self.radioButton_15.setChecked(False)
            self.radioButton_16.setChecked(True)
            self.radioButton_17.setChecked(False)
            self.radioButton_18.setChecked(True)
            self.radioButton_19.setChecked(False)
            self.radioButton_20.setChecked(True)

    # def _gc_allChaShowDefaultVoltAndPd(self):
    #     """all channels all show the default voltage and photodiode at the \
    #         time.
    #     """
    #     # voltage
    #     self.textBrowser.setText(DEFAULT_VOLT_TEXT)
    #     self.textBrowser_2.setText(DEFAULT_VOLT_TEXT)
    #     self.textBrowser_3.setText(DEFAULT_VOLT_TEXT)
    #     self.textBrowser_4.setText(DEFAULT_VOLT_TEXT)
    #     self.textBrowser_5.setText(DEFAULT_VOLT_TEXT)
    #     self.textBrowser_6.setText(DEFAULT_VOLT_TEXT)
    #     self.textBrowser_7.setText(DEFAULT_VOLT_TEXT)
    #     self.textBrowser_8.setText(DEFAULT_VOLT_TEXT)
    #     self.textBrowser_9.setText(DEFAULT_VOLT_TEXT)
    #     self.textBrowser_10.setText(DEFAULT_VOLT_TEXT)

    #     # photodiode
    #     self.textBrowser_11.setText(DEFAULT_PD_TEXT)
    #     self.textBrowser_12.setText(DEFAULT_PD_TEXT)
    #     self.textBrowser_13.setText(DEFAULT_PD_TEXT)
    #     self.textBrowser_14.setText(DEFAULT_PD_TEXT)
    #     self.textBrowser_15.setText(DEFAULT_PD_TEXT)
    #     self.textBrowser_16.setText(DEFAULT_PD_TEXT)
    #     self.textBrowser_17.setText(DEFAULT_PD_TEXT)
    #     self.textBrowser_18.setText(DEFAULT_PD_TEXT)
    #     self.textBrowser_19.setText(DEFAULT_PD_TEXT)
    #     self.textBrowser_20.setText(DEFAULT_PD_TEXT)

    # def _gc_setSwitchCtrlWordOfAllCha(self, switchCtrlWord):
    #     """set the switch control word of all channels at a same time.

    #     Args:
    #         switchCtrlWord (str): 'OFF', 'ON'
    #     """
    #     if switchCtrlWord == 'OFF':
    #         self.CHA1 = 'OFF'
    #         self.CHA2 = 'OFF'
    #         self.CHA3 = 'OFF'
    #         self.CHA4 = 'OFF'
    #         self.CHA5 = 'OFF'
    #         self.CHA6 = 'OFF'
    #         self.CHA7 = 'OFF'
    #         self.CHA8 = 'OFF'
    #         self.CHA9 = 'OFF'
    #         self.CHA10 = 'OFF'
    #     elif switchCtrlWord == 'ON':
    #         self.CHA1 = 'ON'
    #         self.CHA2 = 'ON'
    #         self.CHA3 = 'ON'
    #         self.CHA4 = 'ON'
    #         self.CHA5 = 'ON'
    #         self.CHA6 = 'ON'
    #         self.CHA7 = 'ON'
    #         self.CHA8 = 'ON'
    #         self.CHA9 = 'ON'
    #         self.CHA10 = 'ON'
