import random
x = [random.randint(0,100) for i in range(20)]
print(x)
a = x[:10:]
b = x[10:20:]
a.sort()
b.sort(reverse=False)
print(a)
print(b)
