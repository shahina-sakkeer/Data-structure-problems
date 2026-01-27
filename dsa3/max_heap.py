class Maxheap:
    def __init__(self):
        self.heap=[]

    def parent(self,i):
        return (i-1)//2
    
    def left(self,i):
        return (2*i)+1
    
    def right(self,i):
        return (2*i)+2


    def insert(self,value):
        self.heap.append(value)
        self._heapify_up(len(self.heap)-1)

    
    def _heapify_up(self,index):
        while index>0 and self.heap[index]>self.heap[self.parent(index)]:
            self.heap[index],self.heap[self.parent(index)]=self.heap[self.parent(index)],self.heap[index]
            index=self.parent(index)           #here we pass parent index as index


    def display(self):
        return self.heap
    

    def delete_root(self):
        if len(self.heap)==0:
            print("heap is empty")
            return
        
        if len(self.heap)==1:
            self.heap.pop()
            return
        
        root=self.heap[0]
        self.heap[0]=self.heap.pop()
        self._heapify_down(0)
        return root
    

    def _heapify_down(self,index):
        largest=index
        left=self.left(index)
        right=self.right(index)

        if left<len(self.heap) and self.heap[left]>self.heap[largest]:
            largest=left

        if right<len(self.heap) and self.heap[right]>self.heap[largest]:
            largest=right

        if largest!=index:
            self.heap[index],self.heap[largest]=self.heap[largest],self.heap[index]
            self._heapify_down(largest)       #in heapify down we pass largest index




myheap=Maxheap()
myheap.insert(5)
myheap.insert(10)
myheap.insert(30)
myheap.insert(20)
myheap.insert(45)
myheap.delete_root()
print(myheap.display())