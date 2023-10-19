import requests as req
url = "https://www.bing.com/ck/a?!&&p=21c6cd912ffc9cd6JmltdHM9MTY5NzY3MzYwMCZpZ3VpZD0yYTJhOGVhYi1jM2NmLTZiNzMtMDRmNS05ZjZiYzJkZjZhOWUmaW5zaWQ9NTE3NA&ptn=3&ver=2&hsh=3&fclid=2a2a8eab-c3cf-6b73-04f5-9f6bc2df6a9e&psq=pdf+%e6%95%99%e8%82%b2&u=a1aHR0cHM6Ly93cy5tb2UuZWR1LnR3L0Rvd25sb2FkLmFzaHg_dT1DMDk5MzU4QzgxRDQ4NzZDNzI1Njk1RjIwNzBCNDY3RThCODFFRDYxNEQ3QUY0M0VGNTVGRkZGOEUzODJGNDkyMzBGQkZFQkUzRkJBNjc0MTBFM0QwODgyMzVGQ0VGRjhBMzNDQTU0QkQ2N0Q3REZEOTU3MjI5REU3RjY1OEFGQUNBMzQ3NTM5RDMyQkEyM0I5QTE0MkFBMkI3NTQ1NjU5Jm49MjYwQ0Y5OTY0MUU4MzgyQTFCRUQyM0M3MEExNEQ0MzYwRkZBMjVFRjE1OUQxQjE5Rjk2NkUxQzk4RkJDMzEzQURFNjYyMzdGODdDREY1NUMyMDAzMDk2Rjc0NzdFMEU3RDEyMUZEQkExQTA2OTc1RCZpY29uPS4ucGRm&ntb=1"
r = req.get(url)

#儲存照片、影片、檔案時，圖片為二進制
#儲存檔案，依照檔案類型更改檔案名稱的後綴
#wb = 寫出檔案   rb = 讀取檔案
#而最後一行的 .content 就是將剛剛我們open出來的內容顯示出來
with open("檔案名稱.pdf", mode = "wb")as file:
    file.write(r.content)
