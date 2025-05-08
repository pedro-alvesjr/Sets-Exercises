# Python Functions README

## Functions

### 1. `find_pairs(arr1, arr2, target)`
Finds all pairs of numbers where one element is from `arr1` and another from `arr2` that sum up to the target value.

### 2. `remove_duplicates(my_list)`
Removes duplicate elements from a list while preserving order.

### 3. `longest_consecutive_sequence(nums)`
Finds the length of the longest consecutive elements sequence in an array of numbers.

## Usage Examples:
```python
print(find_pairs((3, 2, 5, 6), (4, 7, 9, 0, 3), 10))  # [(3, 7), (6, 4)]
print(remove_duplicates((2, 3, 4, 3, 4, 6, 10)))  # [2, 3, 4, 6, 10]
print(longest_consecutive_sequence((2, 3, 4, 6, 7, 8, 9, 13, 14)))  # 4
