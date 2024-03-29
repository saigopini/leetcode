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
    
    def enqueue(self, data): #insert always at the front
        self.queue.insert(0, data)
    
    def dequeue(self): #removes at the front
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

    def enqueue(self, data):
        node = Node(data, self.head)
        self.head = node
        self.length += 1
    
    def dequeue(self): #remove at the front
        if self.head == None: return "Empty list"
        self.head = self.head.nextval
        self.length -=1

    
    
q = QueueLinkedList()
q.enqueue("n")
q.enqueue("i")
q.enqueue("l")
q.enqueue("r")
q.enqueue("e")
q.enqueue("m")
q.traverseQueue()
q.dequeue()
q.dequeue()
q.traverseQueue()
