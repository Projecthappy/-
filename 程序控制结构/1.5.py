b=0
while b<5:
   x=int(input('输入一个整数'))
   a=0
   for i in range(2,x):
          if x%i==0:
              a=a+1
              print('不是素数')
              break
   if a==0:
       print('是素数')
