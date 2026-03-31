class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letterCount = {}
        l = 0
        res = 0
        for r in range(len(s)):
            letterCount[s[r]] = letterCount.get(s[r], 0) + 1
            if r - l + 1 - max(letterCount.values()) > k:
                letterCount[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res