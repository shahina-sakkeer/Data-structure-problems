class Minheap:                   #in min heap, parent value of a particular child will be less than its child values(left and right)
    def __init__(self):          #when inserting new node, if child value<parent value, swap them. here iteration is going from down to up(heapify_up)
        self.heap=[]

    def parent(self,i):
        return (i-1) // 2        #return index value of parent
    
    def left(self,i):
        return 2*i + 1           #return index value of left child
    
    def right(self,i):
        return 2*i + 2           #return index value of right child
    
    def insert(self,value):
        self.heap.append(value)
        self._heapify_up(len(self.heap)-1)          #pass the index value of the last added element
    
    def _heapify_up(self,index):          #this method is called when a new value is inserted
        while index> 0 and self.heap[index]<self.heap[self.parent(index)]:          # loop will run till the root node. and when the parent node < child node (ppty of min heap)
            self.heap[index],self.heap[self.parent(index)]=self.heap[self.parent(index)],self.heap[index]          #compare child value and parent value.if child val is less than parent val. if so, swap parent value with child value
            index=self.parent(index)         #after swapping new added value becomes the parent. because after the above step, the newly added node comes to up.so it becomes parent


    def delete_root(self):
        if len(self.heap)==0:      #checking no elements are there
            print("no elements to delete !")
            return
        
        if len(self.heap)==1:         #if only 1 element exist, pop() it
            self.heap.pop()
            return
         
        root=self.heap[0]         #we can only delete root, place first element to a variable "root".
        self.heap[0]=self.heap.pop()          #pop the last element and place it on the vacant self.heap[0]
        self._heapify_down(0)
        return root               #return the delete element(just to show)
    
    #note that when we delete root node, last element will come to the first node. so the above method is for rearranging the parent node only. all other node will be in its valid state. dont think about that.

    def _heapify_down(self,index):        #top------bottom
        smallest=index      #added the index 0 to the variable smallest.assume current node is the smallest. just like how we do selection sort/how we find maximum value from a list
        left=self.left(index)           #calling left fn
        right=self.right(index)         #calling right fn


        if left<len(self.heap) and self.heap[left]<self.heap[smallest]:     #this is not base condition. it is checking left child value is less than the parent
            smallest=left         #if so, smallest is changed to left child. left,right,smallest are index values

        if right<len(self.heap) and self.heap[right]<self.heap[smallest]:     #now the smallest has left child, it is now checking with right child value
            smallest=right

        if smallest!=index:           #from the top we will get the smallest. if it is not equal to index 0, swap. this is the base condition is smallest==index
            self.heap[index],self.heap[smallest]=self.heap[smallest],self.heap[index]           #So the smaller value moves up, and the bigger value moves down.
            self._heapify_down(smallest)           #Now the bigger value has moved down. now check gain Is it still bigger than its new children.So we repeat the same process for that position.

        #why recursion here because we are travelling from top to bottom and we dont know where it will stop. it should stop when the heap property is completlt fine or when it reaches to leaf node


    def min_to_maxheap(self):          #(n//2)-1 when calculating this we will get a parent node of our leaf node
        n=len(self.heap)
        for i in range((n//2)-1,-1,-1):        #going to the leaf node of the tree. because leaf node will be always valid. compare child node with parent. in max heap parent will be greater than children
            self._heapify_down1(i)         #even if it is down to top, why dont we use heapify up because we use it for a new node is inserted. it only change last node. here we need to change all nodes


    def _heapify_down1(self,index):        #even the name is heapify down, the job is doing from bottom to top   
        largest=index
        left=self.left(index)
        right=self.right(index)

        if left<len(self.heap) and self.heap[left]>self.heap[largest]:
            largest=left

        if right<len(self.heap) and self.heap[right]>self.heap[largest]:
            largest=right

        if largest!=index:
            self.heap[index],self.heap[largest]=self.heap[largest],self.heap[index]
            self._heapify_down1(largest)


    def display(self):
        return self.heap
    


# myheap=Minheap()
# myheap.insert(8)
# myheap.insert(99)
# myheap.insert(18)
# myheap.insert(10)
# myheap.insert(3)
# myheap.insert(11)
# # myheap.delete_root()
# # myheap.min_to_maxheap()
# myheap.sort_heap_asc()
# print(myheap.display())



def heapify(lst,n,index):
    largest=index
    left=(2*index)+1
    right=(2*index)+2

    if left<n and lst[left]>lst[largest]:
        largest=left

    if right<n and lst[right]>lst[largest]:
        largest=right

    if largest!=index:
        lst[index],lst[largest]=lst[largest],lst[index]
        heapify(lst,n,largest)


def heap_sort(lst):
    n=len(lst)

    for i in range((n//2)-1,-1,-1):
        heapify(lst,n,i)

    for i in range(n-1,0,-1):
        lst[0],lst[i]=lst[i],lst[0]
        heapify(lst,i,0)    
