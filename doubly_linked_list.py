class Node:
    def __init__(self,data):  #by passing data it means that node should contain data as must. nref and pref is unnecessary
        self.data=data
        self.nref=None
        self.pref=None

class DoublyLL:      #also the linked list can be empty. thatswhy we didnt pass any parameter inside init
    def __init__(self):    #why the node,data is not passed here as a parameter because the function already contains self.head which is being used in every function methods in ll class
        self.head=None

    def printDLLforward(self):
        if self.head is None:
            print("DLL is empty")

        else:
            n=self.head

            while n is not None:
                print(n.data,"----><----",end=" ")
                n=n.nref

    def printDLLreverse(self):
        print()
        if self.head is None:
            print("D LList is empty")
        else:
            n=self.head

            while n.nref is not None:   #we need to go to the last node. no need to print any nodes other than last node. so check the n.nextrefernece is not None. Then only it will go to last
                n=n.nref    # increment that existing to next node till n.nref is none
            while n is not None:    #from the above while loop we will point to the last node. 
                print(n.data,"----><----",end=" ")   #print that data
                n=n.pref     # decrement that existing n to previous node.


    def insert_in_emptylist(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            print("Double ll is not empty")


    def add_at_beginning(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        
        else:
            new_node.nref=self.head  #assign the new node's nref as the existing head
            self.head.pref=new_node  #assign the existing head's as pref
            self.head=new_node
            return
        
    def add_at_end(self,data):
        new_node=Node(data)

        if self.head is None:
            self.head=new_node

        else:
            n=self.head

            while n.nref is not None:
                n=n.nref
            new_node.pref=n
            n.nref=new_node

    def add_after_node(self,data,x):
        if self.head is None:
            print("dll is empty")

        else:
            n=self.head
            while n is not None:
                if n.data==x:
                    break
                else:
                    n=n.nref
            if n is None:
                print("given node is not present in list")
            else:
                new_node=Node(data)
                new_node.pref=n
                new_node.nref=n.nref
                if n.nref is not None:  #it is checking whether we are adding the node after the last node. if not the below condition will work
                    n.nref.pref=new_node  #the current x --> nref ---> pref = newnode
                n.nref=new_node


    def add_before_node(self,data,x):
        if self.head is None:
            print("dll is empty")

        else:
            n=self.head

            while n is not None:
                if n.data==x:
                    break
                else:
                    n=n.nref
            
            if n is None:
                print("Given node is not present in ll")
            else:
                new_node=Node(data)
                new_node.nref=n      #this line is checking for adding before the 1st node and rest node
                new_node.pref=n.pref    #this line is checking for adding before the 1st node and rest node
                if n.pref is not None:   #if the node is adding before the rest node
                    n.pref.nref=new_node   #the current node's pref-->nref is equal to new node (is this for rest node)
                else:
                    self.head=new_node  #if the node is adding before the first node, set head as new_node
                n.pref=new_node   #this line is checking for adding before the 1st node and rest node


    def delete_from_begin(self):
        if self.head is None:
            print("not able to delete because list is empty")
        elif self.head.nref is None:  #it checks if the list contains only one node. 
            self.head=None
            print("the only one node is deleted")
        else:
            self.head=self.head.nref  #it will assign the head as current head's nref
            self.head.pref=None  #the changed self.head's pref is now pointing to None


    def delete_from_end(self):
        if self.head is None:
            print("not able to delete because list is empty")
        elif self.head.nref is None:
            self.head=None
            print("the only one node is deleted")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.pref.nref=None


    # def delete_by_value(self,x):
    #     if self.head is None:
    #         print("dll is empty")

    #     elif self.head.nref is None:  #check if the list contains only one node
    #         if self.head.data==x:   #if the only node is equal to the user provided node
    #             self.head=None
    #         else:
    #             print("Given node is not present the list")
        
    #     elif self.head.data==x:   #check if the node is first node
    #         self.head=self.head.nref
    #         self.head.pref=None
 
    #     else:     #condition checks if we want to delete any middle node
    #         n=self.head  
    #         while n.nref is not None:
    #             if n.data==x:
    #                 break
    #             else:
    #                 n=n.nref    #also keep in mind that the controller from while will come outside if n.nref becomes None or break statement becomes true
            
    #         if n.nref is not None:  #it checks the middle node. the node is present
    #             n.pref.nref=n.nref
    #             n.nref.pref=n.pref
    #         else:           #it means the controller is now become n.nref as none. that means the n is now pointing to last node
    #             if n.data==x:
    #                 n.pref.nref=None   #change the nref of pref of n to None
    #             else:
    #                 print("node is not present in the lst")


    def delete_by_value(self,x):
        if self.head is None:
            print("ll is empty")
            return

        if self.head.nref is None:
            if self.head.data==x:
                self.head=None
                print("deleted the one and only node")
            else:
                print("the given node is not present")
            return

        if self.head.data==x:
            self.head=self.head.nref
            self.head.pref=None
            return

    
        n=self.head
        while n is not None:
            if n.data==x:
                break
            n=n.nref

        if n is None:
            print("this not doesnot exists")
            return
        
        if n.nref is not None:
            n.pref.nref=n.nref
            n.nref.pref=n.pref
        else:
            n.pref.nref=None


    def middle_element(self):
        if self.head is None or self.head.nref is None:
            print("middle is not able to find")
            return
        
        print()
        slow=self.head
        fast=self.head

        while fast.nref is not None and fast.nref.nref is not None:
            slow=slow.nref
            fast=fast.nref.nref

        return slow.data
    

    def remove_middle(self):
        print()
        if self.head is None or self.head.nref is None or self.head.nref.nref is None:
            print("Node is unable to remove")
            return
        
        slow=self.head
        fast=self.head

        while fast.nref is not None and fast.nref.nref is not None:
            slow=slow.nref
            fast=fast.nref.nref

        slow.pref.nref=slow.nref
        slow.nref.pref=slow.pref


    def remove_duplicate(self):  #for sorted list
        if self.head is None:
            print("This list is empty")
            return
        
        n=self.head
        while n.nref is not None:
            if n.data==n.nref.data:
                n.nref=n.nref.nref
                n.nref.nref.pref=n.nref
            else:
                n=n.nref

        print("remove duplicate elements")      


    def check_palindrome(self):
        if self.head is None:
            return True  #empty list is a palindrome

        last=self.head

        while last.nref is not None:
            last=last.nref
        
        first=self.head
        while first!=last and first.pref != last is not None:    #palindrome should end when the pointers meets(ie becoming equal to) and donot cross first to last
            if last.data!=first.data:
                return False
            else:
                first=first.nref
                last=last.pref

        return True
            
        


dd=DoublyLL()

dd.insert_in_emptylist(7)
dd.add_at_beginning(45)
dd.add_at_end(102)
dd.add_at_end(14)
dd.add_after_node(22,14)
dd.add_after_node(99,14)
dd.add_before_node(11,45)
dd.add_before_node(78,14)
# dd.delete_from_begin()
# dd.delete_from_end()
# dd.delete_by_value(102)
# dd.remove_middle()
# dd.remove_duplicate()
print(dd.check_palindrome())
dd.printDLLforward()
# print("The middle element is : ", dd.middle_element())

# dd.printDLLreverse()

