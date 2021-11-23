import sys
graph=[]
for line in sys.stdin:
    if "->" in line:
      s=line.split("->")
    tempLine=[]
    for val in s:
        val=val.strip()
        tempLine.append(val)
        s=tempLine
    graph.append(s)
print(graph)

