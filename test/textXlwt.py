"""
@Project ：_爬虫 
@File    ：textXlwt.py
@IDE     ：PyCharm 
@Author  ：lbw
@Date    ：2023/05/23 18:28 
"""
import xlwt
# 创建work对象
workbook = xlwt.Workbook(encoding="utf-8")
worksheet = workbook.add_sheet('sheet1')
worksheet.write(0,0,'hello')
workbook.save('index.xls')
