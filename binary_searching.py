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

#     return -1

# n=int(input("enter the length of the list"))
# print("enter the elements in asc order")
# new=[int(input()) for i in range(n)]
# key=int(input("enter the value : "))
# new.sort()
# print("sorted array is ",arr)
# index=binary_search(new,key)

# if index != -1:
#     print("Key found at sorted list at index ",index)
# else:
#     print("key doesnot found")




#TAKING FIRST OCCURANCE OF TARGET IF DUPLICATES PRESENT
# def duplicate_binary_target(lst,value):
#     low=0
#     high=len(lst)-1
#     result=-1

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






