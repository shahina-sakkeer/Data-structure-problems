# -------------SELECTION SORT----------------


#SELECTION SORT IN ASC ORDER   
# lst=[3,2,1,4,5]

# for i in range(len(lst)):
#     min_index=i
#     for j in range(i+1,len(lst)):
#         if lst[j] < lst[min_index]:
#             min_index=j

#     lst[i],lst[min_index]=lst[min_index],lst[i]
# print(lst)


#SELECTION SORT IN DESC ORDER 
# def selection(lst):
#     for i in range(len(lst)):
#         max_index=i

#         for j in range(i+1,len(lst)):
#             if lst[j] > lst[max_index]:
#                 max_index=j

#         lst[i],lst[max_index]=lst[max_index],lst[i]

#     return lst

# lst=list(map(int,input("enter the list in space gap :  ").split()))
# print(selection(lst))


#Kth SMALLEST ELEMENT USING SELECTION SORT
# def kth_small(lst,k):
#     for i in range(len(lst)):
#         min_idx=i
#         for j in range(i+1,len(lst)):
#             if lst[j]<lst[min_idx]:
#                 min_idx=j

#         lst[i],lst[min_idx]=lst[min_idx],lst[i]

#     return(lst[k-1])     #if we ask for 3rd smalles and we give lst[k], it will give 3rd index value. but 3rd smallest element is located at 2nd index.

# lst=list(map(int,input("enter the list in space gap :  ").split()))
# k=int(input("enter the target : "))
# print(kth_small(lst,k))



# --------BUBBLE SORT--------

#SORT LIST IN ASC ORDER
# def bubble_asc(lst):
#     for i in range(len(lst)):
#         for j in range(len(lst)-1):
#             if lst[j]>lst[j+1]:
#                 lst[j],lst[j+1]=lst[j+1],lst[j]

#     return lst

# lst=[15,20,10,35,5,20,10]
# print(bubble_asc(lst))



# ---------QUICK SORT------------
# def partition(lst,low,high):              #This function does NOT sort the whole array. it chose pivot, moves smaller element to left, larger to right and pivot to correct position.
#     pivot=lst[high]
#     i=low-1

#     for j in range(low,high):
#         if lst[j] < pivot:
#             i+=1
#             lst[i],lst[j]=lst[j],lst[i]
           

#     lst[i+1],lst[high]=lst[high],lst[i+1]
#     return i+1       #i+1 carries the position of pivot value(from the above swapping). that is returning when partition function calls in the below


# def quick_sort(lst,low,high):       #this function does NOT know how to arrange elements — It only knows when and where to sort.
#     if low<high:
#         p=partition(lst,low,high)    #p is the Boundary between sorted & unsorted. the returning i from partition() will be in this p. that i is the current position of pivot
#         quick_sort(lst,low,p-1)      #Sort left side (elements smaller than pivot). that i is used here for p-1. that is leftlist carries till pivot
#         quick_sort(lst,p+1,high)     #Sort right side (elements bigger than pivot). rightlist carries 


# arr=[10, 7, 8, 9, 1, 5]
#quick_sort(arr,0,len(arr)-1))
# print(lst)



# ---------MERGE SORT---------

#SORT LIST IN ASC ORDER
# def merge_sort(lst):
#     if len(lst)>1:
#         mid=len(lst)//2

#         left_list=lst[:mid]
#         right_list=lst[mid:]

#         merge_sort(left_list)    #why this recusrive fn because we need to reach till the list reaches to len as one
#         merge_sort(right_list)   #after full recusrion is over, we will get many list that contains only single element

#         i=0 
#         j=0
#         k=0

#         while i<len(left_list) and j<len(right_list):     #we need to compare all values from left_list and all values from right_list too.thats why while loop
#             if left_list[i]<right_list[j]:   
#                 lst[k]=left_list[i]    #if the above if condition is true, add element from left_list to the original list(lst) in kth position. This sorting is in-place sorting 
#                 i+=1
#                 k+=1 
#             else:
#                 lst[k]=right_list[j]
#                 j+=1
#                 k+=1

#         while i<len(left_list):        #this condition is written because after above statement are over, there will be one value in either left_list or right_list that has left out. inorder to add that, write this condition
#             lst[k]=left_list[i]
#             i=i+1
#             k+=1

#         while j<len(right_list):      #why while loop because we need to go through all elements which is left out and add that to current k index.
#             lst[k]=right_list[j]
#             j+=1
#             k+=1

#     return lst


# lst=list(map(int,input("enter the list : ").split()))
# print(merge_sort(lst))



