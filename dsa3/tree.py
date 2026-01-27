#=============TREE======================

class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]      #add children to the parent

    def add_child(self,child_data):
        self.children.append(TreeNode(child_data))      #it is not a recursive call. it is function call itself. that means creating child value in list children


    def print_tree(self,level=0):
        print(" " * 4*level,self.data)
        for child in self.children:       
            child.print_tree(level+1)


    def search_node(self,target):
        if self.data==target:
            return True
        
        for child in self.children:
            if child.search_node(target):            #each node have their children. their childern have their children and so on. so recursive solution
                return True

        return False
    

    def delete_node(self,target):
        for child in self.children:         #deletion must be done by the parent.child is the node we want to delete
            if child.data==target:          #self.data == target will not work. a node cannot delete by keeping that node itself.Only the parent can remove a child.So deletion must be handled at the parent level
                self.children.remove(child)
                return True
        
            if child.delete_node(target):       #if this line return true, the below line works
                return True
            
        return False


root=TreeNode("Electronics")
root.add_child("Laptop")
root.add_child("Mobile")
root.add_child("EarPhone")

root.children[0].add_child("Mac")
root.children[0].add_child("Hp Victus")
root.children[0].add_child("Msi thin 15")

root.children[1].add_child("Iphone")
root.children[1].add_child("Android")

root.children[2].add_child("Wireless")

# print(root.search_node("Iphone"))

# root.delete_node("EarPhone")
# root.delete_node("Hp Victus")
root.delete_node("Laptop")

root.print_tree()