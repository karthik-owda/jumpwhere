#Task scheduler
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        counts=Counter(tasks)
        heap=[]
        for count in counts.values():
            heap.append(-count)
        heapq.heapify(heap)
        time=0
        wait=deque()
        while heap or wait:
            time+=1
            if heap:
                cur=heapq.heappop(heap)
                cur+=1
                if cur!=0:
                    wait.append((cur,time+n))
            if wait and wait[0][1]==time:
                heapq.heappush(heap,wait.popleft()[0])
        return time