#SORT LIST IN DESC ORDER
# def merge_sort(lst):
#     if len(lst)>1:
#         mid=len(lst)//2

#         left_list=lst[:mid]
#         right_list=lst[mid:]

#         merge_sort(left_list)
#         merge_sort(right_list)

#         i=j=k=0

#         while i<len(left_list) and j<len(right_list):
#             if left_list[i]>right_list[j]:
#                 lst[k]=left_list[i]
#                 i+=1
#                 k+=1
#             else:
#                 lst[k]=right_list[j]
#                 j+=1
#                 k+=1
        
#         while i<len(left_list):
#             lst[k]=left_list[i]
#             i+=1
#             k+=1

#         while j<len(right_list):
#             lst[k]=right_list[j]
#             j+=1
#             k+=1

#     return lst

# lst=list(map(int,input("enter the list : ").split()))
# print(merge_sort(lst))



#---------INSERTION SORT----------

#SORT LIST IN ASC ORDER
# def insertion_sort(lst):
#     for i in range(1,len(lst)):
#         current_element=lst[i]
#         pos=i

#         while pos>0 and current_element<lst[pos-1]:       #check current element is less than sorted part(ie previou value). why loop because there will be many values in sorted part to check with the current element.
#             lst[pos]=lst[pos-1]        #move bigger value to right side. not like move smaller value to left side. it means the value in pos[i-1] is moved to pos[i]
#             pos=pos-1         #it means if multiple elements are in sorted part, we need to compare moved value with the sorted part

#         lst[pos]=current_element

#     return lst

# lst=[4,6,2,5,4,1]
# print(insertion_sort(lst))



#FIND MAXIMUM AND MINIMUM VALUE AFTER SORTING. using quick_sort

# def partition(lst,low,high):
#     pivot=lst[high]
#     i=low-1

#     for j in range(low,high):
#         if lst[j]>pivot:
#             i=i+1
#             lst[i],lst[j]=lst[j],lst[i]

#     lst[i+1],lst[high]=lst[high],lst[i+1]
#     return i+1



# def quick_sort(lst,low,high):
#     if low<high:
#         p=partition(lst,low,high)
#         quick_sort(lst,low,p-1)
#         quick_sort(lst,p+1,high)



# lst=[20,40,69,78,41,33]
# quick_sort(lst,0,len(lst)-1)
# print("maximum us",lst[0])
# print("minimum us",lst[-1])



# KTH LARGEST USING QUICK SORT. one method
# def partition(lst,low,high):
#     pivot=lst[high]
#     i=low-1

#     for j in range(low,high):
#         if lst[j]>pivot:
#             i+=1
#             lst[i],lst[j]=lst[j],lst[i]

#     lst[i+1],lst[high]=lst[high],lst[i+1]
#     return i+1


# def kth_large(lst,low,high):
#     if low<high:
#         p=partition(lst,low,high)
#         kth_large(lst,low,p-1)
#         kth_large(lst,p+1,high)

#     return lst[k-1]

# lst=[20,85,14,63,25,99,74,55]
# k=int(input("enter which element : "))
# kth_large(lst,0,len(lst)-1)
# print("kth : ",lst[k-1])



# KTH LARGEST USING QUICK SORT. another method
# def partition(lst,low,high):
#     pivot=lst[high]
#     i=low-1

#     for j in range(low,high):
#         if lst[j]>pivot:    #descending. 
#             i+=1
#             lst[i],lst[j]=lst[j],lst[i]

#     lst[i+1],lst[high]=lst[high],lst[i+1]
#     return i+1


# def kth_large(lst,low,high,k):
#     if low<high:
#         p=partition(lst,low,high)   #so all items left of p are larger and right are smaller becuase of descending order
#         if p==lst[k-1]:
#             return lst[p]
#         elif p>k-1:
#             kth_large(lst,low,p-1,k)   #this line is for left list of pivot. Pivot is too far right.So the Kth largest element must be in the left side.
#         else:
#             kth_large(lst,p+1,high,k)    #this line is for right side of pivot. Pivot is too far left.

#     return lst[k-1]

# lst=[20,85,14,63,25,99,74,55]
# k=int(input("enter which element : "))
# result=kth_large(lst,0,len(lst)-1,k)
# print("kth : ",result)



#SORT STRING USING MERGE SORT        
# def merge_string(s):
#     if len(s)<=1:
#         return s          #Return is mandatory for strings. because we cannot do it like list as string is immutable. if we dont return s, Original string s never changes
    
#     mid=len(s) // 2

