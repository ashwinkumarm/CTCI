'''
Created on 04-Jun-2018

@author: Ashwin
'''
def pal_perm(str):
    
    char_count = [0 for _ in range(27)]
    
    for i in range(len(str)):
        if charToNum(str[i]) != -1:
            char_count[charToNum(str[i])] += 1
    
    check = True
        
    for i in char_count:
        if i % 2 != 0:
            if check:
                check = False
            else: 
                return False    
    
    return True

#To consider upper case and lower case as same alphabets
def charToNum(c):
    if c >= 'a' and 'z' >= c:
        return ord(c) - ord('a')
    
    elif c >= 'A' and 'Z' >= c:
        return ord(c) - ord('A')
    
    return -1

print(pal_perm('tact coa'))