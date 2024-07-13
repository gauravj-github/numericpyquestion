n=int(input("enter any number"))
c=2

for i in range(1,n):
    for j in range(i):
        print(c,end="")
    c=c+1
    print()
