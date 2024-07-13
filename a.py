#sum of a digitwhile loop
# s=123
# sum=0
# while(s>0):
#     temp=s%10
#     sum=sum+temp
#     s=s//10
# print(sum)



#sum of a number with for lopp
# s=input("enter any number")
# sum=0
# for i in s:
#     sum=sum+int(i)
# print(sum)




#reverse a digit with for loop
# s=input("enter any value more than one value pleas")
# r=""
# for i in s:
#     r=i+r 
# print(int(r))



#reverse a digit with while loop
# s=123
# rev=0
# while(s>0):
#     temp=s%10
#     rev=(rev*10)+temp
#     s=s//10
# print(rev)

#wrt to creat a number pyramit it started with 3 and 44 and 555 with two for loop
# n= int(input("enter any number"))
# k=3

# for i in range(1,n):
#     for j in range(i):
#         print(k,end="")
#     print()
#     k+=1



#wrt to creat a number pyramit it started with 3 and 44 and 555 mirror with two for loop
# n = int(input("enter a number"))
# k=3
# for i in range(1,n):
#     for j in range(i):
#         print(k,end="")
#     print()
#     k+=1
# k=k-2
# for t in range(1,n-1):
#     for h in range(1,n-t):
#          print(k,end="")
#     print()
#     k-=1


#wrt to creat a number pyramit it started with 3 and 44 and 555 with one for loop
# n= int(input("enter any number"))
# k=3
# for i in range(1,n):
#     print(str(k)*i)
#     k=k+1


#wrt to creat a number pyramit it started with 3 and 44 and 555 mirror with two for loop
# n=int(input("entermany value"))
# k=3
# for i in range(1,n):
#     print(str(k)*i)
#     k+=1
# k=k-2
# for j in range(1,n-1):
#     print(str(k)*(n-j-1))
#     k-=1


#wrt a program to creat a mirror pramid
# n=int(input("entre any value"))
# m=1
# for i in range(1,n):
#     print(" "*(n-i-1),"*"*m) 
#     m=m+2
# m=m-2
# for j in range(n):
#     print(" "*j,"*"*m)
#     m=m-2



#wtpnto creat a half pramid mirror with two loop
# s=6
# for i in range(1,s):
#     for j in range(i):
#         print("*",end="")
#     print()
# for t in range(1,s-1):
#     for f in range(1,(s-t)):
#         print("*",end="")
#     print()



#wtpnto creat a half pramid with two loop
# s=6
# for i in range(1,s):
#     print("*"*i)
# for j in range(1,s-1):
#     print("*"*(s-j-1))


#wtpnto creat a half pramid with two loop
# s=6
# for i in range(1,s):
#     print(" "*(s-i-1),"*"*i)
# for j in range(1,s):
#     print(" "*j,"*"*(s-j-1))

\

#wrt a program to creat a opposite mirror pramid
# s=10
# for i in range(s-1,-1,-1):
#     print(" "*(s-i-1),"*"*(2*i+1))
# for j in range(s):
#     print(" "*(s-j-1),"*"*(2*j+1))
   



#wrt a pramid of a number with two for loop
# s=4
# k=1
# for i in range(1,s):
#   for j in range(i):
#     print(k,end="")
#     k=k+1
#   print()


#/////////////////////////////////////////////////////////////////
#wrp to shoe a number is prime number
# s= int(input("entervksxn"))
# if s==1 or s==0:
#   print("not prime number")

# for i in range(2,s):

#   if s%i==0:
#     print("number is not prime number")
#     break
# else:
#     print("number is prime")



#wrp to shoe a number is prime number in range
# s= int(input("enter any number"))
# for i in range(2,s):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)




#power of a number
# import math as m
# a=int(input("enter a number"))
# b= int(input("enter a number "))

# d=pow(a,b)
# print(d)



#palindrom number program for loop
# s=input("enter any number pailndram")

