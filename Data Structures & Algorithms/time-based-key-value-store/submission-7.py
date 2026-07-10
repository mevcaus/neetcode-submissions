class TimeMap:

    def __init__(self):
        self.storage = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        array = self.storage[key]
        ret = ""
        l,r = 0, len(array) - 1
        while l <= r:
            m = (l + r) // 2
            if array[m][1] == timestamp:
                return array[m][0]
            elif array[m][1] < timestamp:
                ret = array[m][0]
                l = m + 1
            else:
                r = m -1
        return ret
