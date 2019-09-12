"使用xlwt第三方库写入Excel文件"
import xlwt
workbook=xlwt.Workbook(encoding='ascii')
worksheet=workbook.add_sheet('My Worksheet')#创建1片
worksheet.write(0,0,144)#写入1个数据
workbook.save('./files/Excel_Workbook.xls')#保存