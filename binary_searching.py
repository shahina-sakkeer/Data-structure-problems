# LINEAR SEARCH IF DUPLICATE ELEMENTS ARE PRESENT
# def search(lst,value):
#     flag=False
#     new=[]
#     for i in range(len(lst)):
#         if lst[i]==value:
#             new.append(i)
    
#     if new:
#         print("key element found at")
#         for i in new:
#             print(i)
#     else:
#         print("element is not found")


# newlst=list(map(int,input("enter the list").split(" ")))
# key=int(input("Enter a number to find"))
# search(newlst,key)



#BINARY SEARCH 1st WAY WITHOUT DISPLAYING INDEX
# def binary_search(lst,value):
#     low=0
#     high=len(lst)-1
#     found=False

#     while low<=high and not found:
#         mid=(low+high) //2

#         if lst[mid]==value:  #we will always find the target at middle
#             found=True
            
#         elif value>lst[mid]:
#             low=mid+1

#         else:
#             high=mid-1

#     if found==True:
#         print("key found")
#     else:
#         print("key not found")

# new=list(map(int,input("enter a list").split(" ")))
# key=int(input("enter a key"))
# new.sort()
# index=binary_search(new,key)


#ANOTHER WAY TO FIND THE ELEMENT BY DISPLAYING INDEX.MOST PREFERABLE TO DISPLAY INDEX
# def binary_search(lst,value):
#     low=0
#     high=len(lst)-1

#     while low<=high:
#         mid=(low+high) // 2

#         if lst[mid]==value:
#             return mid
            
#         elif value>lst[mid]:
#             low=mid+1

#         else:
#             high=mid-1

#     return

# n=int(input("enter the length of the list"))
# print("enter the elements in asc order")
# new=[int(input()) for i in range(n)]
# key=int(input("enter the value : "))
# new.sort()
# print("sorted array is ",arr)
# index=binary_search(new,key)

# if index is not None:
#     print("Key found at sorted list at index ",index)
# else:
#     print("key doesnot found")



#TAKING FIRST OCCURANCE OF TARGET IF DUPLICATES PRESENT
# def duplicate_binary_target(lst,value):
#     low=0
#     high=len(lst)-1
#     result=None

#     while low <= high:
#         mid=(low+high) // 2
#         if value==lst[mid]:
#             result=mid
#             high=mid-1  #it will check does the target is again there before the middle position
#             #[10,10,10,20,40]. suppose this is the list. target=10. we found target at middle right. but again we are checking wheather target is occuring below the middle index. that will be the first indexes


#         elif value > lst[mid]:
#             low=mid+1

#         else:
#             high=mid-1

#     return result

# new=[10,20,20,40,50]
# target=int(input("enter the target"))
# res=duplicate_binary_target(new,target)

# if res is not None:
#     print("the target found at index ",res)
# else:
#     print("target not found")



# def duplicate_last_target(lst,value):
#     low=0
#     high=len(lst)-1
#     result=-1

#     while low<=high:  #loop exits only when search space is exhausted.Even after finding the target, binary search keeps going until low > high
#         mid=(low+high) //2

#         if value==lst[mid]:
#             result=mid
#             low=mid+1  #it will check does the target is again there after the middle position. this low is going and check inside while loop
        
#         elif value>lst[mid]:
#             low=mid+1
#         else:
#             high=mid-1

#     return result


# new=[20,30,40,50,60,60,70]
# print("The sorted array is: ")
# new.sort()
# print(new)
# target=int(input("enter the target: "))
# index=duplicate_last_target(new,target)

# if index is not None:
#     print("the target lies in ", index)
# else:
#     print("target not found")



#MINIMUM ELEMENT FROM ROTATIONAL SORTED LIST
# def minimum(lst):
#     low=0
#     high=len(lst)-1

#     while low<high:
#         mid=(low+high)//2

#         if lst[mid]>lst[high]:
#             low=mid+1

#         else:
#             high=mid

#     return lst[low]


# arr=[4,5,1,2,3]
# print(minimum(arr))



#RECURSION USING BINARY SEARCH
# def recursive_search(lst,low,high,key):
#     low=0
#     high=len(lst)-1

#     if low>high:
#         return -1
    
#     mid=(low+high) //2
    
#     if key==lst[mid]:
#         return mid
      
#     if key>lst[mid]:
#         return recursive_search(lst,mid+1,high,key)
    
#     if key<lst[mid]:
#         return recursive_search(lst,low,mid-1,key)
    
# lst=list(map(int,input("enter a list : ").split(" ")))
# target=int(input("enter the target "))
# lst.sort()
# print("sorted list is : ",lst)
# print(recursive_search(lst,0,len(lst)-1,target))



#RECURSION USING BINARY SEARCH(another method)
# def recursion_search(lst,key,low,high):

#     while low<=high:
#         mid=(low+high)//2

#         if key==lst[mid]:
#             return mid
        
#         elif key>lst[mid]:
#             return recursion_search(lst,key,mid+1,high)
        
#         else:
#             return recursion_search(lst,key,low,mid-1)
        
#     return
        
# lst=[10,10,20,30,40,50]
# key=int(input("enter the target : "))
# idx=recursion_search(lst,key,0,len(lst)-1)
# if idx is not None:
#     print("element found at ", idx)
# else:
#     print("target not found ")



#REPLACE TARGET ELEMENT BY A VALUE(one method)
# def binary(lst,target,value):
#     low=0
#     high=len(lst)-1
#     res=None
    
#     while low<=high:
#         mid=(low+high)//2

#         if target==lst[mid]:
#             res=mid
#             break
        
#         elif target>lst[mid]:
#             low=mid+1
        
#         else:
#             high=mid-1
            
#     if res is not None:
#         lst.pop(mid)
#         lst.insert(mid,value)
#         return lst
#     else:
#         return lst

# lst=[12,13,14,15,17,20]
# target=int(input("enter the target : "))
# value=int(input("enter the values : "))
# print(binary(lst,target,value))



#REPLACE TARGET ELEMENT BY A VALUE(another method)
# def binary(lst, target, value):
#     low = 0
#     high = len(lst) - 1

#     while low <= high:
#         mid = (low + high) // 2

#         if target == lst[mid]:
#             lst[mid] = value   # direct replace
#             return lst

#         elif target > lst[mid]:
#             low = mid + 1
#         else:
#             high = mid - 1

#     return lst


