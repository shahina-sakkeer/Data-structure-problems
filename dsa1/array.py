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
#         else:
#             pass
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
#     maxi=float("-inf")
#     mini=float("inf")
    
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
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.ref=None

# A LINKEDLIST CLASS Knows where the list starts (head) Controls: insertion, deletion, traversal, conversion from array, Manages entire structure
# class Linkedlist:
#     def __init__(self):
#         self.head=None

#     def arraytoll(self,arr):
#         self.head=Node(arr[0])  #should make the first element as node element

#         n=self.head
#         for i in range(1,len(arr)):
#             new_node=Node(arr[i])
#             n.ref=new_node   #this line connects the previous node to the newnode
#             n=new_node     #moves forward

#         return n
    
#     def printll(self):
#         if self.head is None:
#             print("ll is empty")
        
#         else:
#             n=self.head
#             while n is not None:
#                 print(n.data,"---->",end=" ")
#                 n=n.ref

# arr=[3,4,5,2,3]
# ll=Linkedlist()
# ll.arraytoll(arr)
# ll.printll()


#COMMON ELEMENT IN THE ARRAY
# def common(lst1,lst2):
#     s=set(lst2)
#     for i in range(len(lst1)):
#         if lst1[i] in s:
#             return lst1[i]


# lst1=[3,4,5,4,4,2]
# lst2=[4,6,7,4]
# print(common(lst1,lst2))


#FIND THE DUPLICATES IN AN ARRAY
# def duplicates(lst):
#     s=set()

#     for i in lst:
#         if i in s:
#             return i
#         s.add(i)
        
# lst=[3,4,5,4,4,2]
# print(duplicates(lst))


# def max_min(lst):
#     maxi=lst[0]
#     mini=lst[0]

#     for num in lst:
#         if num>maxi:
#             maxi=num
#         elif num<mini:
#             mini=num
    
#     lst.remove(maxi)
#     lst.remove(mini)

#     maxi=lst[0]
#     mini=lst[0]

#     for i in lst:
#         if i>maxi:
#             maxi=i
#         elif i<mini:
#             mini=i

#     return mini,maxi

# lst=[3,4,5,4,4,2]
# print(max_min(lst))


#COUNT OF EVEN AND ODD NUMBERS
# def even_odd(lst):
#     counte=0
#     counto=0

#     for i in lst:
#         if i%2==0:
#             counte+=1
#         else:
#             counto+=1

#     return counte,counto

# lst=[8,2,3,8,9,6,6,5]
# odd,even=even_odd(lst)
# print("odd count is ",odd)
# print("even count is ",even)


#FIND THE LENGTH OF ARRAY
# def length(lst):
#     count=0
#     for i in lst:
#         count+=1

#     return count

# lst=[5,1,2,3,9,6,5,6]
# print(length(lst))


#FINDING THE COUNT OF OCCURANCE
# def count_num(lst,key):
#     count=0
#     for i in lst:
#         if key==i:
#             count+=1

#     return count


# lst=[5,1,2,3,9,6,5,6]
# key=int(input("enter a target"))
# print(count_num(lst,key))



#LAST OCCURANCE OF A ELEMENT
# def last_occ(lst,key): 
#     for i in range(len(lst)-1,-1,-1): 
#         if lst[i]==key: 
#             return i 
#     return -1 

# lst=[5,1,2,3,9,6,5,6] 
# key=int(input("enter a target")) 
# idx=last_occ(lst,key) 
# if idx!=-1: 
#     print("key found at",idx) 
# else: 
#     print("key not found")



#MOVE ZEROS TO THE END
# def move(lst):
#     write=0
#     og=lst[:]

#     for read in og:
#         if read != 0:
#             lst[write]=read
#             write+=1

#     for read in og:
#         if read == 0:
#             lst[write]=read
#             write+=1

#     return lst
    

# lst=[1,0,2,0,3]
# print(move(lst))



#MOVE ZEROS TO THE START
# def move(lst):
#     write=0
#     og=lst

#     for x in og:
#         if x==0:
#             lst[write]=x
#             write+=1

#     for y in og:
#         if y!=0:
#             lst[write]=y
#             write+=1

#     return lst

# lst=[1,0,2,0,3]
# print(move(lst))


#SWAP FIRST AND LAST ELEMENT
# def swap_first_and_last(lst):
#     left=0
#     right=len(lst)-1

#     while left<right:
#         lst[left],lst[right]=lst[right],lst[left]
#         return lst


# lst=[5,1,2,3,9,6,5,6] 
# print(swap_first_and_last(lst))



#CHECK PALINDROME OR NOT
# def palindrome(lst):
#     left=0
#     right=len(lst)-1

#     while left<right:
#         if lst[left]!=lst[right]:
#             return False
        
