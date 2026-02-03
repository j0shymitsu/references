# QUEUE DATA STRUCTURE
## First-in, first-out

# QUEUE FUNCTIONALITY
class Queue:
    def __init__(self):
        self.items = []


    # Also called 'enqueue' when referring to queues
    ## This example is not O(1)
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
    
def matchmake(queue, user):
    username = user[0]
    matchmaking_status = user[-1]

    if matchmaking_status == 'leave':
        queue.search_and_remove(username)
    elif matchmaking_status == 'join':
        queue.push(username)

    if queue.size() >= 4:
        user_1 = queue.pop()
        user_2 = queue.pop()
        return f'{user_1} matched {user_2}!'
    elif queue.size() < 4:
        return f'No match found'