'''
Created on 04-Jun-2018

@author: Ashwin
'''


# with additional data structure
def is_unique_set(str):
    if len(str) > 128:
        return False

    s = set()
    for c in str:
        if c not in s:
            s.add(c)
        else:
            return False
    return True


# with additional data structure
def isUnique(str):
    if len(str) > 128:
        return False
    
    characters = [False for _ in range(128)]
    
    for c in str:
        if not characters[ord(c) - ord('a')]:
            characters[ord(c) - ord('a')] = True 
        else:
            return False
    return True

# without additional data structure and inplace sorting is allowed
def isUniqueWithoutAddDataStructure(str):
    if(len(str) > 128):
        return False
    
    prev = ''
    for c in sorted(str):
        if prev == c:
            return False
        prev = c
        
    return True


# print(isUnique('ashwina'))
# print(isUniqueWithoutAddDataStructure('ashwin'))
print(is_unique_set("ashwina"))