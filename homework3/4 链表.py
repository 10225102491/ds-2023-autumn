class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
        
    def add(self,item):
        item = Node(item)
        if self.head == None:
            self.head=item
            self.tail=item
        else:
            self.tail.next=item
            self.tail=item
        self.length+=1
        
    def dlt(self,id):
        if id >= self.length:
            return -1
        if id == 0:
            self.head=self.head.next
        else:
            t=self.head
            for i in range(id-1):
                t=t.next
            t.next=t.next.next
        return 0
    
    def get_data(self,id):
        if id >= self.length:
            return -1
        t=self.head
        for i in range(id):
            t=t.next
        return(t.data)
    
    def change(self,id,data):
        if id >=self.length:
            return -1
        t=self.head
        for i in range(id):
            t=t.next
        t.data=data
        return 0
    
    def show(self):
        t=self.head
        while t != None:
            print(t.data,end=' ')
            t=t.next
        print("")
