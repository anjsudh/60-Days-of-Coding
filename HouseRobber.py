from typing import List

def rob(nums: List[int]) -> int:
    if len(nums) == 0 :
        return 0
    soltn = [num for num in nums]
    if(len(nums) > 2):
        soltn[2] = soltn[0] + nums[2]
        for i in range(3, len(nums)):
            soltn[i] = max(soltn[i-2], soltn[i-3]) + nums[i]
    return max(soltn)

print("Input: ", [1,2,3,1], " Solution: ", rob([1,2,3,1]))
print("Input: ", [2,7,9,3,1], " Solution: ", rob([2,7,9,3,1]))