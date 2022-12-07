class MyStack:

    def __init__(self):
        self.Stack = deque()

    def push(self, x: int) -> None:
        tempList = deque()
        tempList.append(x)
        while self.Stack:
            tempList.append(self.Stack.popleft())
        self.Stack = tempList


    def pop(self) -> int:
        return self.Stack.popleft()

    def top(self) -> int:
        return self.Stack[0]

    def empty(self) -> bool:
        if self.Stack:
            return False
        else:
            return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()