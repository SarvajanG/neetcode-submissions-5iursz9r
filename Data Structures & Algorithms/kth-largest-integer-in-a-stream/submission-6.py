class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = []
        self.k = k
        for n in nums:
            if len(self.minHeap) < self.k:
                heapq.heappush(self.minHeap, n)
            elif n > self.minHeap[0]:
                heapq.heappop(self.minHeap)
                heapq.heappush(self.minHeap, n)

    def add(self, val: int) -> int:
        if len(self.minHeap) < self.k:
            heapq.heappush(self.minHeap, val)
        elif val > self.minHeap[0]:
            heapq.heappop(self.minHeap)
            heapq.heappush(self.minHeap, val)
        return self.minHeap[0]
