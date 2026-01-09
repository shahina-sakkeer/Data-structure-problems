class Node:
    def __init__(self,data):
        self.data=data
        self.nref=None
        self.pref=None

class DoubleLinkedlist:
    def __init__(self):
        self.head=None

    def printdll(self):
        if self.head is None:
            print("doubly linked list is empty")
            return
        
        n=self.head
        while n is not None:
            print(n.data,"----->><<-----",end="")
            n=n.nref

    def insert_to_empty(self,data):
        new_node=Node(data)

        if self.head is None:
            self.head=new_node


    def add_at_start(self,data):
        new_node=Node(data)

        if self.head is None:
            self.head=new_node
            return
        
        new_node.nref=self.head
        self.head.pref=new_node
        self.head=new_node


    def add_at_end(self,data):
        new_node=Node(data)

        if self.head is None:
            self.head=new_node
            return
        
        n=self.head
        while n.nref is not None:
            n=n.nref

        new_node.pref=n
        new_node.nref=None
        n.nref=new_node


    def add_before_x(self,data,x):
        if self.head is None:
            print("cannot add x node")
            return
        if x==self.head.data:
            new_node=Node(data)
            new_node.nref=self.head
            self.head.pref=new_node
            self.head=new_node
            return
        
        n=self.head
        while n is not None:
            if n.data==x:
                break
            else:
                n=n.nref

        if n is None:
            print("x node is not found")
            return

        new_node=Node(data)
        new_node.nref=n
        new_node.pref=n.pref
        n.pref.nref=new_node
        n.pref=new_node


    def add_after_x(self,data,x):
        if self.head is None:
            print("cannot add x node")
            return
        
        n=self.head
        while n is not None:
            if n.data==x:
                break
            else:
                n=n.nref

        if n is None:
            print("x is not present")
            return
        new_node=Node(data)
        new_node.pref=n
        new_node.nref=n.nref
        if n.nref is not None:   #checking if the x is not last element
            n.nref.pref=new_node
        n.nref=new_node


    def delete_begin(self):
        if self.head is None:
            print("cannot delete empty list")
            return
        
        if self.head.nref is None:
            self.head=None
            return
        
        self.head=self.head.nref
        self.head.pref=None


    def delete_end(self):
        if self.head is None:
            print("cannot delete empty list")
            return
        
        if self.head.nref is None:
            self.head=None
            return
        
        n=self.head
        while n.nref is not None:
            n=n.nref

        n.pref.nref=None
        n.pref=None
        
    
    def delete_x(self,x):
        if self.head is None:
            print("cannot delete empty list")
            return
        if self.head.data==x and self.head.nref is None:
            self.head=None
            return
        if self.head.data==x:
            self.head=self.head.nref
            self.head.pref=None
            return
        
        n=self.head
        while n is not None:
            if n.data==x:
                break
            else:
                n=n.nref

        if n is None:
            print("x is not present to delete")
            return
        
        n.pref.nref=n.nref
        if n.nref is not None:
            n.nref.pref=n.pref


    def reverse(self):
        if self.head is None:
            print("D LList is empty")
            return
        
        previous=None
        current=self.head

        while current is not None:
            current.pref,current.nref=current.nref,current.pref

            previous=current
            current=current.pref

        self.head=previous


    def middle(self):
        if self.head.nref is None:
            print("not able to find middle as only one node exists")
            return
        
        slow=self.head
        fast=self.head

        while fast is not None and fast.nref is not None:
            slow=slow.nref
            fast=fast.nref.nref

        return slow.data
    

    def remove_middle(self):
        if self.head is None:
            print("no eleements are present in the dll")
            return
        
        slow=self.head
        fast=self.head

        while fast is not None and fast.nref is not None:
            slow=slow.nref
            fast=fast.nref.nref

        slow.pref.nref=slow.nref
        slow.nref.pref=slow.pref


    def remove_dupli_sorted(self):
        if self.head is None:
            print("no eleements are present in the dll")
            return
        
        n=self.head

        while n.nref is not None:
            if n.data==n.nref.data:
                n.nref.nref.pref=n.nref
                n.nref=n.nref.nref
                
            else:
                n=n.nref


    

    def check_palind(self):
        if self.head is None:
            return False
        
        slow=self.head
        fast=self.head

        while fast.nref is not None:
            fast=fast.nref

        while slow!=fast:
            if slow.data != fast.data:
                return False
            else:
                slow=slow.nref
                fast=fast.pref

        return True




DLL1=DoubleLinkedlist()
# DLL1.insert_to_empty(8)
# DLL1.add_at_start(78)
# DLL1.add_at_start(20)
# DLL1.add_before_x(15,20)
# DLL1.add_before_x(20,78)
# DLL1.add_after_x(9,78)
# DLL1.add_at_end(9)
# DLL1.delete_begin()
# DLL1.delete_end()
# DLL1.delete_x(9)
# DLL1.reverse()
# print("middle element is ",DLL1.middle())
# DLL1.remove_middle()
DLL1.add_at_start(10)
DLL1.add_at_start(20)
DLL1.add_at_start(30)
DLL1.add_at_start(20)
DLL1.add_at_start(10)
# DLL1.add_before_x(30,20)
# DLL1.remove_dupli_sorted()
print(DLL1.check_palind())
DLL1.printdll()
