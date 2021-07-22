import time
from constants import SWITCH_OFF_TAIL_DELAY


class GUI_Ctrl(object):
    """Contains the methods that have control function.
    The prefix of following methods 'gc_' means GUI_Ctrl, which is the class /name.
    """

    def gc_setCurrEnterFinishEvent(self):
        """when the SetCurrent is enter finished, I will run gc_setCurrent_cha \
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
            self.textBrowser.setText(str('%.4f' % 0.0000)+' V')
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
            self.textBrowser_2.setText(str('%.4f' % 0.0000)+' V')
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
            self.textBrowser_3.setText(str('%.4f' % 0.0000)+' V')
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
            self.textBrowser_4.setText(str('%.4f' % 0.0000)+' V')
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
            self.textBrowser_5.setText(str('%.4f' % 0.0000)+' V')
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
            self.textBrowser_6.setText(str('%.4f' % 0.0000)+' V')
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
            self.textBrowser_7.setText(str('%.4f' % 0.0000)+' V')
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
            self.textBrowser_8.setText(str('%.4f' % 0.0000)+' V')
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
            self.textBrowser_9.setText(str('%.4f' % 0.0000)+' V')
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
            self.textBrowser_10.setText(str('%.4f' % 0.0000)+' V')
        elif self.radioButton_19.isChecked() == False and \
                self.radioButton_20.isChecked() == True:
            self.multi.turn_on_source(10)
            self.CHA10 = 'ON'
