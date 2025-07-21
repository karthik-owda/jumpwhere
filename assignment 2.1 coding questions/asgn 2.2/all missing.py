# finding all missing numbers
class Solution:  
    def missingNumbers(self, nums: list[int]) -> list[int]:  
        seen = set(nums)  
        return [i for i in range(1, len(nums) + 1) if i not in seen]  
