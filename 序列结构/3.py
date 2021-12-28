x = eval(input('请输入一个列表:'))
a,b = input('请输入两个下标').split(',')
c = x[int(a):int(b)+1:]
print(c)