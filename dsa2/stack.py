#Python does not have a built-in stack type, but stacks can be implemented in different ways using different data structures
#--------------STACK---------------

#USING LIST 

# stack=[]

# stack.append(10)
# stack.append(20)
# stack.append(30)
# print(stack)
# stack.pop()
# print(stack)
# print(len(stack))


# #USING DEQUE

# from collections import deque

# stack=deque()
# stack.append(20)
# stack.append(40)
# stack.append(50)
# stack.pop()
# # print(not stack)
# print(stack)



#STACK IMPLEMENTATION USING LINKEDLIST

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.ref=None


# class Stack:
#     def __init__(self):
#         self.top=None
#         self.count=0


#     def display(self):
#         if self.top is None:
#             print("stack is empty")
#         else:
#             current=self.top

#             while current is not None:
#                 print(current.data,"--->",end=" ")
#                 current=current.ref


#     def push(self,data):        #push element at the begining of the list. cannot add elements from the middle/end. so if then it is not stack
#         new_node=Node(data)

#         if self.top is None:
#             self.top=new_node
#         else:
#             new_node.ref=self.top
#             self.top=new_node

#         self.count+=1


#     def pop(self):              #pop element at the begining of the list. last in first out manner.
#         if self.top is None:
#             print("Stack is underflow")
#             return
        
#         temp=self.top
#         self.top=self.top.ref
#         self.count-=1
#         return temp.data
    

#     def peek(self):
#         if self.top is None:
#             print("Stack is underflow")
#             return
        
#         return self.top.data
    
#     def size(self):
#         return self.count

    

# s1=Stack()
# s1.push(20)
# s1.push(50)
# s1.push(80)
# s1.push(70)
# s1.push(30)
# print("first popped : ",s1.pop())
# # print("scnd popped : ",s1.pop())
# print("peek element is ",s1.peek())
# print("length of list is ",s1.size())

# s1.display()



#IMPLEMENT QUEUE USING STACK
class QueueUsingStack:
    def __init__(self):
        self.s1=[]
        self.s2=[]


    def insert(self,x):
        self.s1.append(x)

    
    def delete(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())        #every element are now at self.s2

        return self.s2.pop()     #pop from s2 
    

    def display(self):
        if self.s1:
            return self.s1
        else:
            return self.s2[::-1]
    

qs=QueueUsingStack()
qs.insert(52)
qs.insert(26)
qs.insert(13)
qs.delete()
print(qs.display())


#REVERSE A STRING
# def reverse(s):
#     lst=list(s)
#     res=[]
    
#     for i in range(len(lst)):
#         res.append(lst.pop())    #it means remove from current lst, append it to new lst
        
#     return "".join(res)


# s="rainbow"
# print(reverse(s))



#REMOVE MIDDLE FROM STACK. not correct
# def del_middle(lst):
#     stack=[]

#     mid=len(lst)//2

#     for i in lst:
#         if i!=lst[mid]:
#             stack.append(i)
    
#     stack.append(lst[mid])
#     stack.pop()

#     return stack

# lst=[2,4,2,3,5,3,4]
# print(del_middle(lst))




#CHECK PARENTHESIS ARE VALID
# def valid_para(s):
#     stack=[]

#     pairs={')': '(', '}': '{', ']': '['}

#     for i in s:
#         if i in "({[":
#             stack.append(i)

#         elif i in ")}]":
#             if not stack:       #if stack is empty. (if stack is none is invalid. it doesnt check stack is empty)
#                 return False
            
#             if stack[-1]==pairs[i]:
#                 stack.pop()
#             else:
#                 return False
            
#     return True

# s="()[]{}"
# print(valid_para(s))



#REVERSE A STACK
# def reverse(lst):
#     new_reverse=[]

#     stack=[]

#     for i in lst:
#         stack.append(i)

#     for i in range(len(stack)):
#         new_reverse.append(stack.pop())

#     return new_reverse


# lst=[3,5,3,6,7,8,4]
# print(reverse(lst))



#CHECK A STRING IS PALINDROME USING STACK
# def palindrome(lst):
#     n=lst[:]
#     new=""
#     stack=[]

#     for i in lst:
#         stack.append(i)

#     for i in range(len(stack)):
#         new=new+stack.pop()

#     if n==new:
#         return True
#     else:
#         return False
    
# lst="jhgugjh"
# print(palindrome(lst))




