num = int(input("enter nay number"))
k=1

for i in range(0,num):
    for j in range(0,i+1):
        print(k,end="")
        k=k+1
    print()