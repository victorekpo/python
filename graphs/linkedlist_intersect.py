import sys
def linkedlist_intersection(group, graph) -> bool:
    tempGroup=[]
    for val in group:
        val=val.strip()
        tempGroup.append(val)
        group=tempGroup
    #print("group",group,"graph",graph)
    interArray=[]
    for item in group:
        for arr in graph:
            if item in arr:
                checkItems=arr[arr.index(item):]
                #print("To Check",checkItems)
                for i in checkItems:
                    if i not in interArray:
                       interArray.append(i)
                    else:
                        print("Intersection found at",i)
                        print(interArray)
                        return True
            elif item not in arr:
                if item in interArray:
                    interArray.remove(item)
                #print(item,"is not there",arr)
    #print("ARR",interArray)
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
