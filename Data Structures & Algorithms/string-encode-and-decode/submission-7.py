class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += s + "Z"

        return res


    def decode(self, s: str) -> List[str]:
        res = []
        temp = ""

        for c in s:
            if c == "Z":
                res.append(temp)
                temp = ""
            else:
                temp += c
        return res



