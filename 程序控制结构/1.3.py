import random
x = [random.randint(0,100) for i in range(50)]
print(x)
for a in range(49,0,-1):
    if x[a]%2==1:
       x.pop(a)
print(x) 
