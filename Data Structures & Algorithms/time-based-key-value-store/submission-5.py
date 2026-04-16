class TimeMap:
    from collections import defaultdict
    def __init__(self):
        self.db = defaultdict(list) # DB = { (keys): [ (value, time) ]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.db[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.db[key]) - 1
        while l <= r:
            mid = (l+r) // 2
            if self.get_time(key, mid) == timestamp:
                return self.get_val(key, mid)
            elif self.get_time(key, mid) < timestamp:
                l = mid + 1
            elif self.get_time(key, mid) > timestamp:
                r = mid - 1

        return self.get_val(key, r) if r >= 0 else ""
    
    def get_time(self, key: str, idx: int) -> int: return self.db[key][idx][1]
    def get_val(self, key: str, idx: int) -> str: return self.db[key][idx][0]  