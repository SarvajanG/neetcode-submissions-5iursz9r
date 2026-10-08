class TimeMap:

    def __init__(self):
        self.nameToTimeVal = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.nameToTimeVal[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key in self.nameToTimeVal:
            array = self.nameToTimeVal[key]
            l = 0
            r = len(array) - 1
            while l <= r:
                m = l + (r-l)//2
                if array[m][0] <= timestamp:
                    res = array[m][1]
                    l = m + 1
                else:
                    r = m - 1
        return res
