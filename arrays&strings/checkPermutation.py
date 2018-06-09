'''
Created on 04-Jun-2018

@author: Ashwin
'''

def checkPermutation(str1, str2):
    if len(str1) != len(str2):
        return False
    
    charCount = [0 for _ in range(128)]
    
    for i in range(len(str1)):
        charCount[ord(str1[i]) - ord('a')] += 1
        charCount[ord(str2[i]) - ord('a')] -= 1
        
    for i in charCount:
        if i != 0:
            return False
        
    return True

print(checkPermutation('dog', 'god'))

