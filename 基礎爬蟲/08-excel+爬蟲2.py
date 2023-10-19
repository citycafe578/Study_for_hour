import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "PPT爬蟲練習"


url = "https://www.ptt.cc/bbs/index.html"
#我們要假裝自己是Google機器人才不會被伺服器擋掉
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"}
res = requests.get(url, headers = headers)
#同時我們需要使用一個叫做html.parser的HTML解析器來讀取HTML
soup = BeautifulSoup(res.text,"html.parser")
articles = soup.find_all("div", class_= "b-ent")

for i in articles:
    title = i.find("div", class_ = "board-class")
    nuser = i.find("div", class_ = "board-nuser")
    print("看板名稱:" + title.text , "  " , "點擊率:" , nuser.text)

wb.save("爬蟲及openpyxl練習.xlsx")