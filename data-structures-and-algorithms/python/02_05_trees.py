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
    
    def preorder(self, visited):
        ''' Current node visited before its children '''
        if self.val is not None:
            visited.append(self.val)
        if self.left:
            self.left.preorder(visited)
        if self.right:
            self.right.preorder(visited)
        return visited
    
    def postorder(self, visited):
        ''' Current node visited after its children '''
        if self.left:
            self.left.postorder(visited)
        if self.right:
            self.right.postorder(visited)
        visited.append(self.val)
        return visited
    
    def inorder(self, visited):
        ''' Current node visited in between its children '''
        if self.left:
            self.left.inorder(visited)
        visited.append(self.val)
        if self.right:
            self.right.inorder(visited)
        return visited
    
    def exists(self, val):
        ''' Return true if value exists in tree '''
        if val == self.val:
            return True
        if val < self.val:
            if self.left and self.left.exists(val):
                return True
            else:
                return False
        if val > self.val:
            if self.right and self.right.exists(val):
                return True
            else:
                return False
        return False
    
    def height(self):
        ''' Returns height of tree rooted at current node '''
        if self.val is None:
            return 0
        left_height = 0
        right_height = 0
        if self.left is not None:
            left_height = self.left.height()
        if self.right is not None:
            right_height = self.right.height()
        return max(left_height, right_height) + 1