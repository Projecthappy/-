with open('grades.txt','r') as f1:
  z=f1.read()
  c=z.replace('\n',',').replace(':',',').split(',')
for cs in range(2,len(c)):
  if c[cs].isdigit()==False:
    break
br,hr=[],[]
b=0
for h in range(0,int(len(c)/cs)):
  for i in range(2,cs):
    if c[i+h*cs]<'60':
      b=b+1
  if b>1:
    br.append(h)
  else:
    hr.append(h)
  b=0
with open('grades.txt','r') as f2:
  d=f2.readlines()
  with open('bad.txt','a') as f3:
    for i1 in br:
      f3.write(d[i1])
  with open('pass.txt','a') as f4:
    for i2 in hr:
      f4.write(d[i2])