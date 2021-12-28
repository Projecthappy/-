a=1
z={}
while a<5:
    name,score=eval(input('请输入第'+str(a)+'个学生的姓名与成绩：'))
    z.update({name:score})
    a=a+1
print('打印学生姓名和成绩信息')
print(z)
print("成绩的最大值为："+str(max(z.values())))
print("成绩的最小值为："+str(min(z.values())))
print("成绩的平均值为："+str(sum(z.values())/len(z)))
