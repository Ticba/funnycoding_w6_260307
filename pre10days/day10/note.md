# 劇本？ AI 輔助

# 場景有幾個？

# 每個場景發生了什麼事情？

# 玩家可以選擇的對話有什麼？

-> 文章回答、條列式回答（分點分項）

Ans: 舞台劇

格式 1 ：我知道你.....。我覺得你的第一個場景.......，這個場景可以有什麼腳色.....，


格式 2 ：
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

idle, running, jumping 對應到的概念是劇本的「場景」
