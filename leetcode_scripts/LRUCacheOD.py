from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

# Tests
def test_LRUCache():
    # Test 1: Basic put/get
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    assert lru.get(1) == 1  # returns 1
    lru.put(3, 3)           # evicts key 2
    assert lru.get(2) == -1 # returns -1 (not found)
    lru.put(4, 4)           # evicts key 1
    assert lru.get(1) == -1 # returns -1 (not found)
    assert lru.get(3) == 3  # returns 3
    assert lru.get(4) == 4  # returns 4

    # Test 2: Overwrite value and check order
    lru2 = LRUCache(2)
    lru2.put(1, 1)
    lru2.put(2, 2)
    lru2.put(1, 10)         # update value for key 1
    assert lru2.get(1) == 10
    lru2.put(3, 3)          # evicts key 2
    assert lru2.get(2) == -1
    assert lru2.get(3) == 3
    assert lru2.get(1) == 10

    # Test 3: Capacity 1
    lru3 = LRUCache(1)
    lru3.put(1, 1)
    assert lru3.get(1) == 1
    lru3.put(2, 2)
    assert lru3.get(1) == -1
    assert lru3.get(2) == 2

    # Test 4: Get non-existent key
    lru4 = LRUCache(2)
    assert lru4.get(99) == -1

    print("All tests passed!")

test_LRUCache()

