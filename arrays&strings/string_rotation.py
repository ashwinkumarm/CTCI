'''
Created on 04-Jun-2018

@author: Ashwin
'''


def string_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    
    s = s1 + s1
    return s.find(s2) != -1


print(string_rotation('waterbottle', 'erbottlewat'))