i=int(input("enter any number"))
j=int(input("enter second number"))
small=0
if i<j:
    small=i
else:
    small=j
for c in range(2,small):
    if i%c==0 and j%c==0:
        hcf=c
print(hcf)