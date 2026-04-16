class MinStack:

    def __init__(self):
        self.stack = []
        self.min_at_instant = []
        self.smallest = None

    def push(self, val: int) -> None:
        if not self.smallest or val < self.smallest:
            self.smallest = val
        self.min_at_instant.append(self.smallest)
        self.stack.append(val)

    def pop(self) -> None:
        if self.min_at_instant:
            self.min_at_instant.pop()
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_at_instant[-1]
