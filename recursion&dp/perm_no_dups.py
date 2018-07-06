def perm_no_dups(s):
    res = []
    _perm_no_dups(list(s), 0, len(s), res)
    return res

def _perm_no_dups(s, l, r, res):
    if l == r:
        res.append(''.join(s))
    else:
        for i in range(l, r):
            s[l], s[i] = s[i], s[l]
            _perm_no_dups(s, l+1, r, res)
            s[l], s[i] = s[i], s[l]


print(perm_no_dups("abc"))