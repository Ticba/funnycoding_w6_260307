# state machine 狀態機
# total states: idle, running, jumping
# 
# idle:
#   cmd run:    -> running 
#   cmd jump:   -> jumping
#  
# running:
#   cmd stop:   -> idle
#   cmd jump:   -> jumping
#
# jumping:
#   cmd any:    -> idle



state = "idle"

while True:
    cmd = input("輸入指令 (run / jump / stop / exit): ")

    if cmd == "exit":
        break

    match state:
        case "idle":
            match cmd:
                case "run":
                    state = "running"
                    print("開始跑")
                case "jump":
                    state = "jumping"
                    print("原地跳")
                case _:
                    print("沒反應")

        case "running":
            match cmd:
                case "stop":
                    state = "idle"
                    print("停下來")
                case "jump":
                    state = "jumping"
                    print("跑步跳")
                case _:
                    print("持續跑")

        case "jumping":
            print("落地")
            state = "idle"