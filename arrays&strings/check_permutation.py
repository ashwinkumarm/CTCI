'''
Created on 04-Jun-2018

@author: Ashwin
'''


def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    
    char_count = [0 for _ in range(128)]
    
    for i in range(len(str1)):
        char_count[ord(str1[i]) - ord('a')] += 1
        char_count[ord(str2[i]) - ord('a')] -= 1
        
    for i in char_count:
        if i != 0:
            return False
        
    return True


print(check_permutation('dog', 'god'))

