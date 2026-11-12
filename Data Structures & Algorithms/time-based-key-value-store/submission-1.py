class TimeMap:

    def __init__(self):
        self.keyStore = {} # hashmap (value, timestamp)
        # timestamps for each key are stored in sorted order (since they arrive in increasing order)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp]) # append value, timestamp to key's list

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.keyStore.get(key, []) # if key doesn't exist, return ""
        # arr = list of [value, timestamp] pairs
        l, r = 0, len(values) - 1

        # binary search on timestamps to find the rightmost timestamp
        while l <= r:
            m = l + ((r - l) // 2)
            if values[m][1] <= timestamp:
                res = values[m][0] # if found, return the corresponding value
                l = m + 1
            else:
                r = m - 1
        return res # return "" if key not found
