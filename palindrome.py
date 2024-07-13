a=int(input("dvjqhgd"))
t=a
dig=0
sum=0

while a!=0:
    sum=a%10
    dig=(dig*10)+sum
    a=a//10
if t==dig:
    print("your given number is plaindrome number ",t)
else:
    print("your numnber is not palindrome",t)