# rev=""
# for i in s:
#   rev=i+rev 
# print(s)
# if s==rev:
#   print("number in palindrom",rev)
# else:
#   print("number is not palindrom")  




# palindrom number program while loop
# s= int(input("enter any number"))
# n=s
# rev=0
# while s>0:
#     temp=s%10
#     rev=(rev*10)+temp
#     s=s//10
# if rev==n:
#     print("number is palindrom")
# else:
#  print("number is not palindrom")



#armstrong number with for loop
# s=input("enter a number")
# c=0
# d=len(s)
# for i in s:
#     c+=int(i)**d
# if int(s)==c:
#     print("number is arm strong number")
# else:
#     print("not arm strong number")



# #armstrong number with while loop
# s=int(input("ahdvja"))
# m=s
# n=len(str(s))
# sum=0
# while(s>0):
#     temp= s%10
#     sum+=temp**n
#     s=s//10
# if m==sum:
#     print("armstrong number")
# else:
#     print("not armstrong number")



#power of a number
# a=int(input("vnxn"))
# b=int(input("khkbs"))
# print(a**b)


#check a number is positive or negative
# s= int(input("ente any number for cheking"))

# if s>0:
#     print("number in not positive")
# elif s<0:
#     print("number in negative")
# else:
#     print("number is zero")



#fibonacciseries 
# n=int(input("enter a loop end point"))
# a=0
# b=1
# print(a,"\n",b)
# for i in range(n):
#     c=a+b
#     a=b
#     b=c
#     print(c)



#check number is even or odd
# s= int(input("enter any number"))

# if s%2==0:
#     print("entered number in even number")
# else:
#     print("number is not prime")


#wrtap to find factorial of a number by user
# s=int(input("enter a number for checking numbetrs factorial"))
# sum=1
# for i in range(1,s+1):
#     sum*=i 
#     print(sum)


#find area of a circle
# r=int(input("enter  radius of a circle"))
# p=3.14
# area=p*r*r
# print(area)


#find area of a triangle
# b=int(input("ente any number base"))
# h=int(input("ente height of a triangle"))

# triagle = b*h/2
# print(triagle)



#find factor of a number 
# s=int(input("enter a nubmer for checking numbers factor"))
# if s>0:
#    for i in range(2,s):
#       if s%i==0:
#          print(i)
# else:
#     print("invalid value")


#reverse of a number
# s=input("enter a number ")
# r=""
# for i in s:
#     r=i+r
# print(int(r))



#abundant number
# s=int(input("enter a number"))
# sum=0
# for i in range(2,s):
#     if s%i==0:
#         sum+=i
# if sum > s:
#     print("entered number is abundant number")
# else:
#     print("number is on abundant")




#perfect number
# s=int(input("enter number"))
# sum=0
# for i in range(1,s):
#  if s%i==0:
#     sum+=i
# if s==sum:
#     print("number is perfect number")
# else:
#     print("number is not perfect")



#strong number
# s=input("enter number")
# sum=1
# d=0
# for i in s:
#     i=int(i)
#     for j in range(1,i+1):
#         sum*=j
#     d+=sum
#     sum=1
# print(s)
# if d == int(s):
#     print("number is strong number")
# else:
#     print("number is not strong")






#replace all 0 with 1 in a given 
# s=input("enter any integer number")
# r=''
# for i in s:
#     if int(i)==0:
#         i='1'
#         r=r+i
    
#     else:
#         r=r+i
# print(int(r))
        



#replace all 0 with 1 in a given integers
# s=int(input("enter any integer number"))
# r=0
# while(s>0):
#     temp = s%10
#     if temp==0:
#         temp=1
#     s=s//10    
#     r=(r*10)+temp
# print(r)


#count number of integer in a variable with for loop
# s=input("enter any value")
# c=0
# for i in s:
#     c+=1
# print(c)



#count number of integer in a variable with for loop
# s=112233
# c=0
# while(s):
#     c+=1
#     s=s//10
# print(c)