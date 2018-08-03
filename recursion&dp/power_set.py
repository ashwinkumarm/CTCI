def power_set(set_elements):
    res = [[]]
    for i in set_elements:
        res = res + [[i] + s for s in res]
    return res


s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
print(power_set(s))

#print([1] + [2])
