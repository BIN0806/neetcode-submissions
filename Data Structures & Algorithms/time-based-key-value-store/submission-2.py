class TimeMap:
    from collections import defaultdict
    def __init__(self):
        self.db = defaultdict(list) 

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.db[key].append((value, timestamp))
        print("set:",self.db)

    def get(self, key: str, timestamp: int) -> str:
        print("get:",self.db)
        l, r = 0, len(self.db[key]) - 1
        while l <= r:
            mid = (l+r) // 2
            if self.get_time(key, mid) == timestamp:
                return self.get_val(key, mid)
            elif self.get_time(key, mid) < timestamp:
                l = mid + 1
            elif self.get_time(key, mid) > timestamp:
                r = mid - 1

        if r > 0: 
            return self.get_val(key, r)
        # if l > r:
        #     if l == len([self.db[key]]):
        #         return self.get_val(key, len([self.db[key]])-1)
        #     else:
        #         return self.get_val(key, r)
        return ""
    
    def get_time(self, key: str, idx: int) -> int:
        return self.db[key][idx][1]
    def get_val(self, key: str, idx: int) -> str:
        return self.db[key][idx][0]  
# DB = { (keys): [ (value, time) ] }
