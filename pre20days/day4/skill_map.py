s = input() # 17 00 12 13
hh, mm = map(int, s.split()) # 把 s 用空格切開，切完之後 hh, mm 都還是 str


# syntax of map function
# map(func, *iterables)
# 把 iterables 這坨資料每一個資料拿出來，當成 func 的輸入，轉換成 func 輸出


# func 可以放 int(), float(), str() these "explicit type conversion" functions.