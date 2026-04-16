class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

# LRU Node, 2nd LRU Node, .... MRU Node
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {} # key: Nodes
        self.capacity = capacity

        self.lru, self.mru = Node(-1, -1), Node(-1, -1)
        self.lru.next, self.mru.prev = self.mru, self.lru
        
    def remove(self, node): 
        prev, nxt = node.prev, node.next

        node.next, node.prev = None, None

        prev.next, nxt.prev = nxt, prev


    # way of move data to the MRU side of the LL
    def insert(self, node):
        previous_node = self.mru.prev

        previous_node.next = node
        self.mru.prev = node

        node.prev = previous_node
        node.next = self.mru

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.cache[key].val = value
        elif len(self.cache) == self.capacity:
            self.cache.pop(self.lru.next.key)
            self.remove(self.lru.next)
            self.cache[key] = Node(key, value)
        else:
            self.cache[key] = Node(key, value)
        self.insert(self.cache[key])