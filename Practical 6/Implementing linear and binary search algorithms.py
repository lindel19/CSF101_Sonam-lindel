#Linear Search
"""def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = linear_search(test_list, 6)
print(f"Linear Search: Index of 6 is {result}")
#Binary search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
test_list_sorted = sorted(test_list)
result_binary = binary_search(test_list_sorted, 6)
print(f"Binary Search: Index of 6 is {result_binary}")
#compare performance
import time
def compare_search_algorithims(arr, target):
    start_time = time.time()
    linear_result = linear_search(arr, target)
    linear_time = time.time() - start_time

    arr_sorted = sorted(arr)
    start_time = time.time()
    binary_result = binary_search(arr_sorted, target)
    binary_time = time.time() - start_time

    print(f"Linear Search: Index of {target} is {linear_result}, Time taken: {linear_time:.6f} seconds")
    print(f"Binary Search: Index of {target} is {binary_result}, Time taken: {binary_time:.6f} seconds")

large_list = list(range(10000))  
compare_search_algorithims(large_list, 8888)

#Implementing Recursive Binary Search
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
result= binary_search_recursive(test_list_sorted, 6, 0, len(test_list_sorted) - 1)
print(f"Recursive Binary Search: Index of 6 is {result}")

#creating a main function
def main():
    import random
    test_list = [random.randint(1, 100) for _ in range(20)]

    print("original list:", test_list)
    print("Sorted list:", sorted(test_list))

    target = random.choice(test_list)
    print(f"\nsearching for: {target}")
#linear search
    result= linear_search(test_list, target)
    print(f"Linear Search: found at indrx {result}") 
#binary search (iterative)    
    sorted_list = sorted(test_list)
    result= binary_search(sorted_list, target)
    print(f"Binary Search(iterative): found at index {result}")

#binary search (recursive)
    result = binary_search_recursive(sorted_list, target, 0, len(sorted_list) - 1)
    print(f"Binary Search(recursive): found at index {result}")

#Compare performance
    print("\nPerformance Comparison:")
    compare_search_algorithims(test_list, target)

if __name__ == "__main__":
    main()"""""

#Exercise 1
def linear_search_all(arr, target):
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices if indices else [-1]

# Test
test_list = [3, 1, 4, 1, 5, 9, 1, 5]
target = 1
result = linear_search_all(test_list, target)
print(f"All indices of {target}: {result}")

#Exercise 2

def binary_search_insertion_point(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
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

#Exercise 3
def linear_search_count(arr, target):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
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
import math
import time

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    # Jump forward until we find a block that may contain the target
    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    # Linear search within the block
    while prev < min(step, n):
        if arr[prev] == target:
            return prev
        prev += 1

    return -1

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