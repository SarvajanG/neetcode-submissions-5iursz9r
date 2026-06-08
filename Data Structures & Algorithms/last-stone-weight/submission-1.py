class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for stone in stones:
            heapq.heappush_max(maxHeap, stone)
        while len(maxHeap) >= 2:
            y = heapq.heappop_max(maxHeap)
            x = heapq.heappop_max(maxHeap)
            if x < y:
                y -= x
                heapq.heappush_max(maxHeap, y)
        return maxHeap[0] if maxHeap else 0