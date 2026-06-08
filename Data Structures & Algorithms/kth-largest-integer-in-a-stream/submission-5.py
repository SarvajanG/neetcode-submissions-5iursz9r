class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = []
        self.k = k
        for i in range(k):
            if i < len(nums):
                heapq.heappush(self.minHeap, nums[i])
        for j in range(k, len(nums)):
            if nums[j] > self.minHeap[0]:
                heapq.heappop(self.minHeap)
                heapq.heappush(self.minHeap, nums[j]) 

    def add(self, val: int) -> int:
        if len(self.minHeap) >= self.k:
            if val > self.minHeap[0]:
                heapq.heappop(self.minHeap)
                heapq.heappush(self.minHeap, val)
        else:
            heapq.heappush(self.minHeap, val)
        return self.minHeap[0]
