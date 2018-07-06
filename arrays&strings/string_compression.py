'''
Created on 04-Jun-2018

@author: Ashwin
'''


def string_compression(str1):
    prev = str1[0]
    s = 1
    sb = []
    for c in range(1, len(str1)):
        if prev == str1[c]:
            s +=1
        else:
            sb.append(prev + str(s))
            s = 1
            prev = str1[c]
    
    sb.append(prev + str(s))
    fin_str = ''.join(sb)
    return fin_str if len(fin_str) < len(str1) else str1


print(string_compression("aabcccccaaa"))
print(string_compression("abcswf"))
