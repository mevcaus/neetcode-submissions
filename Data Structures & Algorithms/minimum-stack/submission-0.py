class MinStack:

    def __init__(self):
        self.stack = []
        self.min_value = []


    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_value.append(val if not self.min_value else min(self.min_value[-1], val))


    def pop(self) -> None:
        self.stack.pop()
        self.min_value.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_value[-1]
