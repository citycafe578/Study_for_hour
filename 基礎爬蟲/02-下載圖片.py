import requests as req
url = "https://i.insider.com/602ee9ced3ad27001837f2ac?width=1000&format=jpeg&auto=webp"
r = req.get(url)

#儲存檔案
#儲存檔案，依照檔案類型更改檔案名稱的後綴
with open("檔案名稱.jpg", mode = "wb")as file:
    file.write(r.content)
