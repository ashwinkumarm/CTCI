def magic_index(sd_list):
    return _magic_index_nd(sd_list, 0, len(sd_list)-1)


def _magic_index(sd_list, s, e):
    if s > e:
        return -1

    m = int((s + e) / 2)
    if sd_list[m] == m:
        return m
    elif sd_list[m] < m:
        return _magic_index(sd_list, m+1, e)
    else:
        return _magic_index(sd_list, s, m-1)


def _magic_index_nd(snd_list, s, e):
    if s > e:
        return -1

    m = int((s + e) / 2)
    if snd_list[m] == m:
        return m

    l = min(snd_list[m], m-1)
    l_value = _magic_index_nd(snd_list, s, l)
    if l_value > 0:
        return l_value

    r = max(snd_list[m], m + 1)
    r_value = _magic_index_nd(snd_list, r, e)

    return r_value



sd_list = [-10, -5, 2, 2, 2, 3, 4, 8, 9, 12, 13]
print(magic_index(sd_list))