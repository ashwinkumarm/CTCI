def rec_multiply(a,b):
    smaller = a if a < b else b
    bigger = a if a > b else b
    return _rec_multiply(smaller, bigger)

def _rec_multiply(smaller, bigger):
    if smaller == 0:
        return 0
    if smaller == 1:
        return bigger

    s = smaller >> 1
    half_prod = _rec_multiply(s, bigger)

    if smaller % 2 == 0:
        return half_prod + half_prod
    else:
        return half_prod + half_prod + bigger

print(rec_multiply(4,5))