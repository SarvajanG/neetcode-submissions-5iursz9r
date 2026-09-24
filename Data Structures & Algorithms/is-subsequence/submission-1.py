class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sp = 0
        tp = 0
        while tp < len(t) and sp < len(s):
            if s[sp] == t[tp]:
                sp += 1
            tp += 1
        if sp == len(s):
            return True
        return False