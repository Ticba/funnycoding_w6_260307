def wash_hands(step):   # step is parameter 參數
    # 你要怎麼「設計」 wash_hands 的功能
    steps_list = ['濕', '搓', '沖', '捧', '擦']
    steps_list = steps_list[step-1:]
    result = ""
    for s in steps_list:
        result += s
    
    return result


ret = wash_hands(2)       # 5 is argument 引數

print(ret)
# wash_hands(5)

# wash_hands(1)



# print(1, 2, sep='****')

def greet(name, hobby):
    print('Hello,', name)
    print('Your hobby is', hobby)

greet('Leo', 'eating')


def passed(score, threshold = 60):
    return score >= threshold   # condition -> bool

print(passed(40, threshold=30))







def main():
    # 算很難的算術
    # wash_hands()
    # .
    # .
    pass
