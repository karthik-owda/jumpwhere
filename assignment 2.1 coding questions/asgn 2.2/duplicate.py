# duplicate values
class Solution:  
    def hasDuplicate(self, nums: list[int]) -> bool:  
        return len(set(nums)) != len(nums)
