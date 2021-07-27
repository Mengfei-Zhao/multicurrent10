

class GUI_GetParam(object):
    """the class of getting the parameters of GUI, and then I can save them to a file.
    """
    def ggp_updateGetParam(self):
        """update all the parameters in the GUI.
        """
        self.ggp_getEnteredAlias()
        self.ggp_getEnteredSetCurrent()
        self.ggp_getVolt()
        self.ggp_getPd()

    def ggp_getEnteredAlias(self):
        """get the entered alias
        """
        self.cha1_alias = self.lineEdit.text()
        self.cha2_alias = self.lineEdit_2.text()
        self.cha3_alias = self.lineEdit_3.text()
        self.cha4_alias = self.lineEdit_4.text()
        self.cha5_alias = self.lineEdit_5.text()
        self.cha6_alias = self.lineEdit_6.text()
        self.cha7_alias = self.lineEdit_7.text()
        self.cha8_alias = self.lineEdit_8.text()
        self.cha9_alias = self.lineEdit_9.text()
        self.cha10_alias = self.lineEdit_10.text()
        # print('cha1_alias is:', self.ch1_alias)

    def ggp_getEnteredSetCurrent(self):
        """get the value of entered SetCurrent"""
        self.cha1_setCurr = self.doubleSpinBox.cleanText()
        self.cha2_setCurr = self.doubleSpinBox_2.cleanText()
        self.cha3_setCurr = self.doubleSpinBox_3.cleanText()
        self.cha4_setCurr = self.doubleSpinBox_4.cleanText()
        self.cha5_setCurr = self.doubleSpinBox_5.cleanText()
        self.cha6_setCurr = self.doubleSpinBox_6.cleanText()
        self.cha7_setCurr = self.doubleSpinBox_7.cleanText()
        self.cha8_setCurr = self.doubleSpinBox_8.cleanText()
        self.cha9_setCurr = self.doubleSpinBox_9.cleanText()
        self.cha10_setCurr = self.doubleSpinBox_10.cleanText()
        # print('cha1_setCurr is:', self.cha1_setCurr)

    def ggp_getVolt(self):
        """get the value of voltage.
        """
        self.cha1_volt = self.textBrowser.toPlainText()[:-2]
        self.cha2_volt = self.textBrowser_2.toPlainText()[:-2]
        self.cha3_volt = self.textBrowser_3.toPlainText()[:-2]
        self.cha4_volt = self.textBrowser_4.toPlainText()[:-2]
        self.cha5_volt = self.textBrowser_5.toPlainText()[:-2]
        self.cha6_volt = self.textBrowser_6.toPlainText()[:-2]
        self.cha7_volt = self.textBrowser_7.toPlainText()[:-2]
        self.cha8_volt = self.textBrowser_8.toPlainText()[:-2]
        self.cha9_volt = self.textBrowser_9.toPlainText()[:-2]
        self.cha10_volt = self.textBrowser_10.toPlainText()[:-2]

    def ggp_getPd(self):
        """get the value of photodiode.
        """
        self.cha1_pd = self.textBrowser_11.toPlainText()[:-2]
        self.cha2_pd = self.textBrowser_12.toPlainText()[:-2]
        self.cha3_pd = self.textBrowser_13.toPlainText()[:-2]
        self.cha4_pd = self.textBrowser_14.toPlainText()[:-2]
        self.cha5_pd = self.textBrowser_15.toPlainText()[:-2]
        self.cha6_pd = self.textBrowser_16.toPlainText()[:-2]
        self.cha7_pd = self.textBrowser_17.toPlainText()[:-2]
        self.cha8_pd = self.textBrowser_18.toPlainText()[:-2]
        self.cha9_pd = self.textBrowser_19.toPlainText()[:-2]
        self.cha10_pd = self.textBrowser_20.toPlainText()[:-2]
