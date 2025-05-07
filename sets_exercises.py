def find_pairs(arr1, arr2, target):
    my_set = set(arr1)
    pairs = []
    for num in arr2:
        complement = target - num
        if complement in my_set:
            pairs.append((complement, num))
    return pairs


def remove_duplicates(my_list):
    my_set = set(my_list)
    new_list = list(my_set)
    return new_list

def longest_consecutive_sequence(nums):
    num_set = set(nums)
    longest_sequence = 0 
    for num in nums:
        if num - 1 not in num_set:
            current_num = num 
            current_sequence = 1 
            while current_num + 1 in num_set:
                current_num += 1 
                current_sequence += 1 
            longest_sequence = max(longest_sequence, current_sequence)
    return longest_sequence
