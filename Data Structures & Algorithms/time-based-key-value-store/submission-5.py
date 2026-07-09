class TimeMap:

    def __init__(self):
        self.storage = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if len(self.storage[key]) == 0:
            return ""
        l,r = 0, len(self.storage[key]) - 1
        retval = ""
        array = self.storage[key]
        while l <= r:
            halfway = (l + r) // 2
            if timestamp >= array[halfway][1]:
                l = halfway + 1
                retval = array[halfway][0]
            else:
                r = halfway - 1
        return retval

            
