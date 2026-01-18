# import sys
# print(sys.getrecursionlimit())

# sys.setrecursionlimit(100)
# print(sys.getrecursionlimit())

# i=0
# def greet():
#     global i
#     i=i+1
#     print("hello",i)
#     greet()

# greet()


#PRINT N NATURAL NUMBERS BACKWARD. THIS IS DIRECT RECUSRION
# def natural(n):
#     if n==0:
#         return 0
    
#     print(n, end=" ")
#     return natural(n-1)

# num=int(input("enter a number"))
# natural(num)



#INDIRECT RECURSION
# def num(x):
#     if x<=0:
#         return
#     print(x,end=" ")
#     num1(x-1)

# def num1(y):
#     print(y,end=" ")
#     num(y-1)

# num1(10)


#FACTORAIL OF A NUMBER
# def fact(n):
#     if n==0:
#         return 1
    
#     return n * fact(n-1)

# num=int(input("Enter the number: "))
# print(fact(num))



#PRINT NAME 10 TIMES WITHOUT LOOP
# def print_name(name,length):
#     if length==0:
#         return
#     print(name)
#     length=length-1
#     print_name(name,length)

# value=input("enter a name : ")
# size=int(input("Enter the limit : "))
# print_name(value,size)



#POWER OF A NUMBER 
# def power(num,value):
#     if value==0:
#         return 1
#     return num*power(num,value-1)

# n=int(input("enter a number"))
# limit=int(input("enter the power value"))
# print(power(n,limit))



#CHECK A NUMBER IS PRIME NUMBER OR NOT
# def prime(num,i=2):
#     if num <= 1:
#         return 0
#     if i==num:    #i now reaches to the num. that means it satisfy all prime number condition
#         return 1
#     if num%i==0:
#         return 0
#     return prime(num,i+1)

# n=int(input("enter a number : "))
# is_prime=prime(n)
# if is_prime==1:
#     print("prime")
# else:
#     print("not prime")



#COUNT THE NUMBER OF DIGITS IN A NUMBER
# def digits(n):
#     if n==0:
#         return 0

#     return 1 + digits(n//10)

# num=int(input("enter a number : "))
# print(digits(num))



#SUM OF FIRST N NUMBERS
# def sum(num):
#     if num<=0:
#         return 0
#     return num+sum(num-1)

# n=int(input("Enter the number : "))
# print(sum(n))


#REVERSE A STRING
# def reverse(s,index,new):
#     if index<0:
#         return new

#     return reverse(s,index-1,new+s[index])

# s=input("enter a string : ")
# print(reverse(s,len(s)-1))


#CHECK PALINDROME OR NOT (one method)
# def palindrome(st,index,n=""):
#     if index<0:
#         return n
    
#     n=n+st[index]
#     return palindrome(st,index-1,n)


# s=input("enter a string : ")
# new=s
# reversed_str=palindrome(s,len(s)-1)
# if reversed_str==new:
#     print("Palindrome")
# else:
#     print("Not palindrome")



#CHECK PALINDROME OR NOT (2nd method)
# def reverse(s,left,right):
#     if left>=right:
#         return True
        
#     if s[left]!=s[right]:
#         return False
        
#     return reverse(s,left+1,right-1)
  
# s="radar"
# print(reverse(s,0,len(s)-1))
    



#COUNT THE VOWELS OF A STRING
# def count_vowels(s,index):
#     vowels={'a','e','i','o','u'}

#     if index<0:
#         return 0
    
#     if s[index] in vowels:
#         return 1 + count_vowels(s,index-1)
#     else:
#         return count_vowels(s,index-1)

# string=input("enter a string : ")
# print(count_vowels(string,len(string)-1))



#SUM OF EVEN NUMBERS UPTO A LIMIT USING RECURSION
# def even_sum(limit):
#     if limit<=0:
#         return 0
    
#     if limit%2==0: 
#         return limit + even_sum(limit-1)
#     else:
#     return even_sum(limit-1)


# num=int(input("Enter a limit : "))
# print(even_sum(num))



#SUM OF EVEN NUMBERS OF A LIST USING RECURSION
# def sum_even(lst,index):
#     if index<0:
#         return 0
        
#     if lst[index] % 2==0:
#         return lst[index] + sum_even(lst,index-1)
#     else:
#         return sum_even(lst,index-1)


# lst=list(map(int,input("enter a list ").split()))
# print(sum_even(lst,len(lst)-1))



#SUM OF LIST
# def list_sum(lst,index):
#     if index<0:
#         return 0
    
#     return lst[index]+list_sum(lst,index-1)

# lst=list(map(int,input("enter a list ").split(" ")))
# print(list_sum(lst,len(lst)-1))



#PRINT FROM 1 TO N
# def print_n(n):
#     if n<=0:
#         return 0
    
#     print_n(n-1)
#     print(n,end=" ")

# num=int(input("enter the number : "))
# print_n(num)


#MAXIMUM VALUE FROM THE LIST
# def maximum(lst,index):
#     if index==0:
#         return lst[0]
    
#     if lst[index]>maximum(lst,index-1):
#         return lst[index]
#     else:
#         return maximum(lst,index-1)
    
# l=list(map(int,input("Enter a list : ").split(" ")))
# print(maximum(l,len(l)-1))



#COUNT HOWMANY TIMES THE TARGET ELEMENT APPEAR IN A LIST
# def count_target(lst,index,target):
#     if index<0:
#         return 0
    
#     if lst[index]==target:
#         return 1 + count_target(lst,index-1,target)
#     else:
#         return count_target(lst,index-1,target)

