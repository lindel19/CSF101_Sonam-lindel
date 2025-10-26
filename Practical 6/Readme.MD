# Instructions
1.Modify the linear search function to return all indices where the target appears, not just the first one.

2.Implement a function that uses binary search to find the insertion point for a target value in a sorted list.

3.Create a function that counts the number of comparisons made in each search algorithm.

4.Implement a jump search algorithm and compare its performance with linear and binary search.
### Input
# Exercise 1
def linear_search_all(arr, target):

    indices = []   #prepares an empty container for storing all matching indices
    for i in range(len(arr)): #iterates through the entire list
        if arr[i] == target:  #checks if the current element is equal to what we are searching
            indices.append(i)
    return indices 
    if indices else [-1]#returns all found indices or -1 if none found

# Test
test_list = [3, 1, 4, 1, 5, 9, 1, 5]
target = 1
result = linear_search_all(test_list, target)
print(f"All indices of {target}: {result}")

# Output
![alt text](<Screenshot 2025-10-23 222816.png>)

# Exercise 2

def binary_search_insertion_point(arr, target):

    left, right = 0, len(arr) - 1 #sets the first and last indices as boundaries
    while left <= right:
        mid = (left + right) // 2 #calculate the middle index
        if arr[mid] == target:
            return mid  # already exists at this index
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left  # insertion point

# Test
sorted_list = [1, 3, 5, 7, 9]
target = 6
result = binary_search_insertion_point(sorted_list, target)
print(f"Insertion point for {target} is index {result}")
# Output
![alt text](<Screenshot 2025-10-23 222912.png>)

# Exercise 3
def linear_search_count(arr, target):

    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1 #increment comparison count each time we check an element
        if arr[i] == target:
            return i, comparisons #return both the found index and number of comparisons
    return -1, comparisons

def binary_search_count(arr, target):

    left, right = 0, len(arr) - 1
    comparisons = 0
    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1, comparisons

# Test
arr = list(range(1, 21))
target = 15

lin_result, lin_comparisons = linear_search_count(arr, target)
bin_result, bin_comparisons = binary_search_count(arr, target)

print(f"Linear Search Comparisons: {lin_comparisons}")
print(f"Binary Search Comparisons: {bin_comparisons}")

#Exercise 4
import math #for sqrt calculation
import time

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n)) # optimal jump size
    prev = 0

    # Jump forward until we find a block that may contain the target
    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))# increase the jump size
        if prev >= n:
            return -1

    # Linear search within the block
    while prev < min(step, n):
        if arr[prev] == target:
            return prev
        prev += 1

    return -1
# Output
![alt text](<Screenshot 2025-10-23 223123.png>)

# Compare performance with Linear & Binary Search
def compare_searches(arr, target):
    arr_sorted = sorted(arr)

    start = time.time()
    linear_search_all(arr, target)
    linear_time = time.time() - start

    start = time.time()
    binary_search_count(arr_sorted, target)
    binary_time = time.time() - start

    start = time.time()
    jump_search(arr_sorted, target)
    jump_time = time.time() - start

    print(f"Linear Search Time: {linear_time:.6f}s")
    print(f"Binary Search Time: {binary_time:.6f}s")
    print(f"Jump Search Time: {jump_time:.6f}s")

# Test with a large list
arr = list(range(1, 100000))
compare_searches(arr, 88888)
# Output
![alt text](<Screenshot 2025-10-23 223217.png>)

# Final all Outputs
![alt text](<Screenshot 2025-10-23 223321.png>)