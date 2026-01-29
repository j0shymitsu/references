class HashMap:
    def __init__(self, size):
        '''Initialise a new HashMap with a specified initial size'''

        # Create a list of None values to represent empty buckets
        self.hashmap = [None for i in range(size)]
    
# =============================================================================

    def insert(self, key, value):
        '''Insert a key-value pair into the hashmap'''

        # Check if need to expand before inserting
        self.resize()

        # Convert the key to an array index using hash function
        index = self.key_to_index(key)

        # Store key-value pair as tuple at calculated index
        self.hashmap[index] = (key, value)
    
# =============================================================================

    def get(self, key):
        '''Retrieve the value associated with a given key'''

        # Convert key to index using hash function
        index = self.key_to_index(key)

        # Retrieve the tuple at that index
        key_value = self.hashmap[index]

        # If bucket is empty, key doesn't exist
        if key_value is None:
            raise Exception("sorry, key not found")
        
        # Return just value (second element)
        return (key_value[1])

# =============================================================================

    def resize(self):
        '''
        Dynamically resize the hashmap when load factor exceeds 5%
        This helps prevent collisions
        '''

        # Edge case: if hashmap is empty, init with size 1
        if len(self.hashmap) == 0:
            self.hashmap = [None for i in range(1)]
            return
        
        # If load factor below 5%, don't resize
        if self.current_load() < 0.05:
            return
        
        # Save reference to current hashmap
        current = self.hashmap

        # Create new hashmap 10x larger than current
        new = [None for i in range(len(current) * 10)]

        # Point self.hashmap to new larger array
        self.hashmap = new

        # Rehash all existing items into new hashmap
        for item in current:
                if item is not None:
                    key = item[0]
                    index = self.key_to_index(key)
                    self.hashmap[index] = (item[0], item[1])

# =============================================================================

    def current_load(self):
        ''' 
        Calculate the current load factor of the hashmap 
        Load factor = number of filled buckets / total buckets
        '''
        filled = 0 
        total = len(self.hashmap)
        # Edge case: Avoid 0 division
        if total == 0:
            return 1
        for item in self.hashmap:
            if item is not None:
                filled += 1
        # Return ratio of filled buckets
        return filled / total

# =============================================================================

    def key_to_index(self, key):
        '''Hash function that converts a string key to an array index'''
        sum_unicode = 0
        # Sum up the Unicode values of all characters in the key
        for char in key:
            sum_unicode += ord(char)    # Gets Unicode val
        # Use modulo to ensure index is within array bounds
        return sum_unicode % len(self.hashmap)
    
# =============================================================================

    def __repr__(self):
        '''
        Return a string representation of the hashmap showing only filled 
        buckets
        '''
        buckets = []
        # Collect all non-empty buckets
        for v in self.hashmap:
            if v != None:
                buckets.append(v)
        # Convert list to string for display
        return str(buckets)
    

############################################################################### 

# Linear probing
class HashMapProbing:
    def insert(self, key, value):
        index = self.key_to_index(key)
        original_index = index
        first_iteration = True
        while (self.hashmap[index] is not None) and (self.hashmap[index][0] != key):
            if (first_iteration == False) and (index == original_index):
                raise Exception (f"hashmap is full")
            index = (index + 1) % len(self.hashmap)
            first_iteration = False
        self.hashmap[index] = (key, value)

    def get(self, key):
        index = self.key_to_index(key)
        original_index = index
        first_iteration = True
        while self.hashmap[index] is not None:
            if self.hashmap[index][0] == key:
                return self.hashmap[index][1]
            if (first_iteration == False) and (index == original_index):
                raise Exception(f"sorry, key not found")
            if self.hashmap[index][0] != key:
                index = (index + 1) % len(self.hashmap)
            first_iteration = False
        raise Exception(f"sorry, key not found")             

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final