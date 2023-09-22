#0 輸出

#0-0 輸出時用print()
print(123)
#但是輸出文字時要用" "把文字放到裡面
print("安安阿")
#輸出的字串可以相加
print("大家好我是" + "citycafe")
print("---------------------我是分隔線---------------------")



#1 簡單的數學

#1-1 我們可以做一些簡單的加減乘除
print(111 + 222) #加法
print(999 - 123) #減法
print(11 * 1234) #乘法
print(121 / 11)  #除法
print(36 // 5)   #除法並且會扣掉小數點
print(36 % 5)    #除法求餘數
print("---------------------我是分隔線---------------------")



#2 變數

#2-1 資料型別
#2-1-1 字串(str)   字串其實就是文字的意思，要用" "框起來
print("安安我CT")
print("123456789")

#2-1-2 整數(int)   整數...就是整數
print(1)
print(1+1)

#2-1-3 浮點數(float) 只要有小數點就是浮點數!
print(1.23)
print(1.23+26.1111)
    #p.s除法的答案會自動變成浮點數
print(25/5)

#2-1-4布林值(bool)  只有兩種可能，True(正確)以及Flase(錯誤)
print(1 == 1)
print(1 == 2)
print("---------------------我是分隔線---------------------")

#2-2-1 可以把變數想成一個標籤，貼在對應的東西上
a = 11
b = 22
c = "安安阿"
d = "我是citycafe"
print(a + b)
print(c)
print(c + d)
print(a, d) #當兩個變數的資料型別相同時用 "+" 相加，否則使用 "," 

print("---------------------我是分隔線---------------------")



#3輸入

#3-1 輸入很簡單，我們要先設立一個變數，默認的資料型態會是字串(str)
a = input()
print(a)

#3-2 但有時候我們會想要輸入的東西是一個整數(int)
b = int(input())
print(b)

#3-3 input()的括號內可以放題是字元
c = int(input("請輸入一個整數"))
print(c)
print("---------------------我是分隔線---------------------")


#4判別氏

#4-1 在程式中， = 是只將A賦予一個B的意義(設立變數)，而 == 才是數學中判斷二者是否相等
a = 123
print(a == 123)

#4-2 我們可以使用if(): 函式來判斷一個條件是否被達成
a = int(input("請輸入一個整數"))
if(a > 5):
    print("這個數字比5大")

#4-3 在後面接一個else: 就可以在條件不符合時執行另一段程式
a = int(input("請輸入一個整數"))
if(a > 5):
    print("這個數字比5大")
else:
    print("這數字可能比5小")

#4-3 而elif(): 便可以在當第一個if部成立時繼續判斷
if(a > 5):
    print("這個數字比5大")
elif(a == 5):
    print("這個數字等於5")
else:
    print("這數字比5小")
print("---------------------我是分隔線---------------------")



#5 迴圈(難)

#5-1 while():迴圈  當括號內的條件符合時就會持續運作
a = 10
while(a > 0):
    print("現在 a = " , a)
    a = a-1 #其他寫法: a-- 、 a-=1

#5-2-1 for i in range(): 迴圈  自動生成一個叫做 i = 0 的變數，並且每執行一次 i 就會 +1，直到 i 等於括號內的數字為止
for i in range(10):
    print("現在 i =", i) #i執行了括號內的次數，但是是從0開始算

#5-2-2 for i in range(起始數字, 結束數字, 公差)
for i in range(50, 0, -2):
    print("現在 i =", i) 
