class TimeMap:

    def __init__(self):
        self.keyStore = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyStore[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        keyList = self.keyStore.get(key, [])
        if len(keyList) == 0:
            return res

        l, r = 0, len(keyList) - 1
        # 0 1 3
        while l <= r:
            mid = (l+r) // 2
            if keyList[mid][0] <= timestamp:
                res = keyList[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res

