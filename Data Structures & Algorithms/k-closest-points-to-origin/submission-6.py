class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for p in points:
            dist = ((p[0] - 0)**2 + (p[1] - 0)**2)**(1/2)
            if len(minHeap) >= k:
                if (-dist) > minHeap[0][0]:
                    heapq.heappop(minHeap)
                    heapq.heappush(minHeap, (-dist, p))
            else:
                heapq.heappush(minHeap, (-dist, p))
        res = [p[1] for p in minHeap]
        return res