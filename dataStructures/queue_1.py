#building queue
#first in, first out, append at the front, delete at front
from node import Node
class Queue():
    def __init__(self):
        self.queue = []

    def getLength(self):
        return len(self.queue)
    
    def traverseQueue(self):
        output = ""
        for i in range(self.getLength()):
            output += str(self.queue[i]) + " ---> "
        output += " ---> None"
        print(output)
    
    def push(self, data): #insert always at the front
        self.queue.insert(0, data)
    
    def pop(self): #removes at the front
        if self.getLength == 0: return "Empty Queue"
        del self.queue[0]

class QueueLinkedList():
    def __init__(self):
        self.head = None
        self.length = 0

    def traverseQueue(self):
        output = ""
        current = self.head
        while current:
            output += str(current.dataval) + " ---> "
            current = current.nextval
        output += " None "
        print(output)

    def push(self, data):
        node = Node(data, self.head)
        self.head = node
        self.length += 1
    
    def pop(self): #remove at the front
        if self.head == None: return "Empty list"
        self.head = self.head.nextval
        self.length -=1

    
    
q = QueueLinkedList()
q.push("n")
q.push("i")
q.push("l")
q.push("r")
q.push("e")
q.push("m")
q.traverseQueue()
q.pop()
q.pop()
q.traverseQueue()



