input_var = input()         # 將輸入當成一行字讀入，存到input_var
var_int = int(input_var)    # 將 input_var 轉換成 int ，存到 var_int 
if var_int == 1:
    # 對的區塊(True)
    print('0')
else:
    # 錯的區塊(False)
    print('1')