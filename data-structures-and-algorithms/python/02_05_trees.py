# TREES
## Widely used data structure that simulate a hierarchical tree; root node
## usually goes at top

# BINARY SEARCH TREE
class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val
    
    def insert(self, val):
        if self.val == None:
            self.val = val
        if self.val == val:
            return self.val
        
        if val < self.val:
            if self.left is None:
                self.left = BSTNode(val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = BSTNode(val)
            else:
                self.right.insert(val)
        
    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val
    
    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val