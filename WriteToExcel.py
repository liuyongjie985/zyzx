# coding:utf-8
import csv
import xlsxwriter

workbook = xlsxwriter.Workbook('output/result.xlsx')

worksheet = workbook.add_worksheet()
worksheet.set_column("A:A", 20)


def writeExcel(row=0, position='开发阶段', city='工作地点'):
    if row == 0:
        worksheet.write(row, 0, position)
        worksheet.write(row, 1, city)
    else:
        worksheet.write(row, 0, out[0])
        worksheet.write(row, 1, out[1])


f = open("output/result_out")

sign = 0
out = []
row = 0
while 1:
    lines = f.readlines(100000)
    if not lines:
        break
    for line in lines:
        if line.strip() == "":
            continue

        out.append(line.decode('utf-8'))
        if len(out) == 2:
            writeExcel(row=row, position=out[0], city=out[1])
            out = []
            row += 1

workbook.close()
print row
