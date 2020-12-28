# -*- coding = utf-8 -*-
# @Time: 2020/12/23 15:43
# @Author: 高才华
# @File: testXlwt.py
# @Software: PyCharm

import xlwt

workbook = xlwt.Workbook(encoding="utf-8")
worksheet = workbook.add_sheet("sheet1")
# worksheet.write(0,0,"我爱我的祖国")
# workbook.save("student.xls")

for i in range(0,9):
    for j in range(0,i+1):
        worksheet.write(i,j,"%d * %d = %d"%(i+1,j+1,(i+1)*(j+1)))

workbook.save("student.xls")
