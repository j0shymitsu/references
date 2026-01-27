# STACK DATA STRUCTURE
## Last-in, first-out

# CRUDE EXAMPLE OF STACK FUNCTIONALITY
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)
    
    def peek(self):
        if self.items == []:
            return None
        return self.items[-1]

    def pop(self):
        if self.items == []:
            return None
        item_to_pop = self.items[-1]
        del self.items[-1]
        return item_to_pop

# IMPLEMENTATION
## Balancing parentheses: Making sure pairs of parantheses are properly matched
def is_balanced(input_str):
    stack = Stack()
    for char in input_str:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if stack.size() == 0:
                return False
            else:
                stack.pop()
    if stack.size() == 0:
        return True
    return False
    