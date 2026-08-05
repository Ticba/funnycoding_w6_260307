# 研究 binary search 
# 怎麼寫（定義成 function）



nums = [i for i in range(1, 10000, 2) if i % 3 != 0]

target = 500


def bs(nums, target):
    # return yes if target 在 nums 裡面
    # return no if not
    left = 0
    right = len(nums)-1

    # loop 
    while left <= right:
        mid = (left + right) // 2

        # 根據 nums[mid] 與 target 的比較結果來決定
        if target == nums[mid]:
            return True
        elif target < nums[mid]:
            right = mid - 1
        else:   # target > nums[mid]
            left = mid + 1
    return False



print(bs(nums, target))    # 呼叫 bs()