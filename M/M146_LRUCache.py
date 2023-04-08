from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if self.cache.__len__() > self.capacity:
            self.cache.popitem(last=False)

if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1,1)
    cache.put(2,2)
    print(cache.get(1))
    cache.put(3,3)
    print(cache.get(2))
