while True:
    try:
        s = input()         # 已經沒有行輸入會跳到 except
        print(s[::-1])
    except:
        break