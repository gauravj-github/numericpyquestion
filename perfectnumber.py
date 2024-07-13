a=int(input("enter any number"))
sum=0
for i in range(1,a):
    if(a%i==0):
        sum+=i
if a==sum:
    print("your number is perfect number",sum)
else:
    print("your number is not perfect number",sum)
       
