class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity
        self.size = 0

        # Dummy head and tail nodes
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        # Always add new node right after head
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        # Remove an existing node from the linked list
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def _move_to_head(self, node):
        # Move certain node to the head (most recently used)
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        # Pop the least recently used node
        node = self.tail.prev
        self._remove_node(node)
        return node

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node:
            return -1
        # Move the accessed node to the head
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if not node:
            newNode = DLinkedNode(key, value)
            self.cache[key] = newNode
            self._add_node(newNode)
            self.size += 1

            if self.size > self.capacity:
                # Pop the tail
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            # Update the value
            node.value = value
            self._move_to_head(node)

# Tests
def test_lru_cache():
    # Test 1: Basic put/get
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1  # returns 1
    cache.put(3, 3)           # evicts key 2
    assert cache.get(2) == -1 # returns -1 (not found)
    cache.put(4, 4)           # evicts key 1
    assert cache.get(1) == -1 # returns -1 (not found)
    assert cache.get(3) == 3  # returns 3
    assert cache.get(4) == 4  # returns 4

    # Test 2: Overwrite value
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(1, 10)
    assert cache.get(1) == 10
    cache.put(3, 3)
    assert cache.get(2) == -1
    assert cache.get(3) == 3

    # Test 3: Capacity 1
    cache = LRUCache(1)
    cache.put(1, 1)
    assert cache.get(1) == 1
    cache.put(2, 2)
    assert cache.get(1) == -1
    assert cache.get(2) == 2

    # Test 4: Get non-existent key
    cache = LRUCache(2)
    assert cache.get(99) == -1

    print("All LRUCache tests passed!")

test_lru_cache()
