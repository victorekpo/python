import sys
a=sys.stdin.readlines()
v=[]
for i in a:
    i=i.split("->")
    temp=[]
    for j in i:
        j=j.strip()
        temp.append(j)
        i=temp
    v.append(i)
print(v)

