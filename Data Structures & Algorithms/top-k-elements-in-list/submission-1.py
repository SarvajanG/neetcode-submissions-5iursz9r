class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numToFreq = {}
        bucket = [[] for i in range(len(nums) + 1)]
        res = []

        for n in nums:
            numToFreq[n] = numToFreq.get(n, 0) + 1

        for num, freq in numToFreq.items():
            bucket[freq].append(num)

        for i in range(len(bucket) -1, -1, -1):
            while bucket[i]:
                if len(res) == k:
                    return res
                res.append(bucket[i].pop())
        return res