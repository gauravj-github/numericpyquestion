n=int(input("enter any number"))

for i in range(1,n):
    print(" "*int(n-i)+"*"*i)
for j in range(1,n):
    print(" "*int(j+1)+"*"*int(n-j-1))