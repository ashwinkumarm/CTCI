def perm_dups(s):
    res = set()
    _perms_dups(list(s), 0, len(s), res)
    return res

def _perms_dups(s, l, r, res):
    if l == r:
        res.add(''.join(s))
    else:
        for i in range(l, r):
            s[l], s[i] = s[i], s[l]
            _perms_dups(s, l+1, r, res)
            s[l],s[i] = s[i], s[l]

print(perm_dups("abcc"))