# lst=list(map(int,input("enter a list : ").split(" ")))
# target=int(input("enter the target : "))
# print(count_target(lst,len(lst)-1,target))



#REMOVE ALL OCCURANCE OF A GIVEN CHARACTER FROM A STRING
# def remove_char(st,index,target,n=""):
#     if index<0:
#         return n
    
#     if st[index]!=target:
#         n=st[index]+n
#         return remove_char(st,index-1,target,n)
#     else:
#         return remove_char(st,index-1,target,n)
    
# s=input("enter a string : ")
# key=input("enter a target : ")
# print(remove_char(s,len(s)-1,key))



#REMOVE ALL OCCURANCE OF A GIVEN CHARACTER FROM A STRING(another method)
# def remove_char(s,target,index=0,new=""):
#     if index==len(s):
#         return new
        
#     if s[index]!=target:
#         return remove_char(s,target,index+1,new+s[index])
#     else:
#         return remove_char(s,target,index+1,new)
        
# s=input("enter a string ")
# key=input("enter a target ")
# print(remove_char(s,key))


#FIBONACCI SERIES
# def fibonacci(limit):
#     if limit==0:
#         return 0
#     if limit==1:
#         return 1
#     return fibonacci(limit-1)+fibonacci(limit-2)


# n=int(input("Enter a limit : "))
# for i in range(n):
#     print(fibonacci(i))


#SUM OF DIGITS
# def sum_of_digits(num):
#     if num==0:
#         return 0
    
#     return (num%10) + sum_of_digits(num//10)

# n=int(input("Enter a number : "))
# print(sum_of_digits(n))


#SUM OF NUMBERS ONLY IF A LIST CONTAINS DIFFERENT DATATYPES
# def sum_num(lst,index):
#     if index<0:
#         return 0
    
#     if isinstance(lst[index],int) and not isinstance(lst[index],bool):
#         return lst[index]+sum_num(lst,index-1)
#     else:
#         return sum_num(lst,index-1)
    
# n=['a',1.2,3,'#',5,'w',True,False]
# print(sum_num(n,len(n)-1))



#HIDE L FROM HELLO
# def hide(s,index,target,n=""):
#     if index==len(s):
#         return n
    
#     if s[index]!=target:
#         n=n+s[index]
#         return hide(s,index+1,target,n)
#     else:
#         return hide(s,index+1,target,n)
    
# string=input("enter a string: ")
# target=input("enter the target : ")
# print(hide(string,0,target))
    


#REVERSING EACH WORD IN A SENTENCE
# def reverse_one_word(s,index,new=""):    #only this function is recursive function
#     if index<0:
#         return new
    
#     return reverse_one_word(s,index-1,new+s[index])


# def reverse_only_one(sentence):      #this one isi normal function
#     words=sentence.split()
#     result=[]

#     for w in words:
#         result.append(reverse_one_word(w,len(w)-1))

#     return " ".join(result)


# st="love my india"
# print(reverse_only_one(st))



#REMOVE EVEN NUMBERS FROM AN ARRAY.(wrong method. in string it works but not in list)
# def remove_even(lst,index,res=[]):
#     if index==len(lst):
#         return res
#     #Python evaluates function arguments before calling, so passing res.append() caused None to propagate.that means it will call res.append(lst[index] at first before calling outer recusrion function
#     if lst[index]%2!=0:
#         return remove_even(lst,index+1,res.append(lst[index]))
#     else:
#         return remove_even(lst,index+1)


# lst=[2,5,3,6,0,1,4,8,9]
# print(remove_even(lst,0))


#CORRECT VERSION FOR REMOVING EVEN NUMBERS FROM AN ARRAY
# def remove_even(lst,index,res):
#     if index==len(lst):
#         return res

#     if lst[index]%2!=0:
#         res.append(lst[index])

#     return remove_even(lst,index+1,res)


# lst=[2,5,3,6,0,1,4,8,9]
# print(remove_even(lst,0,[]))



#REMOVE A TARGET FROM AN ARRAY
# def remove_target(lst,res,index,key):
#     if index==len(lst):
#         return res
    
#     if lst[index]!=key:
#         res.append(lst[index])

#     return remove_target(lst,res,index+1,key)


# lst=[2,5,5,6,0,1,4,8,9]
# key=int(input("enter the target : "))
# print(remove_target(lst,[],0,key))



#REMOVE DUPLICATES FROM AN ARRAY
# def remove_duplicate(lst,res,index,seen):
#     if index==len(lst):
#         return res
    
#     if lst[index] not in seen:
#         seen.add(lst[index])
#         res.append(lst[index])

#     return remove_duplicate(lst,res,index+1,seen)

# lst=[4,5,5,6,6,6,7]
# print(remove_duplicate(lst,[],0,set()))



#NORMAL FLATTENING OF A LIST
# lst=[[1, 2], [3, 4], [5, 6]]
# new=[item for x in lst for item in x]
# print(new)


#RECURSIVELY FLATTENING A LIST
# def flatten_list(lst):
#     res=[]

#     for i in lst:
#         if isinstance(i,list):
#             res.extend(flatten_list(i))
#         else:
#             res.append(i)
#     return res

# lst=[1, [2, [3, 4], 5], [6, 7]]
# print(flatten_list(lst))


# NOTES:  res.append([2, 3, 4])   # WRONG → creates nested list
# res.extend([2, 3, 4])   # CORRECT → adds elements one by one


def prime(limit,i=2):
    if limit<=0:
        return
    
    if limit==i:
        
    
    if limit%i==0:



limit=int(input("enter a  limit : "))
print(prime(limit))
