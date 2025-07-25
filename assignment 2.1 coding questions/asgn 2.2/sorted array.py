# sorted array and square array
class Solution:  
    def squareAndSort(self, nums: list[int]) -> list[int]:  
        return sorted(x * x for x in nums) 
