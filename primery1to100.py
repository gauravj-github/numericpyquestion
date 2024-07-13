prime=int(input("enter any number for finding all prime between this number "))

for i in range(2,prime+1):
    
    for j in range(2,i):
        if i%j==0:
            break
    else:
      print(i)
      
            
