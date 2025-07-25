# find single number
class Solution:  
    def findUnique(self, nums: list[int]) -> int:  
        result = 0  
        for num in nums:  
            result ^= num  
        return result  
