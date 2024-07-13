n=int(input("enter any number"))
count=10

for i in range(n):
    for i in range(n-1-i,0,-1):
        print(count,end="")
        count=count-1
    print()