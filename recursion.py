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
#         return
    
#     print(n)
#     natural(n-1)

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
#     if i==num:
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
# count=0
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
# def reverse(string,i):
#     if i<0:
#         return
#     print(string[i],end="")
#     return reverse(string,i-1)

# s=input("enter a word : ")
# reverse(s,len(s)-1)


#CHECK PALINDROME OR NOT
# def palindrome(s,i,n=""):
#     if i<0:
#         return n
    
#     n=n+s[i]
#     return palindrome(s,i-1,n)

# st=input("enter a string : ")
# ss=st
# is_palindrome=palindrome(st,len(st)-1)
# if is_palindrome==ss:
#     print("palindrom")
# else:
#     print("not palindrom")


#COUNT THE VOWELS OF A STRING
# def count_vowels(s):
#     if s=="":
#         return 0
#     vowels="aeiouAEIOU"

#     if s[0] in vowels:
#         return 1 + count_vowels(s[1:])
#     else:
#        return count_vowels(s[1:])

# st=input("Enter a string : ")
# print(count_vowels(st))


#SUM OF EVEN NUMBERS USING RECURSION
# def even_sum(limit):
#     if limit<=0:
#         return 0
    
#     if limit%2==0: 
#         return limit + even_sum(limit-1)
  
#     return even_sum(limit-1)


# num=int(input("Enter a limit : "))
# print(even_sum(num))


#SUM OF LIST
# def sum_list(lst,i):
#     if i<0:
#         return 0
    
#     return lst[i] + sum_list(lst,i-1)

# l=list(map(int,input("enter a list : ").split(" ")))
# size=len(l)-1
# print(sum_list(l,size))



#PRINT FROM 1 TO N
# def print_n(n):
#     if n<=0:
#         return 0
    
#     print_n(n-1)
#     print(n,end=" ")

# num=int(input("enter the number : "))
# print_n(num)


#MAXIMUM VALUE FROM THE LIST
# def max_num(lst,i):
#     if i==0:
#         return lst[0]
    
#     if lst[i] > max_num(l,i-1):
#         return lst[i]
#     else:
#         return max_num(l,i-1)

# l=list(map(int,input("Enter a list : ").split(" ")))
# size=len(l)-1
# print(max_num(l,size))


#COUNT HOWMANY TIMES THE TARGET ELEMENT APPEAR IN A LIST
# def count_target(lst,target,i):
#     if i==0:
#         return 1 if lst[0]==target else 0

#     if lst[i] == target:
#         return 1 + count_target(lst,target,i-1)
#     else:
#         return count_target(lst,target,i-1)

# l=list(map(int,input("Enter a list : ").split(" ")))
# target=int(input("enter target : "))
# size=len(l)-1
# print(count_target(l,target,size))


#REMOVE ALL OCCURANCE OF A GIVEN CHARACTER FROM A STRING
# def new_string(s,char):
#     if s=="":
#         return ""
    
#     if s[0]==char:
#         return new_string(s[1:],char)
#     else:
#         return s[0]+new_string(s[1:],char)

# st=input("Enter a string : ")
# char=input("enter the character : ")
# print(new_string(st,char))

