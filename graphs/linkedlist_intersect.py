import sys
def linkedlist_intersection(group, graph) -> bool:
    print("working")

graph = []
for line in sys.stdin:
    if "->" in line:
        s=line.split("->")

        graph.somehow_add( s[0], s[1])

    elif "," in line:
        print(linkedlist_intersection(line.split(","), graph) )

