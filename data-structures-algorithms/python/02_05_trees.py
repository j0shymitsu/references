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
    
# RED-BLACK TREE
## - Each node is either red or black
## - The root is black (sometimes omitted)
## - All Nil leaf nodes are black
## - If a node is red, then both its children are black
## - All paths from a single node go through the same number of black nodes
## in order to reach any of its descendant Nil nodes.
class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None

class RBTree:
    def __init__(self):
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    

    def insert(self, val):
        new_node = RBNode(val)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True

        parent = None
        current = self.root

        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                # Duplicate, return
                return
            
        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

        self.fix_insert(new_node)

    def fix_insert(self, new_node):
        current = new_node
        while current != self.root and current.parent.red:
            parent = current.parent
            grandparent = parent.parent

            if grandparent is None:
                break
            
            if parent == grandparent.left:
                uncle = grandparent.right
                if uncle.red:
                    uncle.red = False
                    parent.red = False
                    grandparent.red = True
                    current = grandparent
                else:
                    if current == parent.right:
                        current = parent
                        self.rotate_left(current)
                        parent = current.parent
                    parent.red = False
                    grandparent.red = True
                    self.rotate_right(grandparent)
            else:
                uncle = grandparent.left
                if uncle.red:
                    uncle.red = False
                    parent.red = False
                    grandparent.red = True
                    current = grandparent
                else:
                    if current == parent.left:
                        current = parent
                        self.rotate_right(current)
                        parent = current.parent
                    parent.red = False
                    grandparent.red = True
                    self.rotate_left(grandparent)
        
        self.root.red = False
    
    def exists(self, val):
        curr = self.root
        while curr != self.nil and val != curr.val:
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return curr

    def rotate_left(self, pivot_parent):
        if pivot_parent == self.nil or pivot_parent.right == self.nil:
            return
        
        pivot = pivot_parent.right
        pivot_parent.right = pivot.left

        if pivot.left != self.nil:
            pivot.left.parent = pivot_parent
        pivot.parent = pivot_parent.parent

        if pivot_parent == self.root:
            self.root = pivot
        else:
            if pivot_parent == pivot_parent.parent.left:
                pivot_parent.parent.left = pivot
            if pivot_parent == pivot_parent.parent.right:
                pivot_parent.parent.right = pivot
        
        pivot.left = pivot_parent
        pivot_parent.parent = pivot

    def rotate_right(self, pivot_parent):
        if pivot_parent == self.nil or pivot_parent.left == self.nil:
            return
        
        pivot = pivot_parent.left
        pivot_parent.left = pivot.right

        if pivot.right != self.nil:
            pivot.right.parent = pivot_parent
        pivot.parent = pivot_parent.parent

        if pivot_parent == self.root:
            self.root = pivot
        else:
            if pivot_parent == pivot_parent.parent.right:
                pivot_parent.parent.right = pivot
            if pivot_parent == pivot_parent.parent.left:
                pivot_parent.parent.left = pivot
        
        pivot.right = pivot_parent
        pivot_parent.parent = pivot


# COUNT NODES
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def count_nodes(root):
        if root is None:
            return 0
        return 1 + count_nodes(root.left) + count_nodes(root.right)