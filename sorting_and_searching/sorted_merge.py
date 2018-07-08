def sorted_merge(a, b):
    index_merged = len(a) - 1
    index_a = len(a) - len(b) - 1  # to get the last element which is of None
    index_b = len(b) - 1
    while index_b >= 0:
        if index_a >= 0 and a[index_a] > b[index_b]:
            a[index_merged] = a[index_a]
            index_a -= 1
        else:
            a[index_merged] = b[index_b]
            index_b -= 1
        index_merged -= 1


a = [1, 3, 5, 7, 9, None, None, None, None]
b = [2, 4, 6, 8]
sorted_merge(a, b)
print(a)

