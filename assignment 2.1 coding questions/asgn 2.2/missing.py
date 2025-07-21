# finding missing values
class Solution:  
    def findMissing(self, nums: list[int]) -> int:
        n=len(nums)
        total =(n*(n+1))//2
        return total-sum(nums)
