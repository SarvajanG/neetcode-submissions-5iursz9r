class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = []
        for s in stones:
            heapq.heappush(minHeap, -s)

        while len(minHeap) >= 2:
            x = heapq.heappop(minHeap)
            y = heapq.heappop(minHeap)
            if x < y:
                heapq.heappush(minHeap, x - y)
        if minHeap:
            return -minHeap[0]
        return 0