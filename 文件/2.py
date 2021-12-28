with open('haha.txt','w') as f1:
    f1.write('hjhjhjGFYFGyfFTGGFhjuhuFGHjhY')
f2=open('haha.txt','r')
f3=f2.read().swapcase()
f2=open('haha.txt','w')
f2.write(f3)
f2.close()