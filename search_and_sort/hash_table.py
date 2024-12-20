class HashTable:
    def __init__(self) -> None:
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
    
    def put(self, key, data):
        hash_value = self.hash_function(key, len(self.slots))
        
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data

            else:
                next_slot = self.rehash(hash_value, len(len(self.slots)))
                while(self.slots[next_slot] is not None and self.slots[next_slot] != key):
                    next_slot = self.rehash(next_slot, len(self.slots))
                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data
            
    def hash_function(self, key, size):
        return key % size
    
    def rehash(self, hash_value, size):
        return (hash_value + 1, size)
    
    def get(self, key):
        start_slots = self.hash_function(key, len(self.slots))

        position = start_slots

        while self.slots[position] is not None:
            if self.slots[position] == key:
                return self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slots:
                    return None

    def __getitem__(self, key):
        return self.get(key)
    
    def __setitem__(self, key, value):
        self.put(key, value)

a = HashTable()
a [54] = "cat"
print(a[0])
print(a[55])

