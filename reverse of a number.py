a=123
rev=0


while a!=0:
    dig=int(a%10)
    rev=(rev*10)+dig
    a=a // 10
print(rev)