from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "創建excel檔案練習"

title = ["姓名","座號","成績"]
ws.append(title)
ws.append(["CT",1,100])
ws.append(["老劉",2,85])
ws.append(["彥字",3,92])
ws.append(["使用逗號","就可以","在原有的一行中","向右新增資料"])
wb.save("新excel檔案.xlsx")