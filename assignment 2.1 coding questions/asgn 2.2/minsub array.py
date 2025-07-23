# minimum size subarry sum
class Solution:  
    def minSumSubarray(self, nums: List[int]) -> int:  
        dp = [0] * len(nums)  
        dp[0] = nums[0]  
        for i in range(1, len(nums)):  
            dp[i] = min(nums[i], dp[i - 1] + nums[i])  
        return min(dp)
