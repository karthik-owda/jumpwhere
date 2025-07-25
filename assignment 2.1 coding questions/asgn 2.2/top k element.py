# Top k element
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count=Counter(nums)
        heap=[]
        for num,freq in count.items():
            if len(heap)<k:
                heapq.heappush(heap,(freq,num))
            elif freq>heap[0][0]:
                heapq.heapreplace(heap,(freq,num))
        top_k=[num for freq,num in heap]
        return top_k
