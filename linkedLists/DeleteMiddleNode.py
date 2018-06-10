'''
Created on 09-Jun-2018

@author: Ashwin
'''

def delMiddleNode(node):
    if node == None or node.next == None:
        return False
    
    node.value = node.next.value
    node.next = node.next.next
    return True