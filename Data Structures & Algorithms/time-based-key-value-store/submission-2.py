class TimeMap:

    def __init__(self):
        self.keyToValTime = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyToValTime[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        l = 0
        r = len(self.keyToValTime[key]) - 1
        array = self.keyToValTime[key]
        closest = 0
        while l <= r:
            m = l + (r-l)//2
            if timestamp - array[m][1] < timestamp - array[closest][1] and array[m][1] < timestamp:
                closest = m
            if timestamp > array[m][1]:
                l = m + 1
            elif timestamp < array[m][1]:
                r = m - 1
            else:
                return array[m][0]
        if array and array[closest][1] < timestamp:
            return array[closest][0]
        else:
            return ""