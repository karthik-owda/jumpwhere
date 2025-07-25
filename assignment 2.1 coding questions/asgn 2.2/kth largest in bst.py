# Kth Largest Element in an Array
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap=[]
        for i in nums:
            heapq.heappush(heap,i)
        for i in range(len(nums)-k):
            heapq.heappop(heap)
        return heapq.heappop(heap)
