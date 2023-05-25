import random
class RandomizedSet:

    def __init__(self):
        self.l = []

    def insert(self, val: int) -> bool:
        if val not in self.l:
            self.l.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.l:
            self.l.remove(val)
            return True
        else:
            return False        

    def getRandom(self) -> int:
        return random.sample(self.l, 1)[0]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
'''
RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
'''