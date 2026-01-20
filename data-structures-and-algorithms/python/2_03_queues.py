# QUEUE DATA STRUCTURE
## First-in, first-out

# QUEUE FUNCTIONALITY
class Queue:
    def __init__(self):
        self.items = []


    # Also called 'enqueue' when referring to queues
    def push(self, item):
        self.items.insert(0, item)

    # Also called 'dequeue'    
    def pop(self):
        if self.items == []:
            return None
        item_to_pop = self.items[-1]
        del self.items[-1]
        return item_to_pop

    def peek(self):
        if self.items == []:
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)