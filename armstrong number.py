import math as m
a=input("enter any number")
n=int(a)
dig=0
d=len(a)
for i in a:
   dig+=m.pow(int(i),d)


if dig==n:
    print("number is arm strong",int(dig))
else:
    print("number is not arm strong",int(dig))