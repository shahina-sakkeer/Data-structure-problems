from collections import deque

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


class BinaryTree:
    def __init__(self):
        self.root=None

    def insert(self,data):          #insertion happens in the empty slot. so in insert fn we are checking for the empty slot
        new_node=Node(data)

        if self.root is None:
            self.root=new_node
            return

        q=deque([self.root])

        while q:
            current=q.popleft()     #popleft first value from the queue    

            if not current.left:           #if the current.left has not any value inside, add new node to it
                current.left=new_node
                return 
            else:
                q.append(current.left)          #if current.left already have value, append it to queue

            if not current.right:         #same checking like above is happening in right part also
                current.right=new_node
                return
            else:
                q.append(current.right)


    def inorder_traversal(self,node):      # self → the tree object (tree)   node → the current node we are visiting. firstly the node will be root
        if node:
            self.inorder_traversal(node.left)       #go to left by pausing the current node.left. if that node.left also have left, pause the current node.left and call the next node.left. whenever the node.left becomes none, it will come from back to front
            print(node.data,end=" ")
            self.inorder_traversal(node.right)


    def preorder_traversal(self,node):
        if node:
            print(node.data,end=" ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)


    def postorder_traversal(self,node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.data,end=" ")


    def tree_height(self,node):
        left_height=right_height=0

        if node.left is not None:
            left_height=self.tree_height(node.left)

        if node.right is not None:
            right_height=self.tree_height(node.right)

        return 1+max(left_height,right_height)


tree=BinaryTree()     
tree.insert(10)
tree.insert(13)
tree.insert(5)
tree.insert(23)
tree.insert(8)
tree.insert(11)
tree.insert(12)
tree.insert(1)


# tree.inorder_traversal(tree.root)       #we have to pass the root because the function should need to know from where to start
# tree.preorder_traversal(tree.root)
# tree.postorder_traversal(tree.root)
print(tree.tree_height(tree.root))



#CHECK WHEATHER 2 TREES ARE EQUAL OR NOT
# def check_equal(p,q):
#     if p is None and q is None:
#         return True
    
#     if p is None or q is None:
#         return False
    
#     if p.data!=q.data:
#         return False
    
#     return check_equal(p.left,q.left) and check_equal(p.right,q.right)    #it is checking like left subtree of p and left subtree of q. as well as right subtree of p and right subtree of q
#             #by passing p.left and q.left recusrsively, it means check_equal(p.left,q.left). p will become p.left and q becomes q.left

# lst1 = [10, 13, 23, 8, 5]          #make sure this part works or not
# lst2 = [10, 13, 23, 8, 5]

# t1 = BST()
# t2 = BST()

# for x in lst1:
#     t1.insert(x)

# for x in lst2:
#     t2.insert(x)


    