a=[10,20,40,30,50,20,10,20]
d=[]
c=0

for i in a:
    if i not in d:
        d.append(i)
        c+=1
print(c)