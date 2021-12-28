def ha(lst):
    for i in range(len(lst)):
        for k in lst:
            if k>0:
                lst.remove(k)
                lst.append(k)
            else:
                continue
    return lst
print(ha([1,2,3,-5,-4,5,9,-8,1]))
