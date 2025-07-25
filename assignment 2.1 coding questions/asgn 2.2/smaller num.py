# smaller number
class Solution:  
    def countSmallerNumbers(self, nums: list[int]) -> list[int]:  
        sorted_nums = sorted(nums)  
        rank = {val: i for i, val in enumerate(sorted_nums) if val not in rank}  
        return [rank[num] for num in nums]  
