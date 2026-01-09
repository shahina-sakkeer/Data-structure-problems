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
#     vowels={'a','e','i','o','u'}
#     for i in s.lower():
#         if i in vowels:
#             count+=1

#     return count

# s=input("enter a string : ")
# print(count_vowels(s))



#FIND THE FIRST CHARACTER THAT APPEARS ONLY ONCE
# def non_repeating(s):
#     freq={}
    
#     for i in s:
#         freq[i]=freq.get(i,0)+1

#     for ch in s:
#         if freq[ch]==1:
#             return ch

# s=input("enter a string : ")
# print(non_repeating(s))   



#FIND THE FIRST CHARACTER THAT APPEARS ONLY ONCE
# def first_char(s):
#     dic={}
#     for i in s:
#         if i not in dic:
#             dic[i]=1
#         else:
#             dic[i]=dic[i]+1

#     for ch in s:
#         if dic[ch]==1:
#             return ch

# s=input("enter a string : ")
# print(first_char(s))    



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
# def remove(s):
#     lst=list(s)
#     write=0

#     for read in range(len(lst)):
#         if lst[read]!=" ":
#             lst[write]=lst[read]
#             write+=1

#     return "".join(lst[:write])

# s=input("enter a string : ")
# print(remove(s))



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



#COUNT THE NUMBERS OF WORDS IN A STRING.
# def count_words(s):
#     lst=s.split()
#     count=0

#     for i in lst:
#         count+=1

#     return count

# s=input("enter a string : ")
# print(count_words(s))




#REMOVING DUPLICATE CAHARCTERS. NOT CHANGING THE ORDER
# def remove(s):
#     res=[]
#     seen=set()

#     for i in s:
#         if i not in seen:
#             seen.add(i)
#             res.append(i)

#     return "".join(res)

# s=input("enter a string : ")
# print(remove(s))



#REMOVE DUPLICATES FROM STRING
# def remove_dup(s):
#     lst=list(s)
#     seen=set()

#     write=0
#     for read in range(len(lst)):
#         if lst[read] not in seen:
#             seen.add(lst[read])
#             lst[write]=lst[read]
#             write+=1
#     return "".join(lst[:write])

# s=input("enter a string : ")
# print(remove_dup(s))



#REMOVE ALL OCCURANCE OF GIVEN CHARACTER
# def remove_char(s,ch):
#     lst=list(s)
#     write=0

#     for read in range(len(lst)):
#         if lst[read] != ch:
#             lst[write]=lst[read]
#             write+=1

#     return "".join(lst[:write])

# s=input("enter a string : ")
# ch=input("enter a char : ")
# print(remove_char(s,ch))

            

#FIND THE LONGEST WORD FROM A STRING
# def long(s):
#     lst=s.split()
#     strmaxi=""
#     maxi=0

#     for i in lst:
#         count=0
#         for j in i:
#             count+=1
            
#         if count>maxi:
#             maxi = count
#             strmaxi=i

#     return strmaxi
        

# s="find the longest string using one loop"
# print(long(s))





# def repeating(s):
#     dic={}
#     res=[]

#     for i in s:
#         if i in dic:
#             dic[i]=dic[i]+1
#         else:
#             dic[i]=1

#     for x in dic:
#         if dic[x]!=1:
#             res.append(x)
    
#     return res

# s=input("enter a string ")
# print(repeating(s))



#CHECK 2 STRINGS ANAGRAM OR NOT
# def anagram(str1,str2):
#     dic1={}
#     dic2={}

#     for i in str1:
#         if i not in dic1:
#             dic1[i]=1
#         else:
#             dic1[i]=dic1[i]+1

#     for j in str2:
#         if j not in dic2:
#             dic2[j]=1
#         else:
#             dic2[j]=dic2[j]+1

#     if dic1==dic2:
#         return True
#     else:
#         return False    


# str1="radar"
# str2="rrrra"
# print(anagram(str1,str2))

