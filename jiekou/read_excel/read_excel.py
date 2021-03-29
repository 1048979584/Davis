import xlrd

class ExcelUtil(object):
    def __init__(self, excelPath, sheetName):
        #读取对象和表
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        # get titles
        self.row = self.table.row_values(0)
        # get rows number
        self.rowNum = self.table.nrows
        # get columns number
        self.colNum = self.table.ncols
        # the current column
        self.curRowNo = 1

    def next(self):
        r = []
        while self.hasNext():
            s = {}
            #获取每一行的值
            col = self.table.row_values(self.curRowNo)
            #总列数
            i = self.colNum
            for x in range(i):
            #创建字典，标题为键，内容为值
                s[self.row[x]] = col[x]
            r.append(s)
            self.curRowNo += 1
        return r


    def hasNext(self):
        if self.rowNum == 0 or self.rowNum <= self.curRowNo:
            return False
        else:
            return True


if __name__ == '__main__':
    excel = ExcelUtil("D:\\phthon\\SLEQ\\jiekou\\common\\jiekou.xlsx", 'Sheet1')
    data = excel.next()

