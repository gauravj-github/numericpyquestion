n=int(input("enter any number"))


for i in range(1,n):
    print(" "*(n-i)+"*"*(i+i-1))

for i in range(1,n):
    print(" "*i+"*"*((n+n-1)-i*2))

