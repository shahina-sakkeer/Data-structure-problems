class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class Linkedlist:
    def __init__(self):
        self.head=None

    def printsingle(self):
        if self.head is None:
            print("Singly ll is empty")
            return
        
        n=self.head
        while n is not None:
            print(n.data,"---->",end="")
            n=n.ref

    def add_at_start(self,data):
        new_node=Node(data)
        if self.head is None:
            new_node.ref=None
            self.head=new_node
        else:
            new_node.ref=self.head
            self.head=new_node
            
    
    def add_at_end(self,data):
        new_node=Node(data)

        if self.head is None:
            new_node.ref=None
            self.head=new_node
            return
        
        n=self.head
        while n.ref is not None:
            n=n.ref
        new_node.ref=None
        n.ref=new_node

            
    def add_after_x(self,data,x):
        if self.head is None:
            print("Not possible to add node as ll is empty")
            return
        
        n=self.head
        while n is not None:
            if n.data==x:
                break
            else:
                n=n.ref

        if n is None:
            print("this node is not present")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node


    def add_before_x(self,data,x):
        if self.head is None:
            print("ll is empty")
            return
        
        if self.head.data==x:
            new_node=Node(data)
            new_node.ref=self.head
            self.head=new_node
            return
        
        n=self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            else:
                n=n.ref

        if n.ref is None:   #this condition should match with the while condition above
            print("node x is not present")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node

    def delete_start(self):
        if self.head is None:
            print("ll is empty")
            return
        
        if self.head.ref is None:
            self.head = None
            return
        
        self.head=self.head.ref

    def delete_end(self):
        if self.head is None:
            print("ll is empty")
            return
        
        if self.head.ref is None:
            self.head=None
            return
        
        n=self.head
        while n.ref.ref is not None:  #if we check n.nref is not none, it will reach to last node. but actually we need to change the ref of second last node
            n=n.ref

        n.ref=None


    def delete_x(self,x):   
        if self.head is None:
            print("ll is empty")
            return
        
        if self.head.data==x:    #you can also check wheather the dll contains only one node and that node is ==x . no problem. but it is unneccessary
            self.head=self.head.ref
            return
        
        n=self.head
        while n.ref is not None: 
            if n.ref.data==x:
                break
            n=n.ref

        if n.ref is None:     #this condition should match with the while condition above
            print("this node is not present")
        else:
            n.ref=n.ref.ref


    def reverse(self):
        previous=None
        current=self.head

        while current is not None:
            next=current.ref
            current.ref=previous
            previous=current
            current=next

        self.head=previous



    def middle(self):
        slow=self.head
        fast=self.head

        while fast is not None and fast.ref is not None:
            slow=slow.ref
            fast=fast.ref.ref

        return slow.data
    

    def remove_middle(self):
        if self.head is None:
            print("Not able to remove element")
            return
        
        if self.head.ref is None:
            self.head=None
            return

        previous=None
        slow=self.head
        fast=self.head

        while fast is not None and fast.ref is not None:   #why this condition because in 2 element node, fast.ref and fast.ref.ref will cause bug
            previous=slow
            slow=slow.ref
            fast=fast.ref.ref

        previous.ref=slow.ref


    
    def search_value(self,x):
        if self.head is None:
            print("cannot find the value")
            return
        
        n=self.head
        while n is not None:
            if n.data==x:
                break
            else:
                n=n.ref

        if n is None:
            print("x node doesnot exist")
        else:
            return n.data


    def remove_dupli_sorted(self):
        if self.head is None:
            print("ll is empty")
            return
        
        n=self.head
        while n.ref is not None:
            if n.data==n.ref.data:
                n.ref=n.ref.ref
            else:
                n=n.ref

        print("removed suucessfully")


    def remove_duplic_unsorted(self):
        if self.head is None:
            print("ll is empty")
            return
        
        seen=set()
        seen.add(self.head.data)  #add head node to set. otherwise if the head has duplicate, it will also get added to ll
        n=self.head

        while n.ref is not None:
            if n.ref.data not in seen:
                seen.add(n.ref.data)
                n=n.ref
            else:
                n.ref=n.ref.ref


    def remove_even_nodes(self):
        if self.head is None:
            print("list is empty")

        if self.head is not None and self.head.data%2==0:
            self.head=self.head.ref

        n=self.head
        while n.ref is not None:
            if n.ref.data %2 == 0:
                n.ref=n.ref.ref
            else:
                n=n.ref


    def add_at_index(self,data,x):
        n=self.head

        for i in range(x-1):
            n=n.ref
        
        new_node=Node(data)
        new_node.ref=n.ref
        n.ref=new_node

    
           


LL1=Linkedlist()
LL1.add_at_start(18)
LL1.add_at_start(45)
LL1.add_at_end(16)
LL1.add_at_end(56)
LL1.add_after_x(14,16)
LL1.add_at_end(15)
LL1.add_at_end(45)
LL1.add_before_x(30,45)
# LL1.delete_start()
# LL1.delete_end()
# LL1.delete_x(30)
# LL1.reverse()
print(LL1.middle())
# LL1.remove_middle()
# LL1.remove_dupli_sorted()
# LL1.remove_duplic_unsorted()
# LL1.remove_even_nodes()
LL1.printsingle()



#circular ll
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.ref=None

# class CLinkedlist:
#     def __init__(self):
#         self.head=None
        
#     def printcll(self):
#         if self.head is None:
#             print("cll is empty")
#             return
        
#         n=self.head
#         while n is not None:
#             print(n.data,"--->",end=" ")
#             n=n.ref
            
#             if n==self.head:
#                 break
                
#     def add_start(self,data):
#         new_node=Node(data)
#         if self.head is None:
#             new_node.ref=self.head
#             self.head=new_node
#             return
        
#         n=self.head
#         while n.ref!=self.head:
#             n=n.ref
            
#         new_node.ref=self.head
#         n.ref=new_node
#         self.head=new_node
        
        
# cll=CLinkedlist()
# cll.add_start(10)
# cll.printcll()
            