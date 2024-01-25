class LRUNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        # key, val: pointer to node
        self.cache = {}
        
        # Default 
        self.head = LRUNode(0, 0)
        self.tail = LRUNode(0, 0)
        
        # Doubly Linked
        self.head.next = self.tail
        self.tail.prev = self.head

    # Insert at tail (MRU)
    def insert(self, node): 
        prev = self.tail.prev
        next = self.tail
        prev.next = node
        next.prev = node
        
        node.next = next
        node.prev = prev
    
    # Remove at head (LRU)
    def remove(self, node):
        # Basically just change where things are pointing to 
        prev = node.prev
        next = node.next 
        
        prev.next = next
        next.prev = prev  
    
    def get(self, key):
        if key in self.cache:
            # Update it to be the MRU
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            
            return self.cache[key].val
        
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        
        # Map the new node key, val: pointer to the node
        self.cache[key] = LRUNode(key, value)
        # Insert node to the tail of the linked list
        self.insert(self.cache[key])
        
        # Check capacity
        if len(self.cache) > self.capacity:
            # Remove LRU  
            lru = self.head.next 
            self.remove(lru)
            del self.cache[lru.key]