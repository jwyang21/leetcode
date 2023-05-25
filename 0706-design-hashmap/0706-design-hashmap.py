class MyHashMap:

    def __init__(self):
        self.hm = {}

    def put(self, key: int, value: int) -> None:
        self.hm[key] = value

    def get(self, key: int) -> int:
        _ = -1 if key not in list(self.hm.keys()) else self.hm[key]
        return _

    def remove(self, key: int) -> None:
        if key in list(self.hm.keys()):
            del self.hm[key]
        else:
            pass
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)