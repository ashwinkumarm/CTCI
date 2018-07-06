class Stack:

    def __init__(self):
        self.items = []
            
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, x):
        self.items.append(x)
    
    def pop(self):
        if not self.items:
            raise Exception('Empty Stack')
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
