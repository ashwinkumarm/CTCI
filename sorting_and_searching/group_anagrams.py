def group_anagrams(strs):
    for s in sorted(strs):
        print(s)


def group_anagrams_map(strs):
    anagram_map = {}
    for s in strs:
        if ''.join(sorted(s)) in anagram_map:
            anagram_map[''.join(sorted(s))].append(s)
        else:
            anagram_map[''.join(sorted(s))] = [s]

    res = []
    for k in sorted(anagram_map.keys()):
        for e in anagram_map[k]:
            res.append(e)

    return res


strs = ["ash",  "win", "hsa", "kum", "ar"]
print(group_anagrams_map(strs))