import math as m

a=int(input("enter any number for check automorphic number"))
num=str(a)
s=pow(a,2)
d=str(s)

if d.endswith(num):
    print("number is automorphic",d)
else:
    print("number is not auto morphic",d)
