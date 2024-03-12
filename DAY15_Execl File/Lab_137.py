# Creating and writing in a shhet

from openpyxl import Workbook
wb= Workbook()
wb['Sheet'].title ="Name of SDE"
sh1 = wb.active
sh1['A1'].value ="Name"
sh1['B1'].value = "Status"
#wb.save("final_report.xlsx")
wb.save("C:\\Users\\Welcome\\Desktop\\Demo1.xlsx")
