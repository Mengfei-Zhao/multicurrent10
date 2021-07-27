
from PyQt5.QtWidgets import QMessageBox, QInputDialog, QFileDialog
from operateExcelFile import OperateExcelFile
from operateFile import OperateFile
from constants import PARAM_INIT_FILE_WHEN_START_PROGRAM


class GUI_File(object):
    """the class of operating file in GUI 
    """

    def gf_init(self):
        """initialize the file handle of GUI
        """
        self.OpExlFile = OperateExcelFile()
        self.OpFile = OperateFile()

    def gf_saveEnteredParamIntoAnInitFile(self):
        """save the parameters into a file
        """
        fileName, ok = QInputDialog.getText(
            self, 'Input', "Please enter the file name:")
        if ok:
            fileName = self.OpExlFile.getFileNameWithType(fileName)
            absFilePath = self.OpExlFile.getPathOfResultsFile(fileName)
            sheetName = 'sheet1'
            # Set the title
            title = [['Channel', 'Alias',
                      'SetCurrent(mA)', 'Voltage(V)', 'Photodiode(uA)'], ]
            self.OpExlFile.writeToExcelFile(absFilePath, sheetName, title)
            self.ggp_updateGetParam()  # update all the parameters in the GUI
            data = [
                ['1', self.cha1_alias, self.cha1_setCurr,
                    self.cha1_volt, self.cha1_pd],
                ['2', self.cha2_alias, self.cha2_setCurr,
                    self.cha2_volt, self.cha2_pd],
                ['3', self.cha3_alias, self.cha3_setCurr,
                    self.cha3_volt, self.cha3_pd],
                ['4', self.cha4_alias, self.cha4_setCurr,
                    self.cha4_volt, self.cha4_pd],
                ['5', self.cha5_alias, self.cha5_setCurr,
                    self.cha5_volt, self.cha5_pd],
                ['6', self.cha6_alias, self.cha6_setCurr,
                    self.cha6_volt, self.cha6_pd],
                ['7', self.cha7_alias, self.cha7_setCurr,
                    self.cha7_volt, self.cha7_pd],
                ['8', self.cha8_alias, self.cha8_setCurr,
                    self.cha8_volt, self.cha8_pd],
                ['9', self.cha9_alias, self.cha9_setCurr,
                    self.cha9_volt, self.cha9_pd],
                ['10', self.cha10_alias, self.cha10_setCurr,
                    self.cha10_volt, self.cha10_pd],
            ]
            self.OpExlFile.appendToExcelFile(absFilePath, sheetName, data)
            QMessageBox.information(self, 'Message', 'Save successfully.')
        else:
            pass

    def gf_loadParamIntoGuiFromFile(self):
        """Load parameters into GUI from a specified Excel file
        """
        if self.GUI_INIT_FLAG == True:
            fileName = PARAM_INIT_FILE_WHEN_START_PROGRAM
            absFileName = self.OpExlFile.getPathOfParamFile(
                fileName)  # the return is absolute path of file
            self.GUI_INIT_FLAG = False
            dataInFile = self.OpExlFile.readoutDataFromExcelFile(
                absFileName)  # other input parameters are default
            self.glp_loadParam(dataInFile)
        else:
            try:
                fileName, _ = self.gf_chooseAnExcelFile(
                    'Please choose a file containing initialization parameters: ')
                absFileName = self.OpExlFile.getPathOfParamFile(fileName)
                dataInFile = self.OpExlFile.readoutDataFromExcelFile(
                    absFileName)  # other input parameters are default
                self.glp_loadParam(dataInFile)
            except FileNotFoundError:
                pass

    def gf_chooseAnExcelFile(self, windowTip='Please choose a file:'):
        """choose an excel file to save data.

        Args: 
            windowTip (str): the tip on the top of the dialog.
        Return: fileName (str): the file name.
                filePathWithoutFileName (str): the file path without file name.
        """
        fileSel = QFileDialog.getOpenFileName(
            self, windowTip, '', 'Excel files(*.xlsx , *.xls)')  # file selected
        absolutePath = fileSel[0]  # 将第一个元素（即绝对路径）取出来
        absolutePath = absolutePath.split('/')  # 将absolutePath按照/切分
        # 假设切分后有n部分，将前n-1部分用/重新拼接，就是文件的路径
        filePathWithoutFileName = "/".join(absolutePath[0:len(absolutePath)-1])
        # print('filePathWithoutFileName is :', filePathWithoutFileName)
        fileName = absolutePath[len(
            absolutePath)-1]  # 最后一个就是文件名
        return fileName, filePathWithoutFileName

    def gf_openDocumentation(self):
        """open the documentation.
        """
        self.OpFile.openDocumentation('documentation.md')
