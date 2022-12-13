# Oreon
from sys import stdin, stdout


# Auxiliar dict for the purpose of printing the result in the correct format
to_letter = {
    1: "A",
    2: "B",
    3: "C",
    4: "D",
    5: "E",
    6: "F",
    7: "G",
    8: "H",
    9: "I",
    10: "J",
    11: "K",
    12: "L",
    13: "M",
    14: "N",
    15: "O",
    16: "P",
    17: "Q",
    18: "R",
    19: "S",
    20: "T",
    21: "U",
    22: "V",
    23: "W",
    24: "X",
    25: "Y",
    26: "Z"
}

def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
        
    return parent[i]

def union(parent, rank, x, y):
    if rank[x] < rank[y]:
        parent[x] = y
        
    elif rank[x] > rank[y]:
        parent[y] = x

    else:
        parent[y] = x
        rank[x] += 1


def KruskalMST(V, graph):
    i = 0
    j = 0
    MST_graph = []

    # Sorting non-decreasing as was found online.
    aux_graph = sorted(graph, key=lambda item: item[2])
    
    # print(aux_graph)

    parent = []
    rank = []

    # Using V+1 to avoid bugs, pos 0 of list is unused
    for node in range(V+1):
        parent.append(node)
        rank.append(0)

    # Edges = V-1
    while j < (V - 1):
        try:
            u, v, w = aux_graph[i]  
        except:
            break
        
        i = i + 1
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            j = j + 1
            MST_graph.append([u, v, w])
            union(parent, rank, x, y)

    # print("MST:")
    # for u, v, weight in MST_graph:
    #     print("Edge from " + str(u) + " to " + str(v) + " with weight " + str(weight))
    
    return MST_graph


def prettify(MSTGraph):
    global to_letter
    
    for elem in MSTGraph:
        elem[0] = to_letter[elem[0]]
        elem[1] = to_letter[elem[1]]
    
    return MSTGraph



iter = int(stdin.readline())

for i in range(1, iter + 1):
    number_of_vertex = int(stdin.readline())
    
    graph = []
    
    ## Proceed to adapt input graph to a (x, y, v) format, where x and y are vertex and v is the weight of the connection.
    for x in range(number_of_vertex):
        aux = [int(z) for z in stdin.readline().split(', ')]
        
        print(aux)
        
        x += 1
        y = 0
        v = 0
        
        for conn in aux:
            print(conn)
            
            y += 1
            
            if conn != 0:
                v = conn
                graph.append([x, y, v])

    # print(prettify(graph))
    MSTGraph = KruskalMST(number_of_vertex, graph)
    print(prettify(MSTGraph))
        
    ## ----> Reading of variables is tested and confirmed done correctly
    ## ----> Conversion of input is tested and confirmed done correctly
    ## ----> Prettyfi method is tested and confirmed done correctly
    ## ----> Kruskal algorithm inserted, tested with base case shown in premise, confirmed to be working correctly
    
    
    pass