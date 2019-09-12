"使用第三方xlrd库读写Excel文件"
import xlrd
data = xlrd.open_workbook('./files/计算机1602班创新学分统计表.xlsx')
table1 = data.sheets()[0]  # 通过索引顺序获取第1片
table2 = data.sheet_by_index(0)  # 通过索引顺序获取第1片
table3 = data.sheet_by_name(u'Sheet1')  # 通过名称获取Sheet1片
# for i in range(table3.nrows):#按行输出
#     print(table3.row_values(i))
# li=list(table1.col_values(2))#按列输出
# s={'','学号'}
# for item in s:
#     while item in li:
#         li.remove(item)
# print(li)
print(table1.cell(4,5).value)#获取单元格