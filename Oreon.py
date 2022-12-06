# Oreon


from sys import stdin, stdout



# Auxiliar dict for the purpose of printing the result in the correct format
to_letter = {
    0: "A",
    1: "B",
    2: "C",
    3: "D",
    4: "E",
    5: "F",
    6: "G",
    7: "H",
    8: "I",
    9: "J",
    10: "K",
    11: "L",
    12: "M",
    13: "N",
    14: "O",
    15: "P",
    16: "Q",
    17: "R",
    18: "S",
    19: "T",
    20: "U",
    21: "V",
    22: "W",
    23: "X",
    24: "Y",
    25: "Z"
}

iter = int(stdin.readline())

for i in range(1, iter + 1):
    number_of_cities = int(stdin.readline())
    
    # Maybe graph = []*number_of_cities is more appropriate, see later how it behaves
    graph = [[0]*number_of_cities]*number_of_cities
    
    for i in range(number_of_cities):
        graph[i] = [int(x) for x in stdin.readline().split(', ')]
    
    for row in graph:
        print(row)
        
    ## ----> Reading of variables is tested and confirmed done correctly
    pass