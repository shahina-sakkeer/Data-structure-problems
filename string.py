#REVERSE A STRING
# def reverse(st):
#     s=list(st)
#     left=0
#     right=len(st)-1

#     while left<right:
#         s[left],s[right]=s[right],s[left]
#         left+=1
#         right-=1

#     return "".join(s)

# s=input("enter a string : ")
# print(reverse(s))


#CHECK PALINDROME
# def palindrome(s):
#     left,right=0,len(s)-1

#     while left<right:
#         if s[left]!=s[right]:
#             return False
#         left+=1
#         right-=1
        
# s=input("Enter a string : ")
# res=palindrome(s)
# if res==False:
#     print("not palindrome")
# else:
#     print("palindrome")


#COUNT VOWELS IN A STRING
# def count_vowels(s):
#     count=0
#     vowels="aeiou"

#     for i in s.lower():
#         if i in vowels:
#             count+=1
#     return count

# s=input("enter a string : ")
# print(count_vowels(s))


#FIND THE FIRST CHARACTER THAT APPEARS ONLY ONCE
# def non_repeating(s):
#     count=0
    
#     for i in range(len(s)):
#         count=0
#         for j in range(len(s)):
#             if s[i]==s[j]:
#                 count+=1

#         if count==1:
#             return s[i]
    
# s=input("enter a string : ")
# print(non_repeating(s))     
# 


#REMOVING DUPLICATE CAHARCTERS. NOT CHANGING THE ORDER
# def remove_duplicate(s):
#     result=[]     #list will take the space complexity of o(n)

#     for i in s:    #loop takes o(n). this is time complexity
#         if i not in result:    #the result is a list which contains n length and also take o(n).
#             result.append(i)

#     return "".join(result)  #so total time to complete the loop take o(n^2)

# s=input("enter a string : ")
# print(remove_duplicate(s))



#REVERSE WORDS IN A SENTENCE
# def reverse_words(s):
#     st=list(s)
#     n=len(st)
#     start=0

#     for i in range(n):
#         if st[i]==" ":
#             left=start
#             right=i-1

#             while left<right:
#                 st[left],st[right]=st[right],st[left]
#                 left+=1
#                 right-=1
#             start=i+1

#     left,right=start,n-1
#     while left<right:
#         st[left],st[right]=st[right],st[left]
#         left+=1
#         right-=1

#     return "".join(st)

# s=input("enter a string : ")
# print(reverse_words(s))


#COUNT THE OCCURANCE OF GIVEN CHARACTER
# def occurance(s,target):
#     n=len(s)
#     count=0
#     for i in range(n):
#         if s[i]==target:
#             count+=1
#     return count

# s=input("enter a string : ")
# target=input("enter a letter : ")
# print(occurance(s,target))


#REMOVE ALLL VOWELS FROM A STRING
# def remove_vowels(s):
#     result=[]
#     vowels={'a','e','i','o','u'}

#     for i in s:
#         if i not in vowels:
#             result.append(i)
#     return "".join(result)

# s=input("enter a string : ")
# print(remove_vowels(s))


#REMOVE ALL SPACES FROM A STRING
# def remove_spaces(s):
#     lst=list(s)
#     result=[]

#     for i in s:   #dont need to iterate through lst. as string is iterable, you can directly iterate string.
#         if i != " ":
#             result.append(i)

#     return "".join(result)

# s=input("enter a string : ")
# print(remove_spaces(s))


#REPLACE ALL SPACES WITH -
# def replace_space(s):
#     result=[]

#     for i in s:
#         if i==" ":
#             result.append("-")
#         else:
#             result.append(i)

#     return "".join(result)

# s=input("enter a string : ")
# print(replace_space(s))


#REVERSE ONLY ALPHABET CHARACTERS
# def reverse_isaplha(s):
#     lst=list(s)
#     left=0
#     right=len(s)-1

#     while left<right:
#         if lst[left].isalpha() and lst[right].isalpha():
#             lst[left],lst[right]=lst[right],lst[left]

#             left+=1
#             right-=1

#         elif lst[left].isalpha() and not lst[right].isalpha():
#             right-=1
#         else:
#             left+=1

#     return "".join(lst)

# s=input("enter a string : ")
# print(reverse_isaplha(s))



#COUNT THE NUMBERS OF WORDS IN A STRING. not correct
# def count_words(s):
#     lst=list(s)
#     n=len(s)
#     count=0
#     start=0 

#     i=0
#     while i<n:
#         if lst[i] != " ":
#             count+=1
#         i=i+1
    
#     return count

# s=input("enter a string : ")
# print(count_words(s))


        
