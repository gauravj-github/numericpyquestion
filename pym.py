n=int(input("enter any number"))
c=6

for i in range(n):
    for i in range(n-1-i,0,-1):
        print(c,end="")
    print()
    c=c-1