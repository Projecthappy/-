a=1
while a>0:
   x=int(input('输入四位整数:'))
   if x%400==0:
      print('是闰年')
   elif x%4==0 and x%100!=0:
      print('是闰年')
   else:
       print('不是闰年')
