import sys
def linkedlist_intersection(group, graph) -> bool:
    tempGroup=[]
    for val in group:
        val=val.strip()
        tempGroup.append(val)
        group=tempGroup
    print("group",group,"graph",graph)
    interArray=[]
    for i in group:
        for j in graph:
            if i in j:
                if i not in interArray:
                    interArray.append(i)
                else:
                    print("Value already there, intersection found at",i)
                    return True
                print(i,j)
            elif i not in j:
                if i in interArray:
                    interArray.remove(i)
                print(i,"is not there",j)
    print("ARR",interArray)
    return False

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
