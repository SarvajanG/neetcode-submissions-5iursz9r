class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numToFreq = {}
        for n in nums:
            numToFreq[n] = numToFreq.get(n, 0) + 1

        bucket = [[] for i in range(len(nums) + 1)]
        for num, freq in numToFreq.items():
            bucket[freq].append(num)
        
        res = []
        for i in range(len(bucket) - 1,  -1, -1):
            if len(res) < k:
                while bucket[i]:
                    res.append(bucket[i].pop())
            else:
                return res
        
