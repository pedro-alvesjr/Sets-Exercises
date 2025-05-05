def find_pairs(arr1, arr2, target):
    my_set = set(arr1)
    pairs = []
    for num in arr2:
        complement = target - num
        if complement in my_set:
            pairs.append((complement, num))
    return pairs

