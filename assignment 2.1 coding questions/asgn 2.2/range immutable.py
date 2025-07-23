# Range sum query immutable
class NumArray:  
    def __init__(self, nums: list[int]):  
        self.accumulated = [0]  
        for num in nums:  
            self.accumulated.append(self.accumulated[-1] + num)  

    def getRangeSum(self, left: int, right: int) -> int:  
        return self.accumulated[right + 1] - self.accumulated[left] 
