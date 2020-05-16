from typing import List

def maxProfit(prices: List[int]) -> int:
    if len(prices) == 0:
        return 0
    min_left = None
    max_profit = 0
    for i in range(1,len(prices)):
        min_left = (
            min(min_left, prices[i-1]) 
                if min_left is not None 
                else prices[i-1])
        max_profit = max(max_profit, prices[i] - min_left)
    return max_profit

print("Input: ", [7,1,5,3,6,4], " Solution: ", maxProfit([7,1,5,3,6,4]))
print("Input: ", [7,6,4,3,1], " Solution: ", maxProfit([7,6,4,3,1]))