'''
Created on 04-Jun-2018

@author: Ashwin
'''


def url_ify(s, length):
    str_list = list(s)
    req_len = len(str_list)

    for i in range(length-1, -1, -1):
        if str_list[i] == ' ':
            str_list[req_len-1] = '0'
            str_list[req_len-2] = '2'
            str_list[req_len-3] = '%'
            req_len -= 3
        else:
            str_list[req_len - 1] = str_list[i]
            req_len -= 1
    return str_list


print(url_ify('Mr John Smith    ', 13))