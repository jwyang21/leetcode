class MyStack:#https://firsteast.tistory.com/52

    def __init__(self):
        self.stack = []
        

    def push(self, x: int) -> None:
        # push element x onto stack
        self.stack.append(x)
        

    def pop(self) -> int:
        # remove element on top of the stack and return that
        return self.stack.pop()
        

    def top(self) -> int:
        # get the top element
        # last-in-first-out (LIFO) stack
        return self.stack[-1]
        

    def empty(self) -> bool:
        # return whether the stack is empty
        return not self.stack
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()