#         else:
#             left+=1
#             right-=1



# lst=[2,1,1,1,2]
# result=palindrome(lst)
# if result==False:
#     print("not palindrome")
# else:
#     print("palindrome")



#REMOVE DUPLICATE
# def remove_dup(lst):
#     res=[]
#     for i in range(len(lst)):
#         if lst[i] not in res:
#             res.append(lst[i])

#     return res

# lst=[1,2,2,3,3,3,4]
# print(remove_dup(lst))



#REMOVE ALL OCCURANCE OF GIVEN ELEMENT
# def remove_all(lst,key):
#     write=0

#     for read in range(len(lst)):
#         if lst[read]!=key:
#             lst[write]=lst[read]
#             write+=1

#     return lst[:write]


# lst=[2,1,5,6,2,2,5]
# key=int(input("enter a key : "))
# print(remove_all(lst,key))



#MOVE ALL EVEN NUMBERS TO TH END
# def move_even_end(lst):
#     write = 0
#     original = lst[:]

#     for x in original:
#         if x % 2 != 0:
#             lst[write] = x
#             write += 1

#     for x in original:
#         if x % 2 == 0:
#             lst[write] = x
#             write += 1

#     return lst

# lst=[2,1,5,6,2,2,3]
# print(move_even_end(lst))



#MOVE ALL ODD NUMBERS TO TH START
# def move_odd_start(lst):
#     write=0
#     og=lst[:]

#     for x in og:
#         if x % 2 != 0:
#             lst[write]=x
#             write+=1

#     for x in og:
#         if x % 2 == 0:
#             lst[write]=x
#             write+=1

#     return lst


# lst=[8,6,3,5,5,7,4]
# print(move_odd_start(lst))



#REMOVE DUPLICATE(sorted)
# def remove_dup(lst):
#     write=1

#     for read in range(1,len(lst)):
#         if lst[read] != lst[read-1]:
#             lst[write]=lst[read]
#             write+=1

#     return lst[:write]
    

# lst=[1,2,2,2,3,3,4,4,5,5]
# print(remove_dup(lst))


#REMOVE DUPLICATE(unsorted)
# def remove_dup(lst):
#     seen=set()  #set never creates duplicate values
#     write=0

#     for read in range(len(lst)):
#         if lst[read] not in seen:  
#             seen.add(lst[read])  #if the read is not in set,add it to set.
#             lst[write]=lst[read]   #add that element to list also. it avoids duplicate printing
#             write+=1

#     return lst[:write]   #remove all the end garbage values

# lst=[3,1,2,1,3,6,2]
# print(remove_dup(lst))



#TWO SUM EQUALS TARGET. USING NESTED LOOP
# def two_sum(nums,target):
#     for x in range(len(nums)):
#         for y in range(x+1,len(nums)):
#             if nums[x]+nums[y]==target:
#                 return x,y


# nums = [2,7,11,15]
# target=9
# print(two_sum(nums,target))



#TWO SUM USING ONLY WHILE LOOP.(sorted array)
# def two_sum_sorted(nums,target):
#     left=0
#     right=len(nums)-1

#     while left<right:
#         if nums[left]+nums[right]==target:
#             return left,right
        
#         elif nums[left]+nums[right]>target:
#             right-=1

#         else:
#             left+=1

#     return None

# lst=[2, 3, 7, 11, 15]
# target=int(input("enter a target :  "))
# idx=two_sum_sorted(lst,target)
# if idx is not None:
#     print("elements found at ",idx)
# else:
#     print("elements not found")



#SECOND LARGEST ELEMENT IN AN ARRAY(using 2 passes). There might arise a condition if the array contains same elements only. also check condition for len(lst) > 1
# def sec_large(lst):
#     maxi=float("-inf")
#     sec_max=float("-inf")

#     for x in lst:
#         if x>maxi:
#             maxi=x

#     for x in lst:
#         if x>sec_max and x!=maxi:
#             sec_max=x

#     return sec_max

# lst=[8,9,5,5,6,6,8]
# print(sec_large(lst))



#SECOND LARGEST ELEMENT IN AN ARRAY(using 1 pass)
# def sec_large(lst):
#     if len(lst)<2:   #check condition for len(lst) > 1. if less than 2, return none
#         return None
    
#     maxi=float("-inf")
#     sec_max=float("-inf")

#     for x in lst:
#         if x>maxi:
#             sec_max=maxi
#             maxi=x
#         elif x>sec_max and x!=maxi:
#             sec_max=x

#     return sec_max

# lst=[8,9,5,5,6,6,8]
# print(sec_large(lst))




#THRID LARGEST ELEMENT
# def move(lst):
#     large=float("-inf")
#     second_large=float("-inf")
#     third_large=float("-inf")
    
