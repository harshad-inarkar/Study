from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key: value, freq
        self.freq_to_keys = defaultdict(OrderedDict)  # freq: OrderedDict of keys (for LRU within freq)
        self.min_freq = 0

    def _update(self, key):
        freq = self.cache[key][1]
        # Remove key from current freq OrderedDict
        del self.freq_to_keys[freq][key]
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        # Add key to next freq OrderedDict
        self.cache[key][1] = freq + 1
        self.freq_to_keys[freq + 1][key] = None

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self._update(key)
        return self.cache[key][0]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.cache:
            self.cache[key][0] = value
            self._update(key)
            return
        if len(self.cache) == self.capacity:
            # Evict the least frequently used and least recently used key
            evict_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)

            if not self.freq_to_keys[self.min_freq]:
                del self.freq_to_keys[self.min_freq]

            del self.cache[evict_key]

        self.cache[key] = [value,1]
        self.freq_to_keys[1][key] = None
        self.min_freq = 1

# Tests
def test_LFUCache():
    # Test 1: Basic put/get
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)    # evicts key 2
    assert cache.get(2) == -1
    assert cache.get(3) == 3
    cache.put(4, 4)    # evicts key 1
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4

    # Test 2: LRU within same frequency
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)
    cache.put(3, 3)    # evicts key 2 (freq 1, LRU)
    assert cache.get(2) == -1
    assert cache.get(1) == 1
    assert cache.get(3) == 3

    # Test 3: Capacity 0
    cache = LFUCache(0)
    cache.put(1, 1)
    assert cache.get(1) == -1

    # Test 4: Update value
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(1, 10)
    assert cache.get(1) == 10
    cache.put(3, 3)    # evicts key 2
    assert cache.get(2) == -1
    assert cache.get(3) == 3

    # Test 5: Multiple evictions
    cache = LFUCache(2)
    cache.put(2, 1)
    cache.put(1, 1)
    cache.put(2, 3)
    cache.put(4, 1)
    assert cache.get(1) == -1
    assert cache.get(2) == 3
    assert cache.get(4) == 1

    print("All test cases passed!")

test_LFUCache()

