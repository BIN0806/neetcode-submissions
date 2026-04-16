class MinStack:

    def __init__(self):
        self.stack = []
        self.min_at_instant = []
        self.smallest = None

    def push(self, val: int) -> None:
        if self.smallest == None or val < self.smallest:
            self.smallest = val
            print(self.smallest)
        self.min_at_instant.append(self.smallest)
        self.stack.append(val)
    [-2,0,-3,]
    def pop(self) -> None:
        if self.min_at_instant:
            if self.smallest == self.min_at_instant[-1]:
                self.min_at_instant.pop()
                self.smallest = self.min_at_instant[-1]
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_at_instant[-1]
