# LINKED LISTS
## Linked lists have faster time complexity than regular lists when it comes to inserting/deleting items in the middle of the list

class Node:
    ''' Represents a single node in the linked list '''
    def __init__(self, val):
        self.val = val      # Store the nodes data
        self.next = None    # Pointer to next node (init None)

    def set_next(self, node):
        ''' Update next pointer to reference another nodem '''
        self.next = node

    def __repr__(self):
        ''' String representation '''
        return self.val

# O(1)
class LLQueue:
    ''' Queue implementation using singly linked list '''

    # Not typical FIFO behaviour 
    # def add_to_head(self, node):
    #     if (self.head == None) and (self.tail == None):
    #         self.tail = node
    #     node.next = self.head
    #     self.head = node
    #     return

    def remove_from_head(self):
        ''' Dequeue - removes and returns front element '''
        # Handle empty queue
        if (self.head is None) and (self.tail is None):
            return None
        
        # Save reference to current head before removing it
        head_del = self.head

        # Move head pointer to next node
        self.head = head_del.next

        # If queue is now empty update tail to None as well
        if self.head is None:
            self.tail = None

        # Clean up removed node by setting its next to None
        head_del.set_next(None)
        return head_del

    def add_to_tail(self, node):
        ''' Enqueue - adds element to back of the queue '''
        # Handle empty queue
        if (self.head == None) and (self.tail == None):
            self.head = node
            self.tail = node
            return      # Early return to avoid dup logic
        
        # Edge case: if head is None but tail isn't (shouldn't normally occur)
        if self.head is None:
            self.head = node
            return
        
        # Normal case: link current tail to new node
        self.tail.set_next(node)
        self.tail = node
        
    def __init__(self):
        ''' Initialise an empty queue '''
        self.head = None    # Points to front of queue
        self.tail = None    # Points to back of queue

    def __iter__(self):
        ''' Makes queue iterable '''
        node = self.head
        while node is not None:
            yield node          # Return current node and pause til next iter
            node = node.next    # Move to next node
    
    def __repr__(self):
        ''' String representation '''
        nodes = []
        for node in self:
            nodes.append(node.val)  # Collect all node values
        return " -> ".join(nodes)   # Join with arrows to show direction