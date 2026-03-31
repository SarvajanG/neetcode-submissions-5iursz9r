class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for n in nums:
            if len(minHeap) < k:
                heapq.heappush(minHeap, n)
            elif n > minHeap[0]:
                heapq.heappush(minHeap, n)
                heapq.heappop(minHeap)
                
        return minHeap[0] 
        