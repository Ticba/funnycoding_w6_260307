# while loop (用條件來決定要不要繼續重複)
# syntax


'''
while 條件判斷式 condition expression:
    # 要縮排
    # 縮排的內容就是要重複執行的程式 ( 條件判斷為 True )

( 條件判斷為 False )
接下來的內容
'''

x = input("你的年齡是多少？（12歲以上才能使用）")
while int(x) <= 12:
    # 條件式判斷 True 才執行
    # 否則跳出迴圈
    x = input("你的年齡是多少？（12歲以上才能使用）")

print("歡迎來到此網站")