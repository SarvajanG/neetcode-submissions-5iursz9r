class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Map = {}
        for c in s1:
            s1Map[c] = s1Map.get(c, 0) + 1
        
        l,r = 0,0
        s2Map = {}
        while r < len(s2):
            if s2[r] in s1Map:
                while s2[r] in s2Map and s2Map[s2[r]] >= s1Map[s2[r]]:
                    s2Map[s2[l]] -= 1
                    l += 1    
                s2Map[s2[r]] = s2Map.get(s2[r], 0) + 1
            else:
                s2Map = {}
                l += 1
            r += 1
            if s1Map == s2Map:
                return True
        return False