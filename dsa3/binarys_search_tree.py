class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


    def insert(self,x):           #self means the "root" from root=Node(20). Always the initial comparing is done with root value
            if x==self.data:
                return
            
            if x<self.data:       #We compare the new data with the root value.
                if self.left is None:           #If it is less than the root and self.left is None, we insert the value directly to the left
                    self.left=Node(x)
                else:
                    self.left.insert(x)         #If self.left already has a value, then that left node becomes the parent, and we again compare the new data with that node.
                 #self.left.insert(x) when this is called, it will go to def insert(self,x): here the self now is not root it is root.left. so the self will be the child node.
            elif x>self.data:
                if self.right is None:
                    self.right=Node(x)
                else:
                    self.right.insert(x)          #This process continues recursively until we find an empty spot.that means until we find self.left is none or self.right is none


    def inorder_travel(self):       #left---root-----right
        if self.left is not None:
            self.left.inorder_travel()        #Ask left child to print first
        print(self.data,end=" ")              #print itself

        if self.right is not None:            
            self.right.inorder_travel()       #Ask right child to print


    def preorder_travel(self):           #root----left-----right
        print(self.data,end=" ")

        if self.left is not None:
            self.left.preorder_travel()
        if self.right is not None:
            self.right.preorder_travel()


    def postorder_travel(self):          #left----right-----root
        if self.left is not None:
            self.left.postorder_travel()    #when the recursive loop get fully completed, it will go to below if condition
        if self.right is not None:
            self.right.postorder_travel()

        print(self.data,end=" ")



    def search(self,target):
        print("\t")
        if self.data==target:           #check the target == root value
            print("Node found")
            return True
        
        if target<self.data:            #if target is less than the root, the element will appear in left side. so check only left position
            if self.left is None:       #two conditions are there in left side. Condn 1) check left is empty. if so print msg
                print("No Node is present in left subtree")
            else:
                self.left.search(target)        # Condn 2) if left is not empty, go to search function again. so calling self.left.search(target) means self.left becomes the self in def search(self,target). self.left will be the root now. and this recursive goes on until if found self.data==target
                
        else:
            if self.right is None:
                print("No node is present in right subtree")
            else:
                self.right.search(target)



    def delete(self,target):
        if self.data is None:
            print("tree is empty")
            return
        
        if target<self.data:
            if self.left is None:
                print("Given node is not present in the left tree")
            else:
                self.left=self.left.delete(target)

        elif target>self.data:
            if self.right is None:
                print("Given node is not present in the right tree")
            else:
                self.right=self.right.delete(target)

        else:                 #here target==self.data
            if self.left is None:            # 1) check wheather the current has only right node and no left node
                return self.right            #this will replace the current node with this self.right. this self.right is go back to self.right=self.right.delete(target)'s self.right bcoz that is the last condition called. if 20 need to remove and 30 is the right subtree.Delete 20 → 30 becomes the new root.
            
            if self.right is None:           # 2) check wheather the current has only left node and no right node
                return self.left             #this will replace the current node with this self.left. this self.left is go back to self.left=self.left.delete(target)'s self.left bcoz that is the last condition called
            
            node=self.right                  # 3) if node has 2 children/target=root. It finds the smallest value in the right subtree.
            while node.left is not None:                 #why node.left because the smallet value will present at left side
                node=node.left

            self.data=node.data              #now current node will be there but its value get replaced with last left subtree node value
            self.right=self.right.delete(node.data)          #Because that successor value now exists twice,we remove it from the right subtree.

        return self          #Returns the updated subtree root to the parent


    def minimum_node(self):
        print()
        current=self         #take root node as current. the minimum node will be present at left side. the minimum value will be the leaf node on left side

        while current.left is not None:     #if current have left child present. this loop will iterate until the current.left is None 
            current=current.left            #the current is now changed to current.left. 

        return current.data                 #return the leaf node on left side
    

    def maximum_node(self):
        print()

        current=self

        while current.right is not None:
            current=current.right

        return current.data
    

    def valid_bst(self,min_val=float("-inf"),max_val=float("inf")):           #firstly initialise min and max value in its peek 
        if not min_val<self.data<max_val:           #if the node data breaks bst rule, then it is not valid bst
            return False
        
        left_side=True            #assume valid in the first hand
        right_side=True
        
        if self.left is not None:               #if the self.left has values
            left_side=self.left.valid_bst(min_val,self.data)         #self.left.valid_bst(min_val,self.data) ===> it means max_val will be upto the root node value. ie if root=20. the left child should be upto 20 an dnot greater than 20

        if self.right is not None:   
            right_side=self.right.valid_bst(self.data,max_val)        #the min_val= from the self.data to whatever greater. it cannot be lessthan self.data

        return left_side and right_side


    
    def tree_height(self):
        left_height=right_height=0        #initailise the values with 0

        if self.left is not None:
            left_height=self.left.tree_height()      #calculate the 

        if self.right is not None:
            right_height=self.right.tree_height()

        return 1+max(left_height,right_height)
    

    def kth_largest(self,k):          #we are using inorder travel in reverse order to find the largest ones. here largest ones will appear at the first
        self.count=0          #to track how many nodes we have visited
        self.ans=None         #to store the kth largest value

        def inorder_reverse(node):
            if node is None or self.count>=k:          #when tree ended or already reaches kth value
                return
            
            inorder_reverse(node.right)           #go to right first

            self.count+=1
            if self.count==k:         #we found the answer
                self.ans=node.data
                return
            
            inorder_reverse(node.left)          #go to left

        inorder_reverse(self)
        return self.ans
    

    def kth_smallest(self,k):
        self.count=0
        self.ans=None

        def inorder_travel(node):
            if node is None or self.count>=k:
                return
            
            inorder_travel(node.left)
            
            self.count+=1
            if self.count==k:
                self.ans=node.data
                return
            
            inorder_travel(node.right)

        inorder_travel(self)
        return self.ans



root=Node(20)
root.insert(33)
root.insert(29)
root.insert(6)
root.insert(50)
root.insert(21)
# root=root.delete(6)
# root=root.delete(21)
# root.inorder_travel()
# root.preorder_travel()
# root.postorder_travel()
# root.search(11)
# root.search(29)
# root.search(50)
# print("Minimum node is : ",root.minimum_node())
# print("Maximum node is : ",root.maximum_node())

# if root.valid_bst():
#     print("Valid BST")
# else:
#     print("Not valid")
# print("Maximum height of the tree : ",root.tree_height())

# print(root.kth_largest(3))
# print(root.kth_smallest(3))
