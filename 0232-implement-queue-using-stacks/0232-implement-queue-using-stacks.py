class MyQueue:#https://firsteast.tistory.com/53

    def __init__(self):
        self.inputStack = []
        self.outputStack = []       

    def push(self, x: int) -> None:
        # push element x to the back of the queue
        self.inputStack.append(x)        

    def pop(self) -> int:
        # remove element from in front of queue and return that element.
        val = self.inputStack.pop(0)
        self.outputStack.append(val)
        
        return self.outputStack[-1]       

    def peek(self) -> int:
        # get the front element
        return self.inputStack[0]
        

    def empty(self) -> bool:
        # return whether the queue is empty. 
        return not self.inputStack
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()