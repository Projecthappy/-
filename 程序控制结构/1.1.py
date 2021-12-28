import math
a=1
while a>0:
   x=int(input('请输入x的值：'))
   if x<0:
       y=0
   elif x>=0 and x<5:
       y=x
   elif x>=5 and x<10:
       y=(3*x-5)**0.5
   elif x>=10 and x<20:
       y=(1+x**2)*(x%7)//7
   elif x>=20:
       y=math.sin(x/180*math.pi)
   print(y)
