'''
Created on 04-Jun-2018

@author: Ashwin
'''

def urlIfy(str, length):
    str_list = list(str)
    reqLen = len(str_list)
        
    for i in range(length-1, -1, -1):
        if str_list[i] == ' ':
            str_list[reqLen-1] = '0'
            str_list[reqLen-2] = '2'
            str_list[reqLen-3] = '%'
            reqLen -= 3
        else:
            str_list[reqLen - 1] = str_list[i]
            reqLen -= 1    
    return str_list

print(urlIfy('Mr John Smith    ', 13))
                
    