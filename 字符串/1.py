print('执行开始'.center(16,'-'))
for i in range(11):
    a=''
    a='%{}'.format(i*10).ljust(4,' ')+'['+'*'*2*i+'->'+'.'*2*(10-i)+']'
    print(a)
print('执行结束'.center(16,'-'))