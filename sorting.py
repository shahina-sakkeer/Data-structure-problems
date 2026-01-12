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
#         for j in range(len(lst)-1-i):
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
#     return i+1


# def quick_sort(lst,low,high):       #this function does NOT know how to arrange elements — It only knows when and where to sort.
#     if low<high:
#         p=partition(lst,low,high)    #p is the Boundary between sorted & unsorted
#         quick_sort(lst,low,p-1)      #Sort left side (elements smaller than pivot)
#         quick_sort(lst,p+1,high)     #Sort right side (elements bigger than pivot)


# arr=[10, 7, 8, 9, 1, 5]
# print(quick_sort(arr,0,len(arr)-1))



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

#         while i<len(left_list) and j<len(right_list):     #we need to compare all values from left_list and all values from right_list too.that swhy while loop
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

#         while pos>0 and current_element<lst[pos-1]:   #check current element is less than sorted part(ie previou value). why loop because there will be many values in sorted part to check with the current element.
#             lst[pos]=lst[pos-1]    #move bigger value to right side. not like move smaller value to left side. it means the value in pos[i-1] is moved to pos[i]
#             pos=pos-1     #it means if multiple elements are in sorted part, we need to compare moved value with the sorted part

#         lst[pos]=current_element

#     return lst

# lst=[4,6,2,5,4,1]
# print(insertion_sort(lst))




