# map-coloring

Constraint Satisfaction Problem (CSP) representation of graph coloring problem, using the backtracking algorithm with forward checking and most remaining values (MRV) and degree heuristics. 

Input File Format:
```bash
n m # represents the number of nodes (n) and number of domain values (m)
x1, x2, x3 # country names [variable char length]
v1, v2, v3 # domain values [one char]
# n x n adjacency matrix
# i, j for rows, cols with 1 if country i is adjacent to country j and 0 if not
n n n
n n n
n n n
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
x1 = v2
x2 = v1
x3 = v3
```
