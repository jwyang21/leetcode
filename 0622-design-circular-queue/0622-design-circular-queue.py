class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.data = [None]*k
        self.head = -1
        self.tail = -1

    def enQueue(self, value: int) -> bool:
        if self.isEmpty():
            self.data[0] = value
            self.head = 0
            self.tail = 0
            return True
        elif self.isFull():
            return False
        else:
            self.tail = (self.tail+1)%self.size
            self.data[self.tail] = value
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.data[self.head] = None
            if self.head == self.tail:
                self.head = -1
                self.tail = -1
            else:
                self.head = (self.head+1)%self.size
            return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.data[self.head]
        
    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.data[self.tail]
        
    def isEmpty(self) -> bool:
        return self.head==-1 and self.tail==-1

    def isFull(self) -> bool:
        return self.head==(self.tail+1)%self.size
    #https://leetcode.com/problems/design-circular-queue/solutions/159074/straight-forward-python-solution/
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()