'''
Created on 04-Jun-2018

@author: Ashwin
'''
from __builtin__ import False

def oneAway(str1, str2):
    if len(str2) < len(str1):
        temp = str2
        str2 = str1
        str1 = temp
    
    if len(str2) - len(str1) > 1:
        return False
    
    if len(str2) == len(str1):
        c = 0
        for i in range(len(str1)):
            if c > 1:
                return False
            if str1[i] != str2[i]:
                c += 1
    else:
        c = 0
        j = 0
        i = 0
        while j < len(str1):
            if c > 1:
                return False
            if str1[j] == str2[i]:
                j += 1
                i += 1
            else:
                i += 1
                c += 1    
        
    return c <= 1

print(oneAway('pale','ple'))
print(oneAway('pales','pale'))
print(oneAway('pale','bale'))
print(oneAway('pale','bake'))

    