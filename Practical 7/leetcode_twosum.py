def twoSum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

[2, 7, 11, 15], 9
print(twoSum([2, 7, 11, 15], 9))
[3, 2, 4], 6
print(twoSum([3, 2, 4], 6))
[3, 3], 6
print(twoSum([3, 3], 6))
[1, 5, 8, 13], 14
print(twoSum([1, 5, 8, 13], 14))
[1, 2, 3, 4, 5], 10
print(twoSum([1, 2, 3, 4, 5], 10))