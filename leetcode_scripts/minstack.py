class MinStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        return None

# Tests
def test_MinStack():
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    assert minStack.getMin() == -3
    minStack.pop()
    assert minStack.top() == 0
    assert minStack.getMin() == -2

    minStack2 = MinStack()
    minStack2.push(1)
    minStack2.push(2)
    assert minStack2.getMin() == 1
    minStack2.pop()
    assert minStack2.getMin() == 1
    minStack2.pop()
    assert minStack2.getMin() == None

    minStack3 = MinStack()
    minStack3.push(2)
    minStack3.push(0)
    minStack3.push(3)
    minStack3.push(0)
    assert minStack3.getMin() == 0
    minStack3.pop()
    assert minStack3.getMin() == 0
    minStack3.pop()
    assert minStack3.getMin() == 0
    minStack3.pop()
    assert minStack3.getMin() == 2

    print("All tests passed!")

test_MinStack()
