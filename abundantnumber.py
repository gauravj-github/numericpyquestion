a=int(input("enter any number"))
sum=0

for i in range(1,(a//2)+1):
    if a%i==0:
        sum+=i
print(sum)
if sum>a:
    print("number is abundant",a)
else:
    print("number is not abundant",a)