from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    sum = 0
    head = 0
    tail = -1
    answer = [0,0]
    for i in range(len(nums)):
        sum += nums[i]
        tail+= 1
        if(sum == target):
            break
        if(sum > target):
            sum -= nums[head]
            head += 1

    answer = [head, tail]

    print(answer)
    return


twoSum([3,3], 6)
