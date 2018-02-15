# Class for construct the nodes of the tree. (Subtrees)
class Node:
    def __init__(self, key, parent_node = None):
        self.left = None
        self.right = None
        self.key = key
        if parent_node == None:
            self.parent = self
        else:
            self.parent = parent_node

# Class with the  structure of the tree. 
# This Tree is not balanced.
class Tree:
    def __init__(self):
        self.root = None

    # Insert a single element
    def insert(self, x):
        if(self.root == None):
            self.root = Node(x)
        else:
            self._insert(x, self.root)

    def _insert(self, x, node):
        if(x < node.key):
            if(node.left == None):
                node.left = Node(x, node)
            else:
                self._insert(x, node.left)
        else:
            if(node.right == None):
                node.right = Node(x, node)
            else:
                self._insert(x, node.right)

    # Given a element, return a node in the tree with key x. 
    def find(self, x):
        if(self.root == None):
            return None
        else:
            return self._find(x, self.root)
    def _find(self, x, node):
        if(x == node.key):
            return node
        elif(x < node.key):
            if(node.left == None):
                return None
            else:
                return self._find(x, node.left)
        elif(x > node.key):
            if(node.right == None):
                return None
            else:
                return self._find(x, node.right)

    # Given a node, return the node in the tree with the next largest element.
    def next(self, node):
        if node.right != None:
            return self._left_descendant(node.right)
        else:
            return self._right_ancestor(node)

    def _left_descendant(self, node):
        if node.left == None:
            return node
        else:
            return self._left_descendant(node.left)

    def _right_ancestor(self, node):
        if node.key <= node.parent.key:
            return node.parent
        else:
            return self._right_ancestor(node.parent)

    # Delete an element of the tree
    def delete(self, x):
        node = self.find(x)
        if node == None:
            print(x, "isn't in the tree")
        else:
            if node.right == None:
                if node.left == None:
                    if node.key < node.parent.key:
                        node.parent.left = None
                        del node # Clean garbage
                    else:
                        node.parent.right = None
                        del Node # Clean garbage
                else:
                    node.key = node.left.key
                    node.left = None
            else:
                x = self.next(node)
                node.key = x.key
                x = None


# tests
t = Tree()
t.insert(5)
t.insert(8)
t.insert(3)
t.insert(4)
t.insert(6)
t.insert(2)

t.delete(8)
t.delete(5)

t.insert(9)
t.insert(1)

t.delete(2)
t.delete(100)

print(t.find(5))
print(t.find(8))
print(t.find(4))
print(t.find(6))
print(t.find(9))

