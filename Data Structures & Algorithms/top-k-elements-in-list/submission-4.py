class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        numToFreq = {}
        for n in nums:
            numToFreq[n] = numToFreq.get(n, 0) + 1
        
        bucket = [[] for i in range(len(nums) + 1)]

        for num, freq in numToFreq.items():
            bucket[freq].append(num)
        
        topK = []
        for i in range(len(bucket) - 1, -1, -1):
            while bucket[i]:
                topK.append(bucket[i].pop())
                if len(topK) == k:
                    return topK
        return topK