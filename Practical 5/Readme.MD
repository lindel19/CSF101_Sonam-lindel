### Instructions ###
1. Implement a method to find the maximum value in the BST.
2. Add a method to count the total number of nodes in the BST.
3. Implement a level-order traversal (breadth-first search) for the BST.
4. Create a method to find the height of the BST.
5. Implement a method to check if the tree is a valid BST.

# Inputs
# exercise 1: Implement a method to find the maximum value in the BST
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)
    def find_max(self): #traverses the right most branch of the tree as rightmost node in BST has the maximum value
        if self.root is None:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.key
# Output
![alt text](<Screenshot 2025-10-16 195206.png>)

# 2.Add a to count the total number of nodes in the BST
    def count_nodes(self):
        def count(node):
            if node is None:
                return 0
            return 1 + count(node.left) + count(node.right)
        return count(self.root)
# Output
![alt text](<Screenshot 2025-10-16 195212.png>)

# 3Implement a level-order traversal (breadth-first search) for the BST. 
    def level_order_traversal(self):
        if self.root is None:
            return []
        result=[]
        queue = [self.root]
        while queue:
            Node = queue.pop(0)
            result.append(Node.key)
            if Node.left:
                queue.append(Node.left)
            if Node.right:
                queue.append(Node.right)
        return result
# Output
![alt text](<Screenshot 2025-10-16 195220.png>)

# 4. Create a method to find the height of the BST.
    def height(self): #Recursively finds the longest path from root to a leaf 
        def node_height(node):
            if node is None:
                return -1  # height of empty tree is -1
            return 1 + max(node_height(node.left), node_height(node.right))
        return node_height(self.root)
# Output
![alt text](<Screenshot 2025-10-16 195226.png>)

# 5.implement a method to find the height of the BST. 
    def is_valid_bst(self):
        def validate(node, low=float('-inf'), high=float('inf')):
            if node is None:
                return True
            if not (low < node.key < high):
                return False
            return (validate(node.left, low, node.key) and
                    validate(node.right, node.key, high))
        return validate(self.root)  
# Output
![alt text](<Screenshot 2025-10-16 195233.png>)

bst = BST()
values = [15, 10, 20, 8, 12, 17, 25]
for v in values:
    bst.insert(v)

print("Maximum value in BST:", bst.find_max())
print("Total number of nodes:", bst.count_nodes())
print("Level-order traversal:", bst.level_order_traversal())
print("Height of BST:", bst.height())
print("Is valid BST?", bst.is_valid_bst())
# ALL OUTPUTS
![alt text](<Screenshot 2025-10-16 195238.png>)