#     left=merge_string(s[:mid])   #These already create new strings. we cannot write recursive calls like list because strings are immutable
#     right=merge_string(s[mid:])

#     i=j=0
#     res=[]
#     while i<len(left) and j<len(right):
#         if left[i]<right[j]:
#             res.append(left[i])
#             i+=1
#         else:
#             res.append(right[j])
#             j+=1

#     while i<len(left):
#         res.append(left[i])
#         i+=1

#     while j<len(right):
#         res.append(right[j])
#         j+=1

#     return "".join(res)


# s="mergesortexample"
# print(merge_string(s))



#MERGE 2 SORTED ARRAYS IN DESCENDING ORDER. for descending merge, the lists also should be in desc, l1=[10, 8, 6, 4, 2] l2=[9, 7, 5, 3, 1]
# def merge_array(lst1,lst2):
#     i=j=0
#     res=[]

#     while i<len(lst1) and j<len(lst2):
#         if lst1[i]<lst2[j]:
#             res.append(lst1[i])
#             i+=1
#         else:
#             res.append(lst2[j])
#             j+=1

#     while i<len(lst1):
#         res.append(lst1[i])
#         i+=1
#     while j<len(lst2):
#         res.append(lst2[j])
#         j+=1

#     return res

# l1=[1,3,5,7,9]
# l2=[2,4,6,8,10]
# print(merge_array(l1,l2))



#SORT ARRAY OF OBJECTS BASED ON MARKS (bubble)
# def sort_lst(students):
#     for i in range(len(students)):
#         for j in range(len(students)-1):
#             if students[j]["marks"] > students[j+1]["marks"]:
#                 students[j],students[j+1]=students[j+1],students[j]
    
#     return students


# students = [
#     {"name": "Asha", "marks": 78},
#     {"name": "Rahul", "marks": 92},
#     {"name": "Neha", "marks": 85},
#     {"name": "Vijay", "marks": 67},
#     {"name": "Kiran", "marks": 92}
# ]
# print(sort_lst(students))



#SORT ARRAY OF OBJECTS BASED ON MARKS (quick)
# def partition(students,low,high):
#     pivot=students[high]["marks"]

#     i=low-1

#     for j in range(low,high):
#         if students[j]["marks"] < pivot:
#             i+=1
#             students[j],students[i]=students[i],students[j]

#     students[high],students[i+1]=students[i+1],students[high]
#     return i+1


# def quick(students,low,high):
#     if low<high:
#         p=partition(students,low,high)
#         quick(students,low,p-1)
#         quick(students,p+1,high)


# students = [
#     {"name": "Asha", "marks": 78},
#     {"name": "Rahul", "marks": 92},
#     {"name": "Neha", "marks": 85},
#     {"name": "Vijay", "marks": 67},
#     {"name": "Kiran", "marks": 92}
# ]
# quick(students,0,len(students)-1)
# print(students)



#SORT A LINKEDLIST
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.ref=None


# class Linkedlist:
#     def __init__(self):
#         self.head=None

#     def display(self):
#         n=self.head

#         if n is None:
#             print("empty")
        
#         while n is not None:
#             print(n.data,"--->",end="")
#             n=n.ref

#     def insert(self,data):
#         new_node=Node(data)
#         if self.head is None:
#             self.head=new_node
#         else:
#             new_node.ref=self.head
#             self.head=new_node


#     def bubble(self):
#         if self.head is None:
#             print("ll is empty")
#             return
        
#         swapped=True

#         while swapped:
#             swapped=False   #no swap happened
#             n=self.head
#             while n.ref is not None:   #if we are using this while condition only, It performs only ONE pass through the list.Only the largest element may move to the end.rest of the element remains unchanged.
#                 if n.data>n.ref.data:
#                     n.data,n.ref.data=n.ref.data,n.data
#                     swapped=True        #one swapped
#                 n=n.ref



# ll=Linkedlist()
# ll.insert(10)
# ll.insert(20)
# ll.insert(15)
# ll.insert(12)
# ll.bubble()
# ll.display()
            



#REMOVE DUPLICATES WHILE SORTING
# def remove_dupli(lst):
#     for i in range(len(lst)):
#         for j in range(len(lst)-1):
#             if lst[j]>lst[j+1]:
#                 lst[j],lst[j+1]=lst[j+1],lst[j]

#     write=1

#     for read in range(1,len(lst)):
#         if lst[read]!=lst[read-1]:
#             lst[write]=lst[read]
#             write+=1

#     return lst[:write]


# lst=[5,9,6,8,6,5,4,4,3,5]
# print(remove_dupli(lst))