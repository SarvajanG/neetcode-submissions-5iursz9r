class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        countToWord = defaultdict(list)
        for word in strs:
            count = [0]*26
            for c in word:
                count[ord('z') - ord(c)] += 1
            countToWord[tuple(count)].append(word)
        return list(countToWord.values())