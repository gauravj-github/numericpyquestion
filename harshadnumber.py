a=input("enter any value")
b=int(a)
sum=0
for i in a:
    sum+=int(i)
if b%sum==0:
    print("your number is harshad number",a)
else:
    print("your nunber is not harshad number",a)