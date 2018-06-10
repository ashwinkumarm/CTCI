'''
Created on 09-Jun-2018

@author: Ashwin
'''

from Node import Node

def isPalindrome(ll):
    slow = ll
    fast = ll
    stack = []
    while fast and fast.next:
        stack.append(slow.value)
        slow = slow.next
        fast = fast.next.next
    
    if fast:
        slow = slow.next
    
    while stack:
        if slow.value != stack.pop():
            return False
        slow = slow.next
    return True

root = Node(6,Node(1,Node(6)))

print(isPalindrome(root))