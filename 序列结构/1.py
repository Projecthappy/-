import random
a = [random.randint(0,101) for i in range(1000)]
for b in range(0,101,1):
   print(str(b)+'出现',str(a.count(b))+'次',end='\n')