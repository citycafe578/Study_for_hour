from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "創建excel檔案練習"

wb.save("新excel檔案.xlsx")