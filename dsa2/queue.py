#------------QUEUE-----------

#USING LIST

#but removing elements from front requires shifting all other elements, making it O(n).
# q=[]
# q.append(10)
# q.append(20)
# q.append(30)
# print(q)
# print(q.pop(0))
# print(q)



#USING DEQUE

# from collections import deque
# lst=[5,3,6,9]

# q=deque()
# q.append(20)
# q.append(55)
# q.appendleft(60)
# q.appendleft(12)
# # print(q.pop())
# print(q.popleft())
# # q.extend(lst)
# q.extendleft(lst)
# print(q)
# print(len(q))


#DEQUE IMPLEMENTATION USING CLASS

# from collections import deque

# class MyQueue:
#     def __init__(self):
#         self.myqueue=deque()

#     def add_element(self,item):     #this is enqueue ---- adding element. adding element at end. use o(1)
#         self.myqueue.append(item)

#     def pop_element(self):      #this is dequeue ----- removing element. use o(1). 
#         if not self.myqueue:        #if no values are there in the deque, deque([])
#             print("queue is underflow")         
#             return
        
#         return self.myqueue.popleft()      #first in first out
    
#     def display(self):       #use o(n)
#         return list(self.myqueue)           #the deque object is converted to list form
    

# q1=MyQueue()
# q1.add_element(99)
# q1.add_element(80)
# q1.add_element(52)
# q1.add_element(64)
# q1.pop_element()
# print(q1.display())



#QUEUE IMPLEMENTATION USING LINKEDLIST

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.ref=None


# class MyQueue:
#     def __init__(self):
#         self.first=None
#         self.last=None
#         self.count=0


#     def enqueue(self,data):
#         new_node=Node(data)

#         if self.first is None:      #ll is empty
#             self.first=self.last=new_node           #When the queue is empty, the first inserted node becomes both the front and the rear. Later when we add more element automatically last element will have last pointer. no need travel till last node to delete it/access it
#         else:
#             new_node.ref=None           #here traversal is not needed because the queue maintains a rear (last) pointer. This allows constant-time insertion at the end of the linked list.
#             self.last.ref=new_node
#             self.last=new_node

#         self.count+=1


#     def dequeue(self):
#         if self.first is None:
#             print("queue is underflow")
#             return
        
#         self.first=self.first.ref
#         self.count-=1
#         if self.first is None:       #This condition exists only for the case when the queue had one single element.
#             self.last=None           #if so, mark self.rear as none


    
#     def display(self):
#         if self.first is None:
#             print("queue is underflow")
#             return
        
#         current=self.first
#         while current is not None:
#             print(current.data,"--->",end=" ")
#             current=current.ref


#     def length(self):
#         print()
#         print("size of ll is ",self.count)


# q1=MyQueue()
# q1.enqueue(55)
# q1.enqueue(60)
# q1.enqueue(42)
# q1.enqueue(82)
# q1.dequeue()
# q1.dequeue()
# q1.display()
# q1.length()



#STACK IMPLEMENTATION USING QUEUE
# from collections import deque

# class StackUsingQueue:
#     def __init__(self):
#         self.q1=deque()   #q1 is the main queue
#         self.q2=deque()   #q2 is the helper queue
#         self.count=0


#     def push(self,x):
#         self.q2.append(x)    #whenever q2 is taking here it doesnt contain any elements

#         while self.q1:   #this loop will run until the q1 becomes empty
#             self.q2.append(self.q1.popleft())

#         self.q1,self.q2=self.q2,self.q1    #after this q1 becomes full of elements with last added element at the first and first added at the end. q2 becomes empty
#         self.count+=1


#     def pop(self):
#         if not self.q1:
#             print("stack is empty")
#             return
        
#         return self.q1.popleft()    #as a queue got here is from the above method result. so the latest element will be at the front. when deleting, physically it is FIFO but internally it is LIFO
    

#     def top(self):     #queue doesnt have top. it is a stack term. then why we use top here queue is behaving like a stack
#         if not self.q1:
#             print("stack is empty")
#             return
        
#         return self.q1[0]     #front of the queue
    

#     def display(self):
#         print("new stack is ", list(self.q1))
    

# sq=StackUsingQueue()
# sq.push(10)
# sq.push(20)
# sq.push(30)
# sq.push(40)
# sq.pop()
# sq.display()
    














