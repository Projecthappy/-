with open('grades.txt','w') as f0:
    f0.write('a:56\nb:58\nc:54')
with open('grades.txt','r') as f1:
    z=f1.read()
    print(z)
a,b,m,c=0,1,[],[]
z=z+' '
while b<len(z)+1:
    b=b+1
    if z[a:b].isalnum()==False:
        if z[a:b-1].isdigit():
            c.append(int(z[a:b-1]))
        else:
            m.append(z[a:b-1])
        a=b
        b=b+1
print('平均分为：'+str(sum(c)/len(c)))
d=dict(zip(c,m))
e=sorted(c)
with open('paixu.txt','w') as f2:
    for f in e:
        f2.write(str(d[f])+':'+str(f)+'\n')