class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        s1Count, s2Count = [0]*26, [0]*26
        matches = 0
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1
        
        for i in range(len(s1Count)):
            if s1Count[i] == s2Count[i]:
                matches += 1
        
        l = 0
        for r in range(len(s1), len(s2)):

            if matches == 26:
                return True
            
            right = ord(s2[r]) - ord("a")
            s2Count[right] += 1
            if s1Count[right] == s2Count[right]:
                matches += 1
            elif s1Count[right] + 1 == s2Count[right]:
                matches -= 1
            
            left = ord(s2[l]) - ord("a")
            s2Count[left] -= 1
            if s1Count[left] == s2Count[left]:
                matches += 1
            elif s1Count[left] - 1 == s2Count[left]:
                matches -= 1
            
            l += 1
        return matches == 26