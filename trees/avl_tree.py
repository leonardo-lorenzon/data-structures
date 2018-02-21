# Class for construct the nodes of the tree. (Subtrees)
class Node:
    def __init__(self, key, parent_node = None):
        self.left = None
        self.right = None
        self.height = 0
        self.key = key
        self.parent = parent_node

# Class with the  structure of the AVL tree. 
class Tree:
    def __init__(self):
        self.root = None

    # Insert a sigle element and rebalance the tree
    def avl_insert(self, x):
        self.insert(x)
        node = self.find(x)
        self._rebalance(node)

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

    # Rebalance the tree
    def _rebalance(self, node):
        p = node.parent
        if (node.left and node.right) != None:
            if node.left.height > node.right.height + 1:
                self._rebalance_right(node)
            if node.right.height > node.left.height + 1:
                self._rebalance_left(node)
        elif node.right == None and node.left != None:
            if node.left.height >= 2:
                self._rebalance_right(node)
        elif node.left == None and node.right != None:
            if node.right.height >= 2:
                self._rebalance_left(node)
        self._adjust_height(node)
        if p != None:
            self._rebalance(p)

    # Adjust the height of the node
    def _adjust_height(self, node):
        if (node.left and node.right) != None:
            node.height = 1 + max(node.left.height, node.right.height)
        elif node.right == None and node.left != None:
            node.height = 1 + node.left.height
        elif node.left == None and node.right != None:
            node.height = 1 + node.right.height
        else:
            node.height = 1


    def _rebalance_right(self, node):
        l = node.left
        if (l.left and l.right) != None:
            if l.right.height > l.left.height:
                self._rotate_left(l)
        elif l.left == None and l.right != None:
            if l.right.height > 0:
                self._rotate_left(l)
        self._rotate_right(node)

    def _rebalance_left(self, node):
        r = node.right
        if (r.right and r.left) != None:
            if r.left.height > r.right.height:
                self._rotate_right(r)
        elif r.right == None and r.left != None:
            if r.left.height > 0:
                self._rotate_right(r)
        self._rotate_left(node)

    def _rotate_right(self, node):
        l = node.left
        p = node.parent
        lr = l.right
        l.parent = p
        if p != None:
            if p.key <= l.key:
                p.right = l
            else:
                p.left = l
            if lr != None:
                lr.parent = node
            node.left = lr
            l.right = node
            node.parent = l
            del node
        else:
            p = self.root
            if lr != None:
                lr.parent = node
            p.left = lr
            l.right = node
            node.parent = l
            self.root = l
            del node

        self._adjust_height(l.right)
        self._adjust_height(l)

    def _rotate_left(self, node):
        r = node.right
        p = node.parent
        rl = r.left
        r.parent = p
        if p != None:
            if p.key > r.key:
                p.left = r
            else:
                p.right = r
            if rl != None:
                rl.parent = node
            node.right = rl
            r.left = node
            node.parent = r
            del node
        else:
            p = self.root
            if rl != None:
                rl.parent = node
            p.right = rl
            r.left = p
            node.parent = r
            self.root = r
            del node
                    
        self._adjust_height(r.left)
        self._adjust_height(r)


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

    # Delete an element and rebalance the tree
    def avl_delete(self, x):
        node = self.find(x)
        if node.parent != None:
            p = node.parent
        self.delete(x)
        if node.parent == None:
            p = self.root
        self._rebalance(p)


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
                    else:
                        node.parent.right = None                 
                else:
                    if node.key < node.parent.key:
                        if node.left != None:
                            node.left.parent = node.parent
                        node.parent.left = node.left
                    else:
                        if node.left != None:
                            node.left.parent = node.parent
                        node.parent.right = node.left 
            else:
                x = self.next(node)
                node.key = x.key
                if x.key < x.parent.key:
                    if x.right != None:
                        x.right.parent = x.parent
                    x.parent.left = x.right
                else:
                    if x.right != None:
                        x.right.parent = x.parent
                    x.parent.right = x.right


# tests

t = Tree()
t.avl_insert(15)
t.avl_insert(9)
t.avl_insert(8)
t.avl_insert(25)
t.avl_insert(26)
t.avl_insert(32)
t.avl_insert(2)
t.avl_insert(7)


print(t.find(26).right.key)


