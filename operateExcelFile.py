# coding=UTF-8
import xlrd
import xlwt
from xlutils.copy import copy
import numpy as np
import os

# * 注意：当要修改excel的格式时，write_excel_xls和write_excel_xls_append两个
# * 函数都要加入格式的设置，因为，当第二次对文件操作时，第一次的格式会消失。
# * 还有一种方式，就是最后再写入标题即可。


class OperateExcelFile:
    """This is class of operating excel files
    """

    def getDirPathOfThisFile(self):
        """get the directory path of this file.

        Return: 
            workDir\
        """
        dirPathOfThisFile = os.getcwd()
        # print('dirPathOfThisFile is', dirPathOfThisFile)
        return dirPathOfThisFile

    def getPathOfParamFile(self, fileName):
        """get the path of param_init file.

        Args: 
            fileName: such as 1.xls
        Return:
            pathOfParamFile (str): the path of param_init file, such as workDir\param_init\1.xls
        """
        pathOfParamFile = os.path.join(
            self.getDirPathOfThisFile(), "results", fileName)
        # print('pathOfParamFile is', pathOfParamFile)
        return pathOfParamFile

    def getPathOfResultsFile(self, fileName):
        """get the path of results file.

        Return:
            pathOfResultsFile (str): the path of result file, such as workDir\results\1.xls
        """
        pathOfResultsFile = os.path.join(
            self.getDirPathOfThisFile(), "results", fileName)
        # print('pathOfResultsFile is', pathOfResultsFile)
        return pathOfResultsFile

    def createANewExcelFile(self, fileName):
        """create a new excel file.

        Param: fileName [str]; such as result.xls
        Return: None
        """
        newExcel = xlwt.Workbook()
        newExcel.add_sheet('sheet1')  # 在工作簿中新建一个表格
        newExcel.save(fileName)

    def createANewExcelFile_WithTitleHead(self, fileName, titleHead):
        """create a new excel file with title head.

        Args:
            fileName (str): such as results.xls
            sheetName (str): such as sheet1 sheet2
            titleHead (list): the first row of a results.xls
        """
        self.writeToExcelFile(fileName, 'sheet1', titleHead)

    def getFileNameWithType(self, fileName):
        """Get a file name of a specified file

        Param: fileName [str]; such as result
        Return: fileNameWithType [str]; such as result.xls
        """
        fileNameWithType = fileName + '.xls'
        return fileNameWithType

    def writeToExcelFile(self, fileName, sheetName, value):
        """
        功能：往指定的excel文件中写入数据，第一行标题行会加粗，并将列宽设置为合适的宽度
        参数介绍：
            fileName: 指定的excel文件名，字符串
            sheetName: 指定的sheet名，字符串
            value: 要写入的内容
            example: 
                book_name_xls = 'xls格式测试工作簿.xls'
                sheetName_xls = 'xls格式测试表'
                value1 = [["张三", "男", "19", "杭州", "研发工程师"],
                        ["李四", "男", "22", "北京", "医生"],
                        ["王五", "女", "33", "珠海", "出租车司机"],]
        """
        index = len(value)  # 获取需要写入数据的行数
        workbook = xlwt.Workbook()  # 新建一个工作簿
        sheet = workbook.add_sheet(sheetName)  # 在工作簿中新建一个表格
        ezxf = xlwt.easyxf
        heading_xf = ezxf(
            'font: bold on; align: wrap on, vert centre, horiz center')  # 更改第一行标题的样式

        # 往sheet中写入标题
        for j in range(0, len(value[0])):
            sheet.write(0, j, value[0][j], heading_xf)

        # 往sheet中写入数据
        for i in range(1, index):  # i递增时，代表从第0行到第index-1行，代表行的下移
            for j in range(0, len(value[i])):  # j递增是，代表列的右移
                sheet.write(i, j, value[i][j])  # 像表格中写入数据（对应的行和列）

        # 设置列宽
        for j in range(0, len(value[0])):
            sheet.col(j).width = 256*20
        workbook.save(fileName)  # 保存工作簿
        # print('Write data into .xls file successfully!')

    def appendToExcelFile(self, fileName, sheetName, value):
        """
        功能：往指定的excel文件中指定的sheet中追加写入数据，并将列宽设置为合适的宽度。会保留指定的文档的格式。
        """
        index = len(value)  # 获取需要写入数据的行数
        workbook = xlrd.open_workbook(
            fileName, formatting_info=True)  # 打开工作簿，并复制原来的格式到新的book中
        # sheets = workbook.sheetNames()  # 获取工作簿中的所有表格
        worksheet = workbook.sheet_by_name(sheetName)  # 获取工作簿中指定的sheet
        rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
        new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
        new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
        for i in range(0, index):
            for j in range(0, len(value[i])):
                # 追加写入数据，注意是从i+rows_old行开始写入
                new_worksheet.write(i+rows_old, j, value[i][j])

        # 设置列宽
        for j in range(0, len(value[0])):
            new_worksheet.col(j).width = 256*20
        new_workbook.save(fileName)  # 保存工作簿
        # print('Append data into .xls file successfully!')

    def readoutDataFromExcelFile(self, fileName='result.xls', sheetName='sheet1'):
        """Readout data from an excel file

        Args:
            fileName ([str])
            sheetName ([str]) 
            rowNum ([int]) row that you wanna readout
        Return: 
            dataList ([list]) the readout data
        """
        workbook = xlrd.open_workbook(fileName)  # 打开工作簿
        worksheet = workbook.sheet_by_name(sheetName)  # 获取工作簿中指定的sheet
        dataList = []
        for j in range(0, worksheet.ncols):
            for i in range(0, worksheet.nrows):
                dataList.append(worksheet.cell_value(i, j))
        # print('dataList: ', dataList) 
        return dataList


if __name__ == '__main__':
    OpExlFile = OperateExcelFile()
    OpExlFile.getDirPathOfThisFile()
    file = OpExlFile.getPathOfResultsFile('2.xls')
    titleHead = [['Num', 'Comment', 'FreqOfClk(GHz)', 'AmpOfClk(dBm)', 'Ib1(mA)', 'Ib2(mA)',
                         'Ib3(mA)', 'Ib4(mA)', 'Ibout(mA)', 'Target BER',
                  'Best BER', 'Error compared with setting', 'NumOfIter',
                  'Test times of BER', 'Running time of algorithm(seconds)'], ]
    OpExlFile.createANewExcelFile_WithTitleHead(file, titleHead)
