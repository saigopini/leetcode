"""
Building a stack
"""
class Stack():
    def __init__(self):
        self.stack = []

    def getLength(self):
        return len(self.stack)
    
    def isEmpty(self):
        return self.getLength() == 0
    
    def push(self, a):
        self.stack.append(a)

    def pop(self):
        if self.isEmpty() == False:
            elementRemoved = self.stack.pop()
            return elementRemoved
        else:
            return "Empty stack"
    
    def returnStack(self):
        return "".join(self.stack)
    

def removeStars(word):
    stack = Stack()
    for c in word:
        if c != "*":
            stack.push(c)
        else:
            stack.pop()
    
    return stack.returnStack()

print(removeStars("leet**cod*e"))
        
    