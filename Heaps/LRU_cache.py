from heapq import heapify, heappop, heappush
from collections import defaultdict
import math
class LRUCache:
    def __init__(self, capacity: int):
        self.key_val = defaultdict(lambda : None)
        self.lru_key = []
        self.capacity = capacity
        self.max_val = 0

    def get(self, key: int) -> int:
        if self.key_val[key] != None:
            for item in self.lru_key:
                if item[1] == key: 
                    item[0] = max(self.max_val+1, item[0]+1)
                    self.max_val = item[0]
            heapify(self.lru_key)
            #print("LRU heap after get on key ", key)
            #print(self.lru_key)
            return self.key_val[key]
        return -1
        
    def put(self, key: int, value: int) -> None:
        #print("Adding key ", key)
        if len(self.lru_key) >= self.capacity and self.key_val[key] == None:
            pop = heappop(self.lru_key)
            del self.key_val[pop[1]]
        for item in self.lru_key:
            if item[1] == key: 
                item[0] = max(self.max_val+1, item[0]+1)
                self.max_val = item[0]
        if self.key_val[key] != None:
            self.key_val[key] = value
            heapify(self.lru_key)
        else:
            self.key_val[key] = value
            heappush(self.lru_key, [self.max_val+1, key])
            self.max_val += 1
        #print(self.lru_key)