
class LFUCache:
    class Node:
        def __init__(self, key, value, freq=1):
            self.key = key
            self.value = value
            self.freq = freq
            self.prev = None
            self.next = None

    class DoublyLinkedList:
        def __init__(self):
            self.head = LFUCache.Node(None, None)  # dummy head
            self.tail = LFUCache.Node(None, None)  # dummy tail
            self.head.next = self.tail
            self.tail.prev = self.head

        def insert_head(self, node):
            node.next = self.head.next
            node.prev = self.head
            self.head.next.prev = node
            self.head.next = node

        def remove(self, node):
            node.prev.next = node.next
            node.next.prev = node.prev

        def pop_tail(self):
            if self.tail.prev == self.head:
                return None
            node = self.tail.prev
            self.remove(node)
            return node

        def is_empty(self):
            return self.head.next == self.tail

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.key_node = {}  # key: Node
        self.freq_list = {}  # freq: DoublyLinkedList
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.key_node:
            return -1
        node = self.key_node[key]
        self._update(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.key_node:
            node = self.key_node[key]
            node.value = value
            self._update(node)
        else:
            if self.size == self.capacity:
                # Evict least frequently used node
                min_list = self.freq_list[self.min_freq]
                node_to_remove = min_list.pop_tail()
                if node_to_remove:
                    del self.key_node[node_to_remove.key]
                    self.size -= 1
            new_node = LFUCache.Node(key, value)
            self.key_node[key] = new_node
            if 1 not in self.freq_list:
                self.freq_list[1] = LFUCache.DoublyLinkedList()
            self.freq_list[1].insert_head(new_node)
            self.min_freq = 1
            self.size += 1

    def _update(self, node):
        freq = node.freq
        self.freq_list[freq].remove(node)
        if self.freq_list[freq].is_empty():
            del self.freq_list[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        node.freq += 1
        if node.freq not in self.freq_list:
            self.freq_list[node.freq] = LFUCache.DoublyLinkedList()
        self.freq_list[node.freq].insert_head(node)

# Tests
def test_LFUCache():
    # Test 1: Basic put/get
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)  # evicts key 2
    assert cache.get(2) == -1
    assert cache.get(3) == 3
    cache.put(4, 4)  # evicts key 1
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4

    # Test 2: Frequency update
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1  # freq of 1 becomes 2
    cache.put(3, 3)  # evicts key 2 (freq 1)
    assert cache.get(2) == -1
    assert cache.get(3) == 3
    assert cache.get(1) == 1

    # Test 3: Capacity 0
    cache = LFUCache(0)
    cache.put(0, 0)
    assert cache.get(0) == -1

    # Test 4: Tie-breaker by LRU within same freq
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)  # freq 1: 2, freq 2: 1
    cache.get(2)  # freq 1: -, freq 2: 1,2
    cache.put(3, 3)  # evicts key 1 (was least recently used among freq 2)
    assert cache.get(1) == -1
    assert cache.get(2) == 2
    assert cache.get(3) == 3

    print("All LFUCache tests passed!")

test_LFUCache()
