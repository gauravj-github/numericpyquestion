a=123
sum=0

while a!=0:
    dig=int(a%10)
    sum+=dig
    a=a/10
print("sum of a given digit",sum)