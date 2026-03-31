class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for p in points:
            curDist = math.sqrt(p[0]*p[0] + p[1]*p[1])
            if len(maxHeap) < k:
                heapq.heappush_max(maxHeap, [curDist, p])
            else:
                maxDist = math.sqrt(maxHeap[0][1][0]*maxHeap[0][1][0] + maxHeap[0][1][1]*maxHeap[0][1][1])
                print(maxHeap)
                print(curDist, maxDist)
                if curDist < maxDist:
                    heapq.heappop_max(maxHeap)
                    heapq.heappush_max(maxHeap, [curDist, p])
        res = []
        for item in maxHeap:
            res.append(item[1])
        return res