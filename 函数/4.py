def haha(a):
    d,x,s,q=0,0,0,0
    for i in a:
        if i.isupper()==True:
            d=d+1
        elif i.islower()==True:
            x=x+1
        elif i.isdigit()==True:
            s=s+1
        else:
            q=q+1
    z=(d,x,s,q)
    print(z)