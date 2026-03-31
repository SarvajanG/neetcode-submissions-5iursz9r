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
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]
