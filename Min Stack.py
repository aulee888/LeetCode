class MinStack:
    """
    Naive solution.
    """
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack = self.stack[:] + [x]

    def pop(self) -> None:
        self.stack = self.stack[:-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        n = len(self.stack)
        curr_min = self.stack[0]

        for i in range(1, n):
            if self.stack[i] < curr_min:
                curr_min = self.stack[i]

        return curr_min


class Minstack2:
    def __init__(self):
        self.stack = []
        self.minelements = []

    def push(self, x):
        if not self.stack:
            self.stack.append(x)
            self.minelements.append(x)

        else:
            self.stack.append(x)
            curr_min = self.minelements[-1]

            if x < curr_min:
                self.minelements.append(x)
            else:
                self.minelements.append(curr_min)

    def pop(self):
        self.stack.pop()
        self.minelements.pop()
        
    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minelements[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()