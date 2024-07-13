a=[1,2,3,4,5,6,7,8,9,10]
c=0
m=0

for i in a:
   if i%2==0:
        c+=1
    
   else:
        m+=1
print("number of odd",m)
print("number of enen", c)