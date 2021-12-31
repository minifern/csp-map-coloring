# map-coloring

Constraint Satisfaction Problem (CSP) representation of graph coloring problem, using a backtracking algorithm with forward checking and most remaining values (MRV) and degree heuristics. 

Input File Format:
```bash
n m # represents the number of nodes (n) and number of domain values (m)
R1 R2 R3 R4 R5 R6 R7 R8 # country names [variable char length]
R G B Y # domain values [one char]
# n x n adjacency matrix
# i, j for rows, cols with 1 if country i is adjacent to country j and 0 if not
0 1 1 1 1 1 0 1 
1 0 1 1 0 0 1 1
1 1 0 1 0 0 0 0
1 1 1 0 1 1 1 0
1 0 0 1 0 1 0 0 
1 0 0 1 1 0 1 1
0 1 0 1 0 1 0 1
1 1 0 0 0 1 1 0
```

# To Run
1) Change variable ```inputFile``` and ```outputFile``` to desired file names in ```mapColoring.py```
2) With Python installed, open command line
3) Navigate to directory containing ```mapColoring.py``` file
4) Run ```python mapColoring.py```

Results will be displayed in specified output file format

Output File:

```bash
# country name = chosen domain value
R1 = G
R2 = B
R3 = Y
R4 = R
R5 = Y
R6 = B
R7 = Y
R8 = R
```
