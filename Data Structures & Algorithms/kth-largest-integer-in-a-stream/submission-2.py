class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.k = k
        for n in nums:
            if len(self.min_heap) < self.k:
                heapq.heappush(self.min_heap, n)
            elif n > self.min_heap[0]:
                heapq.heappop(self.min_heap)
                heapq.heappush(self.min_heap, n)

    def add(self, val: int) -> int:
        if len(self.min_heap) >= self.k:
            if val > self.min_heap[0]:
                heapq.heappush(self.min_heap, val)
                heapq.heappop(self.min_heap)
        else:
            heapq.heappush(self.min_heap, val)
        return self.min_heap[0]
