# two sum
class Solution:  
    def locateTwoSum(self, nums: list[int], target: int) -> list[int]:  
        num_map = {}  
        for i, val in enumerate(nums):  
            if target - val in num_map:  
                return [i, num_map[target - val]]  
            num_map[val] = i
