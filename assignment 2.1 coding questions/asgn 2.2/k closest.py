#K Closest
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap=[]
        for (x,y) in points:
            dist=-(x*x+y*y)
            if len(heap)==k:
                heapq.heappushpop(heap,(dist,x,y))
            else:
                heapq.heappush(heap,(dist,x,y))
        return [(x,y) for (dist,x,y) in heap]
