'''
Created on 08-Jun-2018

@author: Ashwin
'''
class TreeNode:
    
    def __init__(self, key, value, left, right, parent):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
    
    def hasChildrens(self):
        return self.left or self.right
    
    def hasLeftChild(self):
        return self.left
    
    def hasRightChild(self):
        return self.right
    
    def isLeftChild(self):
        return self.parent.left == self.left
    
    def isRightChild(self):
        return self.parent.right == self.right    