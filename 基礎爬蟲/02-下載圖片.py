import requests as req
url = "https://i.insider.com/602ee9ced3ad27001837f2ac?width=1000&format=jpeg&auto=webp"
r = req.get(url)

#儲存照片、影片、檔案時，圖片為二進制
#儲存檔案，依照檔案類型更改檔案名稱的後綴
#wb = 寫出檔案   rb = 讀取檔案
#而最後一行的 .content 就是將剛剛我們open出來的內容顯示出來
with open("檔案名稱.jpg", mode = "wb")as file:
    file.write(r.content)
