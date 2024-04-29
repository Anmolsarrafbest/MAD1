class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class doubly_linked_list:
    def __init__(self):
        self.head = None
        self.last = None
      
    def insert_end(self,data):
        newnode = Node(data)
        newnode.prev = self.last
        if self.head == None:            
            self.head = newnode
            self.last = newnode
        else:
            self.last.next = newnode
            self.last = newnode
    def insert_at_pos(self,data,pos):
        curr=self.head
        count=1
        while curr.next!= None:
            if count ==pos:
                no=Node(data)
                no.prev=curr
                no.next=curr.next
                curr.next=no
            count+=1
            curr=curr.next    
        return  
    def __str__(self):
        curr=self.head
        result=''
        while curr != None:
            result=result+str(curr.data)+'->'
            curr=curr.next
        return result[:-2]
l=doubly_linked_list()
k=[1,4,56,86,23,5]
for i in k:
    l.insert_end(i)
print(l)    
l.insert_at_pos(2,2)
print(l)    