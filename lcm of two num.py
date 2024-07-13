a=int(input("enter any  first number "))
b=int(input("entre any second number"))
if a<b:
    min=a
else:
    min=b

for i in range(min, (a *b )+1):
    if i%a==0 and i%b==0:
        lcm=i
        print("lcm of your two number is",lcm)
        break
    