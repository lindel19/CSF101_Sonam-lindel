# Practical 4
# Practical Reflection: Linked List Implementation

### Objective Reflection
In this lab, I implemented a **singly linked list** in Python and added several important operations:
- Finding the middle element
- Detecting a cycle in the linked list
- Removing duplicates from an unsorted list
- Merging two sorted linked lists into a single sorted linked list

The objective was to understand the **structure of linked lists**, practice **pointer manipulation**, and learn how to implement both **iterative and algorithmic solutions** for linked list problems.

### What I Learned
1. **Finding the Middle Element**  
   - Using **two pointers (slow and fast)** allows finding the middle efficiently in a single traversal.  
   - Reinforced understanding of **pointer movement** in linked lists.

2. **Cycle Detection**  
   - Implemented using **Floyd’s Tortoise and Hare algorithm**.  
   - Learned how a fast-moving pointer can help detect cycles efficiently without extra space.

3. **Removing Duplicates**  
   - Using a **set to track seen values** ensures O(n) time complexity for unsorted linked lists.  
   - Helped me practice **node deletion and pointer adjustment**.

4. **Merging Two Sorted Lists**  
   - Learned how to merge two linked lists using a **dummy node**.  
   - Avoided creating a new list manually by reusing existing nodes, which is **memory-efficient**.

### Challenges Faced
- Carefully managing **pointers** when deleting nodes to avoid losing the rest of the list.  
- Ensuring **cycle detection** was implemented correctly in all cases, including edge cases like an empty list.  
- Merging two sorted lists without losing the order required careful step-by-step comparisons.

### Conclusion
This lab strengthened my understanding of:
- Linked list structures and **pointer manipulation**
- Efficient algorithms for **cycle detection and duplicate removal**
- How to merge linked lists while maintaining **sorted order**

 