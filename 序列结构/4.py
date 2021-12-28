a={'a':1,'b':2,'c':3,'d':4,'e':5}
print(a)
c=1
while c==1:
    b=input('请输入键：')
    if b<'f':
             print("键{}对应的值为:{}".format(b,a[b]))
    else:
             print('您输入的键不存在!')
