class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        numToFreq = {}
        bucket = [[] for i in range(len(nums) + 1)]
        res = []
        for n in nums:
            numToFreq[n] = numToFreq.get(n, 0) + 1
        
        for num, freq in numToFreq.items():
            bucket[freq].append(num)
        print(bucket)
        for i in range(len(bucket)):
            while bucket[i]:
                maxVal = max(bucket[i])
                maxValIndex = bucket[i].index(maxVal)
                res.extend([maxVal]*i)
                bucket[i].pop(maxValIndex)
        return res
        
