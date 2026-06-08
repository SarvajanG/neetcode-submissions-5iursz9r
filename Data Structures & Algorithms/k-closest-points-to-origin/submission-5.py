class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        res = []
        for point in points:
            dist = ((point[0] - 0)**2 + (point[1]- 0)**2)**0.5
            if len(maxHeap) < k:
                heapq.heappush_max(maxHeap, [dist,point])
            elif dist < maxHeap[0][0]:
                heapq.heappop_max(maxHeap)
                heapq.heappush_max(maxHeap, [dist,point])
        for item in maxHeap:
            res.append(item[1])
        return res