class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

obj1=Node(20)
obj2=Node(30)
obj3=Node(40)
obj4=Node(50)
obj1.next=obj2
obj2.next=obj3
obj3.next=obj4

curr=obj1
while curr!=None:
    print(curr.data,end="-->")
    curr=curr.next
    