#     for i in lst:
#         if i>large:
#             second_large=large
#             large=i
            
#         elif i>second_large and i!= large:
#             third_large=second_large
#             second_large=i
            
#         elif i>third_large and i!=large and i!=second_large:
#             third_large=i
            
#     return third_large
    
# lst=[2,15,7,3,11]
# print(move(lst))



#THIRD SMALLEST ELEMENT
# def move(lst):
#     small=float("inf")
#     sec_small=float("inf")
#     third_small=float("inf")
    
#     for i in lst:
#         if i<small:
#             sec_small=small
#             small=i
            
#         elif i<sec_small and i!=small:
#             third_small=sec_small
#             sec_small=i
            
#         elif i<third_small and i!=small and i!=sec_small:
#             third_small=i
            
#     return third_small
    
# lst=[2,15,7,3,11,14,5]
# print(move(lst))




#SECOND MINIMUM ELEMENT
# def sec_min(lst):
#     mini=float("inf")
#     sec_mini=float("inf")

#     for x in range(1,len(lst)):
#         if lst[x]<mini:
#             sec_mini=mini
#             mini=lst[x]

#         elif lst[x]<sec_mini and lst[x]!=mini:
#             sec_mini=lst[x]

#     return sec_mini

# lst=[8,9,5,5,6,6,8]
# print(sec_min(lst))



#FIND THE FREQUESNCY OF ALL NUMBERS IN AN ARRAY
# def count_freq(lst):
#     dic={}

#     for x in lst:
#         if x not in dic:
#             dic[x]=1
#         else:
#             dic[x]=dic[x]+1
#     return dic

# lst=[8,9,5,5,6,6,8]
# print(count_freq(lst))



#DELETE A SPECIFIC ELEMENT FROM AN ARRAY
# def remove(lst,target):
#     write=0

#     for fast in range(len(lst)):
#         if lst[fast]!=target:
#             lst[write]=lst[fast]
#             write+=1

#     return lst[:write]

# lst=[8,9,5,5,6,6,8]
# target=int(input("enter a number : "))
# print(remove(lst,target))


#FIND SEC LARGE AND SEC SMALL ELEMENT(using 2 loops)
# def sec_large_small(lst):
#     big=float("-inf")
#     sbig=float("-inf")
#     small=float("inf")
#     ssmall=float("inf")

#     if len(lst)<4:
#         return None

#     for i in lst:
#         if i>big:
#             sbig=big
#             big=i
#         elif i>sbig and i!=big:
#             sbig=i

#     for j in lst:
#         if j<small:
#             ssmall=small
#             small=j
#         elif j<ssmall and j!=small:
#             ssmall=j

#     return sbig,ssmall

# lst=[8,9,5,5,6,6,8]
# print(sec_large_small(lst))
           


#FIND SEC LARGE AND SEC SMALL ELEMENT(using 1 loops)
# def sec_large_small(lst):
#     big=float("-inf")
#     sbig=float("-inf")
#     small=float("inf")
#     ssmall=float("inf")

#     if len(lst)<2:
#         return None

#     for i in lst:
#         #second largest
#         if i>big:
#             sbig=big
#             big=i
#         elif i>sbig and i!=big:
#             sbig=i

#         #second smallest
#         if i<small:
#             ssmall=small
#             small=i
#         elif i<ssmall and i!=small:
#             ssmall=i

#     return sbig,ssmall

# lst=[8,9,5,5,6,6,8]
# print(sec_large_small(lst))


#REMOVE ONLY THE SUB ARRAY THAT CONTAINS ALL OCCURANCE OF LARGEST ELEMENT(this solution is removing only maximum element from a list)
# def remove_subarray(lst):
#     maxi=float("-inf")
#     write=0

#     for i in lst:
#         if i>maxi:
#             maxi=i

#     for fast in range(len(lst)):
#         if lst[fast]!=maxi:
#             lst[write]=lst[fast]
#             write+=1

#     return lst[:write]

# arr = [1, 3, 7, 7, 2]
# print(remove_subarray(arr))


#FINDING WHEATHER A TARGET IS PRESENT.(1 METHOD)
# def find(lst,target):
#     res=[]
#     for i in lst:
#         for j in i:
#             res.append(j)

#     seen=set(res)
#     if target in seen:
#         return True
    
#     return False


# lst=[[1,2,3],[6,7,9],[11,34]]
# target=11
# result=find(lst,target)
# if result==True:
#     print("element founded")
# else:
#     print("not found")



#FINDING WHEATHER A TARGET IS PRESENT.(2 METHOD)
# def find(lst, target):
#     for sub in lst:
#         for val in sub:
#             if val == target:
#                 return True
#     return False

