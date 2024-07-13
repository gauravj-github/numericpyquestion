n=int(input("enter any number"))
k=3

for i in range(1,n):
    print(str(k)*i)
    k=k+1
k=k-2
for i in range(n-2,0,-1):
    print(str(k)*i)
    k=k-1