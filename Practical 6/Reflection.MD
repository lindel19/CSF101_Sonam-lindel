# Practical 5 Reflection: Implementing Linear and Binary Search Algorithms

### Objective Reflection
I implemented **linear search**, **binary search (iterative and recursive)**, and **jump search** algorithms in Python. The main objective was to understand how different search algorithms work, analyze their efficiency, and learn when to use each one. I also explored counting comparisons and finding insertion points, which deepened my understanding of algorithmic performance.

### What I Learned
1. **Linear Search**  
   - Simple and easy to implement.  
   - Works on **unsorted lists**.  
   - Inefficient for large lists, as its **time complexity is O(n)**.  
   - Modifying it to return all occurrences improved its utility for real-world problems.

2. **Binary Search**  
   - Efficient on **sorted lists**, with **O(log n)** time complexity.  
   - Implementing both iterative and recursive versions helped me understand recursion and how search boundaries are updated.  
   - Learned the importance of **sorting the data first**, which is a prerequisite for binary search.  

3. **Jump Search**  
   - Acts as a compromise between linear and binary search.  
   - Uses **blocks of size √n** to jump and then performs linear search within the block.  
   - Useful for scenarios where **random access is allowed** and lists are large.  

4. **Counting Comparisons and Insertion Points**  
   - Measuring the number of comparisons gave a practical insight into algorithm efficiency.  
   - Finding insertion points is a useful extension of binary search for **maintaining sorted lists dynamically**.

### Challenges Faced
- Understanding **recursive binary search** initially took time; visualizing the left and right boundaries helped.  
- Implementing **jump search** required careful calculation of block indices to avoid index errors.  
- Comparing performance for very large lists required attention to **execution time measurement** using `time.time()`.

### Conclusion
This lab helped me **strengthen my understanding of search algorithms**, their differences, and practical use cases. I now appreciate:
- When **linear search** is sufficient (small or unsorted data).  
- Why **binary search** is preferred for large sorted data.  
- How **jump search** can provide a middle ground.  

Additionally, implementing comparison counters and insertion points provided a deeper perspective on **algorithm efficiency** and **practical applications** in real-world programming.

