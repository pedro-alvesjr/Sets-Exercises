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
