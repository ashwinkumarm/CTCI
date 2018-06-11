'''
Created on 08-Jun-2018

@author: Ashwin
'''

from TreeNode import TreeNode

class BinarySearchTree:
    
    def __init__(self):
        self.root = None
        self.size = 0
        
    def length(self):
        return self.size
    
    def __len__(self):
        return self.size
    
    def __iter__(self):
        self.root.__iter__()
    
    def put(self, key, val):
        if self.root == None:
            self.root = TreeNode(key, val)
        else:
            self.root = self._put(key, val, self.root)
        
        self.size += 1
        
    def _put(self, key, val, node):
        if key < node.key:
            if node.hasLeftChild():
                node.left = self._put(key, val, node.left)
            else:
                node.left = TreeNode(key, val, parent = node)
        elif key > node.key:
            if node.hasRightChild():
                node.right = self._put(key, val, node.right)
            else:
                node.right = TreeNode(key, val, parent = node) 
            
        return node
    
    def __setitem__(self, key, value):
        self.put(key,value)
        
    def get(self, key):
        if self.root.key == key:
            return self.root.value
        else:
            self._get(key, self.root)
    
    def _get(self, key, node):
        if node == None:
            return None
        
        if node.key > key:
            return self._get(key, node.left)
        elif node.key < key:
            return self._get(key, node.right)
        else:
            return node.value
        
    def __getitem__(self, key):
        return self.get(key)
    
    def __contains__(self, key):
        if self.get(key):
            return True
        else:
            return False
        
    def delete(self, key):
        if key == self.root.key:
            root = None
            return root
        else:
            self._delete(key, self.root)
    
    def _delete(self, key, node):
        nodeToRemove = self._get(key, node)
        if nodeToRemove:
            if nodeToRemove.hasBothChildrens():
                nodeToRemove.value = self.findMin(nodeToRemove.right).value
                nodeToRemove.right = self._delete(key, node.right)
            else:
                nodeToRemove = node.left if node.right is None else node.right

    def inOrderTraversal(self):
        if self:
            self.inOrderTraversal(self.left)
            print(self.key)
            self.inOrderTraversal(self.right)

    def preOrderTraversal(self):
        if self:
            print(self.key)
            self.inOrderTraversal(self.left)
            self.inOrderTraversal(self.right)

    def postOrderTraversal(self):
        if self:
            self.inOrderTraversal(self.left)
            self.inOrderTraversal(self.right)
            print(self.key)
                
        
    
    
bstTree = BinarySearchTree()
bstTree[10] = "ten"
bstTree[5] = "five"
bstTree[1] = "one"
bstTree[3] = "three"
bstTree[15] = "fifteen"
bstTree[19] = "nineteen"

print(bstTree[10])

if 10 in bstTree:
    print('10')
if 20 in bstTree:
    print('20')
    