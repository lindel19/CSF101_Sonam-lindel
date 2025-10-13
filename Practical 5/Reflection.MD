#Practical 5
# Practical Reflection: Binary Search Tree (BST) Implementation

### Objective Reflection
 I implemented a **Binary Search Tree (BST)** in Python along with several important operations:
- Finding the maximum value
- Counting the total number of nodes
- Level-order traversal (breadth-first search)
- Calculating the height of the tree
- Validating whether a tree is a BST

The goal was to understand the properties of BSTs and practice implementing recursive and iterative algorithms for tree-based data structures.

### What I Learned
1. **Maximum Value in BST**  
   - The maximum value is always located at the **rightmost node**.  
   - Traversing to the rightmost child is straightforward and efficient.

2. **Counting Nodes**  
   - Recursion makes it simple to count all nodes:  
     `count = 1 + count(left) + count(right)`  
   - I understood how tree traversal naturally lends itself to recursive solutions.

3. **Level-Order Traversal (BFS)**  
   - Implemented using a **queue** to traverse the tree level by level.  
   - This helps in visualizing tree structure and is different from depth-first traversals.

4. **Height of BST**  
   - Calculating height recursively gave insight into the **depth of recursion** and how the structure of the tree affects performance.  
   - Learned that height is an important factor for time complexity in search operations.

5. **Validating BST**  
   - Checking the BST property using **min/max boundaries** reinforced understanding of BST rules:  
     ```
     left < node < right
     ```
   - Recursive validation ensures that all nodes satisfy the BST property.

### Challenges Faced
- Managing recursion correctly, especially for counting nodes and height calculation.  
- Ensuring the validation function correctly handled all edge cases for left and right subtree comparisons.  
- Understanding the differences between level-order (BFS) and depth-first traversals.

### Conclusion
This lab strengthened my understanding of **tree data structures**, **recursion**, and **algorithmic thinking**. I now appreciate:
- The efficiency of BST operations for **search, insert, and traversal**.  
- How recursion simplifies operations on hierarchical structures.  
- The importance of validating tree properties to maintain correct behavior.


