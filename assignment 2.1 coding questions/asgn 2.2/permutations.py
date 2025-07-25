#44. Permutations
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def backtrack(start,end):
            if start==end:
                result.append(nums[:])
                return
            for i in range(start,end):
                nums[start],nums[i]=nums[i],nums[start]
                backtrack(start+1,end)
                nums[start],nums[i]=nums[i],nums[start]
        result=[]
        backtrack(0,len(nums))
        return result
