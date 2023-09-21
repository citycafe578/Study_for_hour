import requests as req
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

title = ['名稱', '價格', '預購價']
ws.append(title)

header = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}


for i in range(23):
    url = "https://api.hahow.in/api/courses?limit=24&page="
    url = url + str(i)
    print(url)
    r = req.get(url, headers = header)
    print(r)
    
    request_jason = r.json()

    for data in request_jason['data']:
        course = []
        course.append(data["title"])
        course.append(data['owner']['name'])
        course.append(data["price"])
        course.append(data["preOrderedPrice"])
        ws.append(course)

wb.save("data.xlsx")