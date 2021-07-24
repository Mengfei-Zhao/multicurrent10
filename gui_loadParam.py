
class GUI_LoadParam(object):
    """the class of loading parameters in file to GUI.
    """

    def glp_loadParam(self, dataInFile):
        """load parameters to GUI

        Args:
            dataInFile (list): looks like:
            ['Channel', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Alias', 'fds', 'ee', '4', '5', 'j', 'l', 'hg', 'bkh', 'jg', 'kjh', 'SetCurrent(mA)', '4.000', '0.000', '0.000', '0.000', '0.000', '0.000', '0.000', '0.000', '0.000', '0.000', 'Voltage(V)', '3.0315', '3.0321', '3.0326', '3.0330', '3.0336', '3.0465', '3.0459', '3.0444', '3.0453', '3.0454', 'Photodiode(uA)', '-0.01 ', '-0.02 ', '0.00 ', '0.01 ', '0.04 ', '0.03 ', '0.06 ', '0.03 ', '0.01 ', '0.02 ']
        """
        self._glp_loadAlias(dataInFile)
        self._glp_loadSetCurr(dataInFile)

    def _glp_loadAlias(self, dataInFile):
        """load alias to GUI.
        """
        self.lineEdit.setText(dataInFile[12])
        self.lineEdit_2.setText(dataInFile[13])
        self.lineEdit_3.setText(dataInFile[14])
        self.lineEdit_4.setText(dataInFile[15])
        self.lineEdit_5.setText(dataInFile[16])
        self.lineEdit_6.setText(dataInFile[17])
        self.lineEdit_7.setText(dataInFile[18])
        self.lineEdit_8.setText(dataInFile[19])
        self.lineEdit_9.setText(dataInFile[20])
        self.lineEdit_10.setText(dataInFile[21])

    def _glp_loadSetCurr(self, dataInFile):
        """load SetCurrent to GUI.
        """
        self.doubleSpinBox.setValue(float(dataInFile[23]))
        self.doubleSpinBox.setValue(float(dataInFile[24]))
        self.doubleSpinBox.setValue(float(dataInFile[25]))
        self.doubleSpinBox.setValue(float(dataInFile[26]))
        self.doubleSpinBox.setValue(float(dataInFile[27]))
        self.doubleSpinBox.setValue(float(dataInFile[28]))
        self.doubleSpinBox.setValue(float(dataInFile[29]))
        self.doubleSpinBox.setValue(float(dataInFile[30]))
        self.doubleSpinBox.setValue(float(dataInFile[31]))
        self.doubleSpinBox.setValue(float(dataInFile[32]))
