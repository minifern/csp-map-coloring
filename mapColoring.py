from __future__ import print_function
import sys
import copy

# class representation of map to color
class Map():
    def __init__(self, countries, colors, matrix):
        self.countries = countries # list of string countries
        self.colors = colors # list of char colors
        self.matrix = matrix # adjacency matrix
        self.n = len(countries) # number of countries [nodes]
        self.m = len(colors) # number of colors [domain]

    # returns number of constraints on a country given index
    def findConstr(self, solution, country):
        constraints = 0
        for i in self.matrix[country]:
            # only consider unassigned countries
            if i == '1' and solution[country] == -1:
                constraints += 1
        return constraints
    
    # determines if color is valid assignment
    def isLegal(self, solution, country, color):
        for i in range(self.n):
            if(self.matrix[country][i] == '1' and color == solution[i]):
                return False
        return True

# functions to update variables not in Map class
# returns updated version of variable
# parameters
    # domDict: dictionary of all countries mapped to valid domain colors
    # sol: dictionary of  countries mapped to their solution colors, -1 if not colored
    # history: list of expanded countries
    # country: index of country to expand
    # color: index of color to assign

def updateDom(domDict, country, color):
    update = domDict[country]
    update[color] = ''
    return update

def updateSolDict(sol, country, color):
    update = sol
    update[country] = color
    return update

def updHist(history, country, color):
    update = copy.deepcopy(history)
    update.append(country)
    return update

# functions to implement forward checking

def addInference(mc, solution, domDict, country, color):
    # remove color from domain of all neighboring countries
    for i in range(mc.n):
        if(mc.matrix[country][i] == '1' and solution[i] == -1):
            domDict[country] = updateDom(domDict, country, color)
    # check for failure
    for dom in domDict[country]:
        if dom != '':
            return (True, domDict)
    return (False, domDict)

def removeInference(mc, domDict, solution, country, color):
    for i in range(mc.n):
        if(mc.matrix[country][i] == '1' and solution[i] == -1):
            domDict[i][color] = mc.colors[color]
    return domDict
    

# function to implement mrv then degree heuristic
# returns index of country to evaluate
# parameters
    # mc: Map instance
    # solution: dictionary of  countries mapped to their solution colors, -1 if not colored
    # domDict: dictionary of all countries mapped to valid domain colors
def calcHeuristic(mc, solution, domDict):
    # mrv heuristic
    mrv = []
    maxDom = -1
    for i in range(mc.n):
        if solution[i] == -1:
            curDom = len([ct for ct in domDict[i] if ct != ''])
            if curDom >= maxDom:
                maxDom = curDom
                mrv.append((i, curDom))
    degree = []
    for c, d in mrv:
        if d == maxDom:
            degree.append((c, d))

    # degree heuristic
    maxConstr = (0, -1)
    for c, dom in degree:
        curConstr = mc.findConstr(solution, c)
        if curConstr >= maxConstr[1]:
            maxConstr = (c, curConstr)

    return maxConstr[0]

# recursive backtracking function to execute map coloring
# returns when all countries have been colored
# parameters
    # mc: Map instance
    # domDict: dictionary of all countries mapped to valid domain colors
    # solution: dictionary of  countries mapped to their solution colors, -1 if not colored
    # history: list of expanded countries
    # country: index of country to expand
def coloring(mc, domDict, solution, history, country):
    for color in range(mc.m):
        if mc.isLegal(solution, country, color):
            # remove color from domain of updated country
            domDict[country] = updateDom(domDict, country, color)

            # FORWARD CHECKING
            fwc = addInference(mc, solution, domDict, country, color)
            if(fwc[0]):
                domDict = fwc[1]
                # update solution list
                solution = updateSolDict(solution, country, color)
            else:
                domDict = removeInference(mc, solution, domDict, country, color)

            # update history list
            history = updHist(history, country, color)

            if(len(history) <= mc.n):
                coloring(mc, domDict, solution, history, calcHeuristic(mc, solution, domDict))
            else:
                return True
    return False

# function to execute map coloring
def runMapColoring(countries, colors, adjMatrix, outputFile):
    # create Map
    mc = Map(countries, colors, adjMatrix)

    # collections for search
    domDict = {i: copy.deepcopy(colors) for i in range(len(countries))}
    solution = {i: -1 for i in range(len(countries))}
    history = []

    # call backtracking function
    failure = coloring(mc, domDict, solution, history, calcHeuristic(mc, solution, domDict))

    if failure:
        return failure
    else:
        # write to file
        toFile(mc, solution, outputFile)

# output to file
# parameters
    # solution: list with selected colors
    # outputFile: name of file to output results
def toFile(mc, solution, outputFile):
    with open(outputFile, 'w') as outputFile:
        sys.stdout = outputFile # std out is output file 
            
        for c in solution:
            print(mc.countries[c] + " = " + mc.colors[solution[c]])

    # Reset stdout
    sys.stdout = sys.__stdout__

# function to read information from file
def main():
    inputFile = "mapInput.txt"
    outputFile = "Output1.txt"

    #read lines from file
    with open(inputFile) as textFile:
        values = textFile.readline()
        countries = textFile.readline()
        colors = textFile.readline()
        adj = textFile.readlines()

    textFile.close()

    #represent n and m
    n = values.split()[0]
    m = values.split()[1]

    #represent countries
    countries = countries.split()

    #represent colors
    colors = colors.split()

    #represent adjacency matrix
    adjMatrix = []
    tempArr = []
    for row in adj:
        for char in row:
            if char == '1' or char == '0':
                tempArr.append(char)
        adjMatrix.append(tempArr)
        tempArr = []

    # run backtracking algorithm
    runMapColoring(countries, colors, adjMatrix, outputFile)

#run script
main()