def mm(n):
    return sum(i for i in range(n) if i % 3 == 0 or i % 5 == 0)

def merge_strings(a,b):
    a = list(a)
    b = list(b)

    i = 0
    r = []
    while i < max(len(a), len(b)):
        if i < len(a):
            r.append(a[i])
        if i < len(b):
            r.append(b[i])
        i += 1

    return ''.join(r)

# a = "abc"
# b = "de"
# print(merge_strings(a,b))

def splitInteger(num,parts):
    rem = num % parts
    q = int (num / parts)
    if rem == 0:
        return [q for i in range(parts)]
    else:
        res = [q for i in range(parts)]
        i = 0
        while rem > 0:
            res[i] = res[i] + 1
            i += 1
            rem -= 1
        return res

#print(splitInteger(20, 6))

def first_non_repeating_letter(str):
    if len(str) == 0:
        return ''
    dict = {}

    for i in str:
        i = i.lower()
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    for i in str:
        if dict[i.lower()] == 1:
            return i


#print(first_non_repeating_letter(""))

def find_processes(start_item,end_item,tasks):
    if start_item == end_item:
        return []
    s_dict = {}
    p_dict = {}
    for t in tasks:
        p, s, e = t.split(":")
        if s in s_dict:
            s_dict[s].append(p)
        else:
            s_dict[s] = [p]
        p_dict[p] = e

    res = []
    while start_item in s_dict:
        s_process = s_dict[start_item]
        res.append(s_process)
        if end_item == p_dict[s_process]:
            return res
        else:
            start_item = p_dict[s_process]

    return []


