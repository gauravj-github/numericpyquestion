sum=1
n=int(input("enter any number"))
for i in range(0,n):
    print(" "*int(n-1-i) + "*"*sum)
    sum=sum+2
