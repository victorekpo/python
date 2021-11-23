import sys
def linkedlist_intersection(group, graph) -> bool:
    tempGroup=[]
    for val in group:
        val=val.strip()
        tempGroup.append(val)
        group=tempGroup
    print(group)

    return (1>2)

graph = [] #edge list representation
for line in sys.stdin:
    if "->" in line:
        s=line.split("->")
        tempLine=[]
        for val in s:
            val=val.strip()
            tempLine.append(val)
            s=tempLine
        graph.append(s)
    elif "," in line:
        print(linkedlist_intersection(line.split(","), graph) )

print(graph)
