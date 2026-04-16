class TimeMap:
    from collections import defaultdict
    def __init__(self):
        self.db = defaultdict(dict) 
        self.timeline = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.db[timestamp]:
            self.db[timestamp] = { key : value}
        self.db[timestamp][key] = value
        self.timeline[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key in self.db[timestamp]:
            return self.db[timestamp][key]
# time_line = {} ((keys): [time,....,last_seen])
# DB = { (time): {(keys): (value)}}
# get either gets
