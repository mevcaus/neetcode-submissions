class MinStack:

    def __init__(self):
        self.storage = []

    def push(self, val: int) -> None:
        if self.storage:
            self.storage.append([val, min(self.storage[-1][1], val)])
        else:
            self.storage.append([val, val])

    def pop(self) -> None:
        self.storage.pop()

    def top(self) -> int:
        return self.storage[-1][0]

    def getMin(self) -> int:
        return self.storage[-1][1]
