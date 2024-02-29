"""
Building a stack using both list and linkedlist implementations
"""
from node import Node

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

class StackLinkedList():
    def __init__(self):
        self.head = None
        self.length = 0

    def traverseList(self):
        output = ""
        current = self.head 
        while current:
            output += str(current.dataval) + " ---> "
            current = current.nextval
        output += " ---> None "
    
    def push(self, data): #inserts at back
        if self.head == None:
            self.head = Node(data, None)
        else:
            current = self.head
            while current.nextval:
                current = current.nextval
            current.nextval = Node(data, None)
        self.length += 1
    
    def pop(self): #remove from the back
        if self.head == None:
            return "Empty list"
        else:
            current = self.head
            counter = 0
            while counter < self.length - 1 and current:
                current = current.nextval
                counter += 1
            current.nextval = None
            self.length -= 1
    
    
    


def removeStars(word):
    stack = Stack()
    for c in word:
        if c != "*":
            stack.push(c)
        else:
            stack.pop()
    
    return stack.returnStack()

print(removeStars("leet**cod*e"))
        
    