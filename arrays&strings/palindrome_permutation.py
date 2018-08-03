'''
Created on 04-Jun-2018

@author: Ashwin
'''


def pal_perm(str):
    char_count = [0 for _ in range(27)]
    
    for i in range(len(str)):
        if char_num(str[i]) != -1:
            char_count[char_num(str[i])] += 1
    
    check = True
        
    for i in char_count:
        if i % 2 != 0:
            if check:
                check = False
            else: 
                return False    
    
    return True


# To consider upper case and lower case as same alphabets
def char_num(c):
    if 'z' >= c >= 'a':
        return ord(c) - ord('a')
    
    elif 'Z' >= c >= 'A':
        return ord(c) - ord('A')
    
    return -1


print(pal_perm('tact coa'))
