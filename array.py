#FIND THE LEADERS OF ARRAY
# def leader(lst):
#     if len(lst)==0:
#         return []
    
#     maximum=lst[-1]
#     result=[maximum]

#     for i in range(len(lst)-2,-1,-1):
#         if lst[i] >= maximum:
#             maximum=lst[i]
#             result.append(lst[i])
#     return result[::-1]    

# lst=list(map(int,input("Enter a list").split(" ")))
# print(leader(lst))


#sort a list contains 0 1 2 only
# def sorted(lst):
#     low=0
#     mid=0
#     high=len(lst)-1

#     while mid<=high:
#         if lst[mid]==0:
#             lst[low],lst[mid]=lst[mid],lst[low]   #it is moving all 0's to left
#             low=low+1   #then moving forward
#             mid=mid+1

#         elif lst[mid]==2:
#             lst[mid],lst[high]=lst[high],lst[mid]   #it is moving all 2's to right
#             high=high-1

#         else:
#             mid=mid+1

#     return lst

# lst=list(map(int,input("Enter a list").split(" ")))
# print(sorted(lst))


#COUNT MORE THAN N/K OCCURANCE OF THE ELEMENTS IN THE LIST. i didnt get the answers
# def count_freq(lst,k,count=0):
#     result_count=0
#     for i in range(len(lst)):
#         count=0
#         for j in range(i+1,len(lst)):
#             if lst[i]==lst[j]:
#                 count=count+1
#                 print("individual count: ",count)
#         if count>len(lst)//k:
#             result_count+=1
#             print("result count",result_count)

#     return result_count
    

# lst=list(map(int,input("Enter a list").split(" ")))
# k=int(input("enter the value of k : "))
# print(count_freq(lst,k))


#FIND THE LARGEST AND SMALLEST ELEMENT . one way of solving problem
# def big_small(lst):
#     maxi=lst[0]
#     mini=lst[0]
    
#     for i in range(len(lst)):
#         if lst[i]>maxi:
#             maxi=lst[i]

#     for j in range(len(lst)):
#         if lst[j]<mini:
#             mini=lst[j]

#     return maxi,mini

# lst=list(map(int,input("Enter a list").split(" ")))
# print(big_small(lst))


#another way of solving problem
# def big_small(lst):
#     maxi=lst[0]
#     mini=lst[0]
    
#     for num in lst:
#         if num>maxi:
#             maxi=num
#         else:
#             mini=num

#     return maxi,mini

# lst=list(map(int,input("Enter a list").split(" ")))
# print(big_small(lst))


#REVERSE AN ARRAY 
# def reverse(lst):
#     left=0
#     right=len(lst)-1

#     while left<right:
#         lst[left],lst[right]=lst[right],lst[left]
#         left=left+1
#         right=right-1

#     return lst

# lst=list(map(int,input("Enter a list").split(" ")))
# print(reverse(lst))


#MOVE ALL THE 0'S TO THE END
# def move_zero(lst):
#     low=0
    
#     for i in range(len(lst)):
#         if lst[i]!=0:
#             lst[low]=lst[i]
#             low=low+1

#     for i in range(low,len(lst)):
#         lst[i]=0

#     return lst

# lst=list(map(int,input("Enter a list").split(" ")))
# print(move_zero(lst))


#FIND MISSING NUMBER
# def missing_num(lst):
#     s=set(lst)

#     for i in range(min(lst),max(lst)+1):
#         if i not in s:
#             return i

# lst=list(map(int,input("Enter a list").split(" ")))
# print(missing_num(lst))


#HOW TO CONVERT A ARRAY TO LINKEDLIST
# A node class Stores data, Stores reference to next node, Does NOT know about the full list, Does NOT perform insert/delete/search
class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

# A LINKEDLIST CLASS Knows where the list starts (head) Controls: insertion, deletion, traversal, conversion from array, Manages entire structure
class Linkedlist:
    def __init__(self):
        self.head=None

    def arraytoll(self,arr):
        self.head=Node(arr[0])  #should make the first element as node element

        n=self.head
        for i in range(1,len(arr)):
            new_node=Node(arr[i])
            n.ref=new_node   #this line connects the previous node to the newnode
            n=new_node     #moves forward

        return n
    
    def printll(self):
        if self.head is None:
            print("ll is empty")
        
        else:
            n=self.head
            while n is not None:
                print(n.data,"---->",end=" ")
                n=n.ref

arr=[3,4,5,2,3]
ll=Linkedlist()
ll.arraytoll(arr)
ll.printll()
