class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Count = [0]*26
        s2Count = [0]*26

        for i in range(len(s1)):
            s1Count[ord("a") - ord(s1[i])] += 1
            s2Count[ord("a") - ord(s2[i])] += 1

        if s1Count == s2Count:
            return True

        l = 0
        r = len(s1)
        while r < len(s2):
            s2Count[ord("a") - ord(s2[l])] -= 1
            s2Count[ord("a") - ord(s2[r])] += 1
            if s1Count == s2Count:
                return True
            l += 1
            r += 1
        return False
