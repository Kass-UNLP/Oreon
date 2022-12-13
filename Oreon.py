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

    print(prettify(graph))
        
    ## ----> Reading of variables is tested and confirmed done correctly
    ## ----> Conversion of input is tested and confirmed done correctly
    ## ----> Prettyfi method is tested and confirmed done correctly
    
    
    pass