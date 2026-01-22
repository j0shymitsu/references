# LINKED LISTS
## Linked lists have faster time complexity than regular lists when it comes to inserting/deleting items in the middle of the list

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return self.val

# O(1)
class LLQueue:
    # def add_to_head(self, node):
    #     if (self.head == None) and (self.tail == None):
    #         self.tail = node
    #     node.next = self.head
    #     self.head = node
    #     return

    def remove_from_head(self):
        if (self.head is None) and (self.tail is None):
            return None
        head_del = self.head
        self.head = head_del.next
        if self.head is None:
            self.tail = None
        head_del.set_next(None)
        return head_del

    def add_to_tail(self, node):
        if (self.head == None) and (self.tail == None):
            self.head = node
            self.tail = node
        if self.head is None:
            self.head = node
            return
        self.tail.set_next(node)
        self.tail = node
        
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    
    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)