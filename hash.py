class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.ref=None


class HashTable:
    def __init__(self,capacity):
        self.capacity=capacity
        self.size=0
        self.table=[None] * capacity


    def _hash(self,key):
        return hash(key) % self.capacity     #note that hash() returns different numbers in different runs for securoty reasons. sometimes it will go to index 3 or index 0. 
    

    def display(self):
        for i in range(self.capacity):
            print(f"Index {i}:", end=" ")

            current=self.table[i]

            if current is None:
                print("Empty")
            else:
                while current is not None:
                    print(f"[{current.key}:{current.value}]", end=" -> ")
                    current=current.ref
                print("None")

    
    def insert(self,key,value):
        index=self._hash(key)

        if self.table[index] is None:
            self.table[index]=Node(key,value)
            self.size+=1
        else:
            current=self.table[index]
            while current is not None:   #travel through the LL until the current becomes None
                if current.key==key:     #in each node, check the key in the current == the given key.
                    current.value=value  #if above condition is true, update the current value with the given value
                    return
                current=current.ref     #when the above if condition fails, move to next node

            new_node=Node(key,value)
            new_node.ref=self.table[index]
            self.table[index]=new_node
            self.size+=1


    def search(self,key):
        index=self._hash(key)

        current=self.table[index]
        while current is not None:
            if current.key==key:
                return current.value
            current=current.ref
        
        print("key not found")
        return 
            

        
ht=HashTable(5)
ht.insert("apple",3)   
ht.insert("grape",4)  
print(ht.search("apple"))
print(ht.search("grape"))
ht.display() 