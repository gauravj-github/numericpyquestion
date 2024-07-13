a=int(input("enter an number "))

if a<=0 or a==1:
  print("not prime number",a)

  for i in range(2,a):
      if a%i==0:
        print("not prime number",a)
        break
else:
  print("prime number",a)