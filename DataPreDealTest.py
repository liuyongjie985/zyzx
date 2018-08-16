# coding:utf-8

import re
from openpyxl import load_workbook
import xlrd
import csv
import traceback

# result = []


# 输出
o = open("data/TestData.txt", "w")

my_list = ["./data/test.xlsx"]

for x in my_list:

    workbook = load_workbook(x)
    # booksheet = workbook.active                #获取当前活跃的sheet,默认是第一个sheet
    sheets = workbook.get_sheet_names()  # 从名称获取sheet
    booksheet = workbook.get_sheet_by_name(sheets[0])

    rows = booksheet.rows
    columns = booksheet.columns
    # 迭代所有的行
    count = 0
    for row in rows:
        count += 1
        line = [col.value for col in row]
        print line
        try:
            if len(line) == 3:
                # print line[2]
                o.write((str(line[1]).strip() + '|' + str(line[2]).strip().replace(u"\n", u"").replace(u"\r\n",
                                                                                                       u"").replace(
                    u"#", u":") + "#"))
                o.write('\n')

        except:
            traceback.print_exc()
            print line[2]
            try:
                o.write(str(line[1]).strip() + '|' + str(
                    line[2].replace(u"\n", u"").replace(u"\r\n", u"").replace(u"#", u":").encode(
                        'utf-8')).strip() + "#")
            except:
                o.write(
                    (str(line[1].encode('utf-8')).strip() + '|' + str(
                        line[2].replace(u"\n", u"").replace(u"\r\n", u"").replace(u"#", u":").encode(
                            'utf-8')).strip() + "#"))

            o.write('\n')
        try:
            if len(line) == 2:
                # print line[1]
                o.write((str(line[0]).strip() + '|' + str(line[1]).replace(u"\n", u"").replace(u"\r\n", u"").replace(
                    u"#", u":").strip() + "#"))
                o.write('\n')
        except:
            # traceback.print_exc()
            print line[1]
            try:
                o.write(
                    (str(line[0].encode('utf-8')).strip() + '|' + str(
                        line[1].replace(u"\n", u"").replace(u"\r\n", u"").replace(u"#", u":").encode(
                            'utf-8')).strip() + "#"))
            except:
                o.write(str(line[0]).encode('utf-8').strip() + '|' + str(
                    line[1].replace(u"\n", u"").replace(u"\r\n", u"").replace(u"#", u":").encode(
                        'utf-8')).strip() + "#")
            o.write('\n')
    workbook.close()

print count
o.close()
