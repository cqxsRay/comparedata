
import os
import xlrd
from datetime import datetime
from xlrd import xldate_as_tuple

class read_xls:
    def __init__(self, xls_name, sheet_name):
        """
        :param xls_name: 文件名
        :param sheet_name: sheet 名字
        """
        self.xls_name = xls_name
        self.sheet_name = sheet_name
        # 获取excel文件路径
        xlsPath = os.path.join(os.getcwd(), 'file',self.xls_name)
        # open xls file
        file = xlrd.open_workbook(xlsPath)
        # get sheet by name
        self.sheet = file.sheet_by_name(self.sheet_name)
        # 获取行数
        self.rows = self.sheet.nrows
        # 获取列数
        self.cols = self.sheet.ncols
        # 获取第一行作为Key
        # self.keys = self.sheet.row_values(0)
        # 针对这个excel，是取第三行
        self.keys = self.sheet.row_values(2)

    """
    按情况处理数据
    返回类型是列表中字典
    """

    def dict_xls(self):
        if self.rows <= 0:
            print("总行数小于1")
        else:
            cls = []
            # 一般excel是从第1行开始有数据
            # for i in range(1, self.rows):
            # 针对这个excel是从第4行开始有数据
            for i in range(3, self.rows):
                s = {}
                for j in range(self.cols):
                    ctype = self.sheet.cell(i, j).ctype
                    cell = self.sheet.cell(i, j).value
                    # 如果是整型
                    if ctype == 2 and cell % 1 == 0:
                        cell = int(cell)
                    # 如果是日期的类型
                    elif ctype == 3:
                        # 转成datetime对象
                        date = datetime(*xldate_as_tuple(cell, 0))
                        cell = date.strftime('%Y/%d/%m %H:%M:%S')
                    # 处理布尔类型的值
                    elif ctype == 4:
                        cell = True if cell == 1 else False
                    s[self.keys[j]] = cell
                cls.append(s)
            # 返回excel解析的数据
            return cls
# ff=read_xls('白条开新_基础信息验证_DataModel_CDS_V2.17_20190716.xlsx','信息验证输入输出报文')
# ff.dict_xls()
