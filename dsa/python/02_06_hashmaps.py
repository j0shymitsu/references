class HashMap:
    def get(self, key):
        index = self.key_to_index(key)
        key_value = self.hashmap[index]
        if key_value is None:
            raise Exception("sorry, key not found")
        return (key_value[1])
    
    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    # Crude example: this doesn't resize or handle collisions like a "proper"
    # hashmap would
    def key_to_index(self, key):
        sum_unicode = 0
        for char in key:
            sum_unicode += ord(char)
        return sum_unicode % len(self.hashmap)
    
    def insert(self, key, value):
        storage_index = self.key_to_index(key)
        key_value_pair = (key, value)
        self.hashmap[storage_index] = key_value_pair

    def __repr__(self):
        buckets = []
        for v in self.hashmap:
            if v != None:
                buckets.append(v)
        return str(buckets)