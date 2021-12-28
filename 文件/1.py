with open('data.txt','w') as fp:
    fp.write('45,345,24,24,4,65,7,45,43,43,7,78,87,78')
with open('data.txt','r') as fp:
    f1=str(sorted(map(int,fp.read().split(','))))
    with open('data_asc.txt','w') as fp:
        fp.write(f1)