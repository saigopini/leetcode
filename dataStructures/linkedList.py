from node import Node

class LinkedList():

    def __init__(self):
        self.head = None
        self.length = 0
    
    def isEmpty(self):
        if self.head == None:
            return True
        return False

    def traverseList(self):
        output = ""
        if self.isEmpty() == False:
            current = self.head
            while current:
                output += str(current.dataval) + ' ----> '
                current = current.nextval
            output += 'None'
            print(output)
        else:
            print("linked list is empty")
    
    def insertAtFront(self, data):
        #set node to point at self.head/rest of linked list
        node = Node(data, self.head) 
        #self.head is now 
        self.head = node
        self.length += 1
    
    def insertAtBack(self, data):
        current = self.head
        while current.nextval:
            current = current.nextval
        current.nextval = Node(data, None)
        self.length += 1

    def insertAtMiddle(self, data, posAfter):
        current = self.head
        while current:
            if current.dataval == posAfter:
                temp = current.nextval
                current.nextval = Node(data, temp)
                break
            current = current.nextval
        self.length += 1
  
    def deleteAtMiddle(self, data):
        if self.isEmpty() == True: return
        current = self.head
        while current.dataval != data:
            current = current.nextval
        if current.dataval != data:
            return str(data) + " does not exist in linkedlist"
        temp = current.nextval
        current.dataval = temp.dataval
        current.nextval = temp.nextval
        self.length-=1
    
    def deleteAtMiddleElement(self):
        if self.isEmpty() == True: return
        prev = None
        slow, fast = self.head, self.head
        while fast and fast.nextval:
            prev = slow
            slow = slow.nextval
            fast = fast.nextval.nextval
        prev.nextval = slow.nextval     
        self.length -= 1
    
    def deleteAtEnd(self):
        if self.isEmpty() == True: return
        current = self.head
        prev = self.head
        counter = 1
        while counter < self.length-1 and current.nextval:
            prev = current
            current = current.nextval
            counter +=1
        current.nextval = None
        self.length -= 1
    
    def deleteAtEnd2(self):
        if self.isEmpty() == True: return
        prev = self.head
        current = self.head
        while current.nextval:
            prev = current
            current = current.nextval
        prev.nextval = None
        self.length -= 1


    def deleteAtFront(self):
        if self.isEmpty() == True: return
        self.head = self.head.nextval
        self.length -= 1
    
    def reverseList(self):
        current = self.head
        prev = None
        #use two pointers, prev and current
        #prev keeps track of what current used to point to and sets it to the current
        while current:
            nxt = current.nextval
            current.nextval = prev #current.next is pointing to prev
            prev = current
            current = nxt
        self.head = prev

    def printLength(self):
        print(self.length)
    
l = LinkedList()
l.insertAtFront("a")
l.insertAtFront('p')

l.insertAtMiddle("c", "a")
l.insertAtBack("k")
l.traverseList()
l.reverseList()
l.traverseList()
print("delete end")
l.deleteAtEnd()
l.traverseList()
print("delete end")
l.deleteAtEnd2()
l.traverseList()

l.printLength()









            




