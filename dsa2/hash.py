# ///////--------------CUSTOM IMPLEMENTATION OF HASHING----------------/////////

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
            print("index",i,end="--->")

            n=self.table[i]

            if n is None:
                print("Empty")
            else:
                while n is not None:
                    print(n.key,":",n.value,end=" ")
                    n=n.ref
                print()

    
    def insert(self,key,value):      #insertion and updation  
        index=self._hash(key)

        if self.table[index] is None:    #self.table[index] is the head of the linkedlist.
            self.table[index]=Node(key,value)
            self.size+=1

        else:
            n=self.table[index]
            while n is not None:   #travel through the LL until the current becomes None
                if n.key==key:     #in each node, check the key in the current == the given key.
                    n.value=value  #if above condition is true, update the current value with the given value
                    return
                n=n.ref     #when the above if condition fails, move to next node

            new_node=Node(key,value)         #if no key is present with the given key, we need to add new_node. new_node will be always added at the begining of ll. because when we add at the end, it will increase the time complexity.
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
        
        return None
  

    def remove(self,key):
        index=self._hash(key)

        previous=None
        n=self.table[index]

        while n is not None:
            if n.key==key:
                if previous is None:         #if the first key is the target
                    self.table[index]=n.ref          
                else:
                    previous.ref=n.ref       #if the target was not the firdt key

                self.size-=1
                return
                
            previous=n
            n=n.ref

        print("key not found")


    def remove_duplicates(self,s):
        temp_hash=HashTable(50)    #Use a separate HashTable for duplicate removal. if we are not doing like this, each caharacters will get polluted with other values and keys in hash table
        result=""
        for ch in s:
            if temp_hash.search(ch) is None:     #we are not calling the main class. we are calling the temporary class. thats why no self here. also this line will check wheather the ch is not there in hashtable. then only it will get inside. otherwise skip
                temp_hash.insert(ch,True)        #if ch is not in hashtable, add it to table. note that in these logic, we are adding only valid things. not adding any invalid. here it is duplicates
                result=result+ch                 #at the same time add it to result also.(same method that we have done in array/string)

        return result
    

    def first_nonrepeat_char(self,s):
        freq=HashTable(50)    #this is a dictionary creation

        for ch in s:
            value=freq.search(ch)

            if freq.search(ch) is None:     #this is scratch creation
                freq.insert(ch,1)
            else:
                freq.insert(ch,value+1)

        for i in s:
            if freq.search(i)==1:
                return i
            

    def two_sum(self,lst,target):    #it wil work for sorted and unsorted array
        temp_hash=HashTable(50)

        for i in range(len(lst)):
            current=lst[i]
            compliment=target-current

            index=temp_hash.search(compliment)    #the lst value is considered as key and index as value
            if index is None:             #if the value got from above line is not present in the hashtable temp_hash 
                temp_hash.insert(current,i)
            else:
                return (index,i)    #index=the previous element index of hash table. i=current element index



        
ht=HashTable(10)
ht.insert("apple",3)   
ht.insert("grape",4)  
ht.insert("orange",8)
ht.insert("mango",5)
# print(ht.search("apple"))
# print(ht.search("grape"))
# print(ht.search("gra"))
# ht.remove("mango")
# ht.remove("yyyy")
ht.display() 
print(ht.remove_duplicates("programming"))
print(ht.first_nonrepeat_char("swiss"))
print(ht.two_sum([15, 11, 7, 2],9))



# ///////////----------HASH TABLE USING PYTHON DICTIONARY--------------///////////

# class HashTable:
#     def __init__(self):
#         self.table={}

#     def display(self):
#         return self.table

#     def insert(self,key,value):
#         self.table[key]=value

#     def search(self,key):
#         return self.table.get(key,None)
    
#     def remove(self,key):
#         if key in self.table:
#             del self.table[key]



    # def remove_duplicate(self,s):
    #     temp_h=Hashtable()
    #     result=""

    #     for ch in s:
    #         if temp_h.search(ch) is None:
    #             temp_h.insert(ch,True)
    #             result+=ch

    #     return result


    # def first_nonrepeat_char(self,s):
    #     res={}

    #     for i in s:
    #         if i not in res:
    #             res[i]=1
    #         else:
    #             res[i]=res[i]+1

    #     for ch in s:
    #         if res[ch]==1:
    #             return ch


# h1=HashTable()
# h1.insert("key1",55)
# h1.insert("key2",60)
# h1.insert("key1",30)
# print(h1.display())
# print(h1.remove_duplicate("progrramingg"))
# print(h1.first_nonrepeat_char("swiss"))