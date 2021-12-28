def asorted(lista):
    u=[]
    temp=lista[::] 
    while temp:
        Min=min(temp)
        u.append(Min)
        temp.remove(Min)
    return u
print(asorted([5,4,8,3,4,5,1,2]))