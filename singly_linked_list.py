class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class LinkedList:
    def __init__(self):
        self.head=None   #initially set ll as empty

    def printLL(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n=self.head

            while n is not None:
                print(n.data,"----->",end=" ")  #self.head.data.   it means the head carries the reference of 1st node right. that address's data is printed
                n=n.ref  #it means the current node's reference is the self.head  

    def add_at_beginning(self,data):
        new_node=Node(data)    #create an object of the node which carries the data as parameter
        new_node.ref=self.head  #the new node's ref should now carry the existing self.head   
        self.head=new_node    #the self.head then should carry the new_node reference


    def add_at_end(self,data):
        new_node=Node(data)

        if self.head is None:  # checking wheather ll is empty
            new_node.ref=None
            self.head=new_node
        else:                 # if ll is not empty
            n=self.head

            while n.ref is not None:
                n=n.ref
                
            n.ref=new_node


    def add_after_node(self,data,x):
        n=self.head

        while n is not None:  #if the linked list is not empty
            if x==n.data:    #checking given x is equal to data inside self.head(internally it check wheather x is first node)
                break
            else:
                n=n.ref     #if x is not first node, migrate to the node till it reaches to the x node
        if n is None:
            print("This node is not existing in LL")
        else:
            new_node=Node(data) 
            new_node.ref=n.ref
            n.ref=new_node

    def add_before_node(self,data,x):

        if self.head is None:
            print("LL is empty")
            return

        if self.head.data==x:
            new_node=Node(data)
            new_node.ref=self.head
            self.head=new_node
            return
        
        n=self.head
        while n.ref is not None:
            if n.ref.data==x:       #here the we need to get the previous node of the given node. so we need to check x with n.ref.data
                break
            else:
                n=n.ref

        if n.ref is None:
            print("This node is not present in ll")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node


    def delete_node_beginning(self):
        if self.head is None:
            print("LL is empty")

        else:
            self.head=self.head.ref


    def delete_node_end(self):
        if self.head is None:
            print("List is empty")

        elif self.head.ref is None:
            self.head=None

        else:
            n=self.head

            while n.ref.ref is not None:
                n=n.ref
            n.ref=None


    def delete_node_between(self,x):
        if self.head is None:
            print("LL is empty to delete by value")

        else:
            if self.head.data==x:    #checking wheather we are deleting first node
                self.head=self.head.ref

            else:
                n=self.head
                while n.ref is not None:  #while loop is checking wheather the condition T/F. if true only proceeds else exit from that loop
                    if n.ref.data==x:
                        break
                    else:
                        n=n.ref    

                #now the n carries the previous node that we got from while loop    
                if n.ref is None:
                    print("Not possible to delete the node")
                else:
                    n.ref=n.ref.ref


    def reverse_ll(self):
        previous=None
        current=self.head

        while current is not None:
            next=current.ref
            current.ref=previous
            previous=current
            current=next

        self.head=previous


    def middle_element(self):
        if self.head is None or self.head.ref is None:
            print("list is not able to find middle")

        slow=self.head
        fast=self.head

        while fast is not None and fast.ref is not None:
            slow=slow.ref
            fast=fast.ref.ref

        return slow.data
    
    
    
    def remove_middle_element(self):
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
            print("List is empty")
            return
        
        n=self.head
        while n is not None:
            if n.data==x:
                break
            n=n.ref

        if n is None:
            print("This node doesnot exists")
        else:
            return n.data
        

    def remove_duplicate(self):
        if self.head is None:
            print("Dll is empty")
            return
        
        n=self.head
        while n.ref is not None:
            if n.data==n.ref.data:
                n.ref=n.ref.ref
            else:
                n=n.ref

        print("removed duplicates")


    def check_palindrome(self):
        if self.head is None:
            print("Sll is empty")
            return
        
        slow=self.head
        fast=self.head

        while fast.ref is not None and fast.ref.ref is not None:
            slow=slow.ref
            fast=fast.ref.ref

        previous=None
        current=slow.ref
        while current is not None:
            next=current.ref
            current.ref=previous
            previous=current
            current=next

        first_node=self.head
        second_node=previous
        while second_node is not None:
            if first_node.data!=second_node.data:
                return False
            
            else:
                first_node=first_node.ref
                second_node=second_node.ref

        return True


LL1=LinkedList()

LL1.add_at_beginning(90)    
LL1.add_at_beginning(71)
LL1.add_after_node(40,90)   #71 -----> 90 -----> 40 -----> 
LL1.add_at_end(80)          #71 -----> 90 -----> 40 -----> 80 -----> 
LL1.add_before_node(53,40)   #42 -----> 71 -----> 90 -----> 53 -----> 40 -----> 80 -----> 
LL1.add_at_beginning(42)
LL1.add_after_node(53,53)
LL1.add_at_end(80)
# LL1.delete_node_end()
# LL1.delete_node_between(90)
# LL1.delete_node_between(42)
# LL1.reverse_ll()
# print("Middle element is ",LL1.middle_element())
# print("Removed middle element : ", LL1.remove_middle_element())
# print("Searched element is : ", LL1.search_value(40))
# LL1.remove_duplicate()
# print(LL1.check_palindrome())
LL1.printLL()
