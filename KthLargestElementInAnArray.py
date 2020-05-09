from typing import List

class Heap:
    def __init__(self, max_size = 0):
        self.nums = [-1 for i in range(max_size + 1)]
        self.size = 0
        self.max_size = max_size

    def add(self, num):
        self.nums[self.size] = num
        pos = self.size
        self.size += 1
        while (pos>=1):
            if (self.nums[pos] < self.nums[int(pos/2)]) :
                temp = self.nums[pos]
                self.nums[pos] = self.nums[int(pos/2)]
                self.nums[int(pos/2)] = temp
            else:
                break
            pos = int(pos/2)

    def minheap(self):
        self.nums[0] = self.nums[self.size - 1]
        self.nums[self.size - 1] = -1
        self.size -= 1
        pos = 0
        while(pos<self.size):
            new_pos = 2*pos
            if ((new_pos < self.size 
                    and self.nums[pos] > self.nums[new_pos]) 
                or  (new_pos+1 < self.size 
                        and self.nums[pos] > self.nums[new_pos+1])):
                if (new_pos+1 < self.size 
                    and self.nums[new_pos+1] < self.nums[new_pos]):
                    new_pos = new_pos+1
                temp = self.nums[new_pos]
                self.nums[new_pos] = self.nums[pos]
                self.nums[pos] = temp
            else:
                break
            pos = new_pos

    def top(self):
        return self.nums[0]
    
    def print(self):
        print(self.nums)

    
def findKthLargest(nums: List[int], k: int) -> int: 
    h = Heap(k)
    for i in range(k):
        h.add(nums[i])
    for i in range(k, len(nums)):
        if(h.top() < nums[i]):
            h.minheap()
            h.add(nums[i])
    return h.top()
    

print(findKthLargest([3,2,3,1,2,4,5,5,6], 4))