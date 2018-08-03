# no duplicates
def search_rotated_array(a, x):
    return _search_rotated_array(a, 0, len(a) - 1, x)


def _search_rotated_array(a, l, r, x):

    if l > r:
        return -1

    m = int((l + r) / 2)

    if a[m] == x:
        return m

    if a[l] < a[m]:
        if a[l] <= x <= a[m]:
            return _search_rotated_array(a, l, m-1, x)
        else:
            return _search_rotated_array(a, m+1, r, x)
    elif a[m] < a[r]:
        if a[m] <= x <= a[r]:
            return _search_rotated_array(a, m+1, r, x)
        else:
            return _search_rotated_array(a, l, m-1, x)
    elif a[l] == a[m]:
        if a[r] != a[m]:
            return _search_rotated_array(a, m+1, r, x)
        else:
            ind = _search_rotated_array(a, l, m-1, x)
            if ind != -1:
                return ind
            else:
                return _search_rotated_array(a, m+1, r, x)

    return -1


# a = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
# a = [2, 2, 2, 2, 2, 2, 2, 2, 0, 2]
a = [2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
print(search_rotated_array(a, 0))
