import os
from collections import deque
import queue as Q
initialState = ""
searchMethod = ""
options = ""


userInput = input("Enter the initial state followed by search method and options: ")
userInput = userInput.split()
if (len(userInput) == 4):
    initialState = userInput[0][1:]
    initialState = initialState + " " + userInput[1][:len(userInput[1]) - 1]
    searchMethod = userInput[2]
    options = userInput[3]
else:
    initialState = userInput[0][1:]
    initialState = initialState + " " + userInput[1][:len(userInput[1]) - 1]
    searchMethod = userInput[2]
endState = sorted(initialState)
endState.append(endState.pop(endState.index(" ")))
endState = "".join(endState)
root = (initialState, 0, "")
def treeSearch(problem, strategy, endState, option):
    result = [-1,-1,-1,-1]
    numExpanded = 0
    maxFringe = 0
    numCreated = 0
    depth = -1
    
    mySet = set()
    if (strategy == "DFS" or strategy == "DLS"):
        stack = [problem]

        while (len(stack) != 0):
            temp = stack.pop()
            spaceLoc = temp[0].index(" ")
            if(temp[0] == endState or temp[0] == "123456789ABCDFE " ):
                depth = temp[1]
                result = [depth, numCreated, numExpanded, maxFringe]
                return result
            if (strategy != "DLS" or (strategy == "DLS" and temp[1] < int(option))):
                if((temp[0],temp[2] ) not in mySet):
                    numExpanded = numExpanded + 1
                    mySet.add((temp[0], temp[2]))
                    if (validMove(spaceLoc, "up")):
                        stack.append((movePiece(temp[0], spaceLoc, "up"), temp[1] + 1, temp[0]))
                        numCreated = numCreated + 1
                    if (validMove(spaceLoc, "left")):
                        stack.append((movePiece(temp[0], spaceLoc, "left"), temp[1] + 1, temp[0]))
                        numCreated = numCreated + 1
                    if (validMove(spaceLoc, "down")):
                        stack.append((movePiece(temp[0], spaceLoc, "down"), temp[1] + 1, temp[0]))
                        numCreated = numCreated + 1
                    if (validMove(spaceLoc, "right")):
                        stack.append((movePiece(temp[0], spaceLoc, "right"), temp[1] + 1, temp[0]))
                        numCreated = numCreated + 1    
                    if len(stack) > maxFringe:
                        maxFringe = len(stack)

    if (strategy == "BFS"):
        queue = deque([problem])

        while (len(queue) != 0):
            temp = queue.popleft()
            spaceLoc = temp[0].index(" ")
            if(temp[0] == endState or temp[0] == "123456789ABCDFE " ):
                depth = temp[1]
                result = [depth, numCreated, numExpanded, maxFringe]
                return result
            
            if((temp[0],temp[2]) not in mySet):
                numExpanded = numExpanded + 1
                mySet.add((temp[0], temp[2]))
                if (validMove(spaceLoc, "right")):
                    queue.append((movePiece(temp[0], spaceLoc, "right"), temp[1] + 1, temp[0]))
                    numCreated = numCreated + 1                   
                if (validMove(spaceLoc, "down")):
                    queue.append((movePiece(temp[0], spaceLoc, "down"), temp[1] + 1, temp[0]))
                    numCreated = numCreated + 1
                if (validMove(spaceLoc, "left")):
                    queue.append((movePiece(temp[0], spaceLoc, "left"), temp[1] + 1, temp[0]))
                    numCreated = numCreated + 1
                if (validMove(spaceLoc, "up")):
                    queue.append((movePiece(temp[0], spaceLoc, "up"), temp[1] + 1, temp[0]))
                    numCreated = numCreated + 1
                 
                if len(queue) > maxFringe:
                    maxFringe = len(queue)

    if (strategy == "GBFS"):
        errorCount = 0
        hdict = []
        hdict.append(problem)

        while (len(hdict) != 0):

            temp = hdict.pop()
            spaceLoc = temp[0].index(" ")

            if(temp[0] == endState or temp[0] == "123456789ABCDFE " ):
                depth = temp[1]
                result = [depth, numCreated, numExpanded, maxFringe]
                return result

            if((temp[0], temp[2]) not in mySet):
                numExpanded = numExpanded + 1
                mySet.add((temp[0], temp[2]))
                if (validMove(spaceLoc, "right")):
                    moveTemp = movePiece(temp[0], spaceLoc, "right")
                    if (options == "h1"):
                        errorCount = getErrorCount(moveTemp, endState)
                    else:
                        errorCount = getMahhattanDistance(moveTemp, endState)
                    hdict.append((moveTemp, temp[1] + 1, temp[0], errorCount))
                    numCreated = numCreated + 1

                if (validMove(spaceLoc, "down")):
                    moveTemp = movePiece(temp[0], spaceLoc, "down")
                    if (options == "h1"):
                        errorCount = getErrorCount(moveTemp, endState)
                    else:
                        errorCount = getMahhattanDistance(moveTemp, endState)
                    hdict.append((moveTemp, temp[1] + 1, temp[0], errorCount))
                    numCreated = numCreated + 1

                if (validMove(spaceLoc, "left")):
                    moveTemp = movePiece(temp[0], spaceLoc, "left")
                    if (options == "h1"):
                        errorCount = getErrorCount(moveTemp, endState)
                    else:
                        errorCount = getMahhattanDistance(moveTemp, endState)
                    hdict.append((moveTemp, temp[1] + 1, temp[0], errorCount))
                    numCreated = numCreated + 1

                if (validMove(spaceLoc, "up")):
                    moveTemp = movePiece(temp[0], spaceLoc, "up")
                    if (options == "h1"):
                        errorCount = getErrorCount(moveTemp, endState)
                    else:
                        errorCount = getMahhattanDistance(moveTemp, endState)
  
                    hdict.append((moveTemp, temp[1] + 1, temp[0], errorCount))
       
                    numCreated = numCreated + 1  

                if len(hdict) > maxFringe:
                    maxFringe = len(hdict)
                hdict.sort(key=lambda tup: tup[3], reverse=True)

    if (strategy == "AStar"):
        errorCount = 0
        hdict = []
        hdict.append(problem)

        while (len(hdict) != 0):
            temp = hdict.pop()
            spaceLoc = temp[0].index(" ")

            if(temp[0] == endState or temp[0] == "123456789ABCDFE " ):
                depth = temp[1]
                result = [depth, numCreated, numExpanded, maxFringe]
                return result

            if((temp[0], temp[2]) not in mySet):
                #hdict.clear()
                #lowCount = []
                numExpanded = numExpanded + 1
                mySet.add((temp[0], temp[2]))

                if (validMove(spaceLoc, "right")):
                    moveTemp = movePiece(temp[0], spaceLoc, "right")
                    if (options == "h1"):
                        errorCount = getErrorCount(moveTemp, endState)
                        errorCount = errorCount + temp[1]
                    else:
                        errorCount = getMahhattanDistance(moveTemp, endState)
                        errorCount = errorCount + temp[1]
                    hdict.append((moveTemp, temp[1] + 1, temp[0], errorCount))
                    numCreated = numCreated + 1
                   

                if (validMove(spaceLoc, "down")):
                    moveTemp = movePiece(temp[0], spaceLoc, "down")
                    if (options == "h1"):
                        errorCount = getErrorCount(moveTemp, endState)
                        errorCount = errorCount + temp[1]
                    else:
                        errorCount = getMahhattanDistance(moveTemp, endState)
                        errorCount = errorCount + temp[1]
                    hdict.append((moveTemp, temp[1] + 1, temp[0], errorCount))
                    numCreated = numCreated + 1


                if (validMove(spaceLoc, "left")):
                    moveTemp = movePiece(temp[0], spaceLoc, "left")
                    if (options == "h1"):
                        errorCount = getErrorCount(moveTemp, endState)
                        errorCount = errorCount + temp[1]
                    else:
                        errorCount = getMahhattanDistance(moveTemp, endState)
                        errorCount = errorCount + temp[1]
                    hdict.append((moveTemp, temp[1] + 1, temp[0], errorCount))
                    numCreated = numCreated + 1


                if (validMove(spaceLoc, "up")):
                    moveTemp = movePiece(temp[0], spaceLoc, "up")
                    if (options == "h1"):
                        errorCount = getErrorCount(moveTemp, endState)
                        errorCount = errorCount + temp[1]
                    else:
                        errorCount = getMahhattanDistance(moveTemp, endState)
                        errorCount = errorCount + temp[1]
                    hdict.append((moveTemp, temp[1] + 1, temp[0], errorCount))
                    numCreated = numCreated + 1

                if len(hdict) > maxFringe:
                    maxFringe = len(hdict)
                hdict.sort(key=lambda tup: tup[3], reverse=True)

    return result

def getErrorCount(currentState, endState):
    errorCount = 0
    for i in range(len(currentState)):
        if (currentState[i] != endState[i]):
            errorCount = errorCount + 1
    return errorCount

def getMahhattanDistance(currentState, endState):
    totalDistance = 0
    for i in range(len(currentState)):
        if (currentState[i] != endState[i]):
            currentPlace = i
            goalPlace = endState.index(currentState[i])
            if (goalPlace < 4):
                if (currentPlace > 3):
                    while (currentPlace > 3):
                        currentPlace = currentPlace - 4
                        totalDistance = totalDistance + 1
                    if (currentPlace > goalPlace):
                        while (currentPlace > goalPlace):
                            currentPlace = currentPlace - 1
                            totalDistance = totalDistance + 1
                    elif (currentPlace < goalPlace):
                        while (currentPlace < goalPlace):
                            currentPlace = currentPlace + 1
                            totalDistance = totalDistance + 1
                else:
                    if (currentPlace > goalPlace):
                        while (currentPlace > goalPlace):
                            currentPlace = currentPlace - 1
                            totalDistance = totalDistance + 1
                    elif (currentPlace < goalPlace):
                        while (currentPlace < goalPlace):
                            currentPlace = currentPlace + 1
                            totalDistance = totalDistance + 1
            elif (goalPlace < 8):
                if ( currentPlace > 7):
                    while ( currentPlace > 7):
                        currentPlace = currentPlace - 4
                        totalDistance = totalDistance + 1
                    if (currentPlace > goalPlace):
                        while (currentPlace > goalPlace):
                            currentPlace = currentPlace - 1
                            totalDistance = totalDistance + 1
                    elif (currentPlace < goalPlace):
                        while (currentPlace < goalPlace):
                            currentPlace = currentPlace + 1
                            totalDistance = totalDistance + 1
                elif ( currentPlace < 4):
                    currentPlace = currentPlace + 4
                    totalDistance = totalDistance + 1
                    if (currentPlace > goalPlace):
                        while (currentPlace > goalPlace):
                            currentPlace = currentPlace - 1
                            totalDistance = totalDistance + 1
                    elif (currentPlace < goalPlace):
                        while (currentPlace < goalPlace):
                            currentPlace = currentPlace + 1
                            totalDistance = totalDistance + 1
                else:
                    if (currentPlace > goalPlace):
                        while (currentPlace > goalPlace):
                            currentPlace = currentPlace - 1
                            totalDistance = totalDistance + 1
                    elif (currentPlace < goalPlace):
                        while (currentPlace < goalPlace):
                            currentPlace = currentPlace + 1
                            totalDistance = totalDistance + 1
            elif (goalPlace < 12):
                if ( currentPlace > 11):
                    while (currentPlace > 11):
                        currentPlace = currentPlace - 4
                        totalDistance = totalDistance + 1
                    if (currentPlace > goalPlace):
                        while (currentPlace > goalPlace):
                            currentPlace = currentPlace - 1
                            totalDistance = totalDistance + 1
                    elif (currentPlace < goalPlace):
                        while (currentPlace < goalPlace):
                            currentPlace = currentPlace + 1
                            totalDistance = totalDistance + 1
                elif (currentPlace < 8):
                    while (currentPlace < 8):
                        currentPlace = currentPlace + 4
                        totalDistance = totalDistance + 1
                    if (currentPlace > goalPlace):
                        while (currentPlace > goalPlace):
                            currentPlace = currentPlace - 1
                            totalDistance = totalDistance + 1
                    elif (currentPlace < goalPlace):
                        while (currentPlace < goalPlace):
                            currentPlace = currentPlace + 1
                            totalDistance = totalDistance + 1
                else:
                    if (currentPlace > goalPlace):
                        while (currentPlace > goalPlace):
                            currentPlace = currentPlace - 1
                            totalDistance = totalDistance + 1
                    elif (currentPlace < goalPlace):
                        while (currentPlace < goalPlace):
                            currentPlace = currentPlace + 1
                            totalDistance = totalDistance + 1
            else:
                if (currentPlace < 12):
                    while(currentPlace < 12):
                        currentPlace = currentPlace + 4
                        totalDistance = totalDistance + 1
                    if (currentPlace > goalPlace):
                        while (currentPlace > goalPlace):
                            currentPlace = currentPlace - 1
                            totalDistance = totalDistance + 1
                    elif (currentPlace < goalPlace):
                        while (currentPlace < goalPlace):
                            currentPlace = currentPlace + 1
                            totalDistance = totalDistance + 1
                else:
                    if (currentPlace > goalPlace):
                        while (currentPlace > goalPlace):
                            currentPlace = currentPlace - 1
                            totalDistance = totalDistance + 1
                    elif (currentPlace < goalPlace):
                        while (currentPlace < goalPlace):
                            currentPlace = currentPlace + 1
                            totalDistance = totalDistance + 1
    return totalDistance




def movePiece(state, spaceLoc , dir):
    newState = state

    if dir == "left":
        temp = newState[spaceLoc - 1]
        newState = newState.replace(newState[spaceLoc], temp )
        newState = newState.replace(newState[spaceLoc - 1]," ", 1)
        
    if dir == "right":
        temp = newState[spaceLoc + 1]
        newState = newState.replace(newState[spaceLoc + 1],newState[spaceLoc])
        newState = newState.replace(newState[spaceLoc], temp, 1)
    if dir == "up":
        temp = newState[spaceLoc - 4]
        newState = newState.replace(newState[spaceLoc], temp)
        newState = newState.replace(newState[spaceLoc - 4]," ", 1)
    if dir == "down":
        temp = newState[spaceLoc + 4]
        newState = newState.replace(newState[spaceLoc + 4],newState[spaceLoc])
        newState = newState.replace(newState[spaceLoc], temp, 1)

    return newState

def validMove(spaceLoc, dir):
    move = False
    if dir == "left":
        if (spaceLoc % 4 == 0):
            move = False
        else:
            move = True 
    elif dir == "right":
        if (spaceLoc % 4 == 3):
            move = False
        else:
            move = True
    elif dir == "up":
        if (spaceLoc < 4):
            move = False
        else:
            move = True
    elif dir == "down":
        if (spaceLoc > 11):
            move = False
        else:
            move = True

    return move


gameStats = treeSearch(root, searchMethod, endState, options)
print(gameStats)
'''
F = open("Readme.txt", "w")


initialState = "123456789ABC DFE"
searchMethod = "BFS"
options = ""
root = (initialState, 0, "")
gameStats = treeSearch(root, searchMethod, endState, options)
F.write(initialState + " " + searchMethod + " " + options + "\n")
F.write(','.join(str(e) for e in gameStats))
F.write("\n")

initialState = "123456789AB CDFE"
searchMethod = "BFS"
options = ""
root = (initialState, 0, "")
gameStats = treeSearch(root, searchMethod, endState, options)
F.write(initialState + " " + searchMethod + " " + options + "\n")
F.write(','.join(str(e) for e in gameStats))
F.write("\n")


initialState = "123456789ABC DFE"
searchMethod = "DFS"
options = ""
root = (initialState, 0, "")
gameStats = treeSearch(root, searchMethod, endState, options)
F.write(initialState + " " + searchMethod + " " + options + "\n")
F.write(','.join(str(e) for e in gameStats))
F.write("\n")

initialState = "123456789AB CDFE"
searchMethod = "DFS"
options = ""
root = (initialState, 0, "")
gameStats = treeSearch(root, searchMethod, endState, options)
F.write(initialState + " " + searchMethod + " " + options + "\n")
F.write(','.join(str(e) for e in gameStats))
F.write("\n")


initialState = "123456789ABC DFE"
searchMethod = "DLS"
options = "3"
root = (initialState, 0, "")
gameStats = treeSearch(root, searchMethod, endState, options)
F.write(initialState + " " + searchMethod + " " + options + "\n")
F.write(','.join(str(e) for e in gameStats))
F.write("\n")

initialState = "123456789AB CDFE"
searchMethod = "DLS"
options = "3"
root = (initialState, 0, "")
gameStats = treeSearch(root, searchMethod, endState, options)
F.write(initialState + " " + searchMethod + " " + options + "\n")
F.write(','.join(str(e) for e in gameStats))
F.write("\n")

initialState = "123456789ABC DFE"
searchMethod = "GBFS"
options = "h1"
root = (initialState, 0, "")
gameStats = treeSearch(root, searchMethod, endState, options)
F.write(initialState + " " + searchMethod + " " + options + "\n")
F.write(','.join(str(e) for e in gameStats))
F.write("\n")


initialState = "123456789AB CDFE"
searchMethod = "GBFS"
options = "h1"
root = (initialState, 0, "")
gameStats = treeSearch(root, searchMethod, endState, options)
F.write(initialState + " " + searchMethod + " " + options + "\n")
F.write(','.join(str(e) for e in gameStats))
F.write("\n")

initialState = "123456789ABC DFE"
searchMethod = "GBFS"
options = "h2"
root = (initialState, 0, "")
gameStats = treeSearch(root, searchMethod, endState, options)
F.write(initialState + " " + searchMethod + " " + options + "\n")
F.write(','.join(str(e) for e in gameStats))
F.write("\n")

initialState = "123456789AB CDFE"
searchMethod = "GBFS"
options = "h2"
root = (initialState, 0, "")
gameStats = treeSearch(root, searchMethod, endState, options)
F.write(initialState + " " + searchMethod + " " + options + "\n")
F.write(','.join(str(e) for e in gameStats))
F.write("\n")


initialState = "123456789ABC DFE"
searchMethod = "AStar"
options = "h1"
root = (initialState, 0, "")
gameStats = treeSearch(root, searchMethod, endState, options)
F.write(initialState + " " + searchMethod + " " + options + "\n")
F.write(','.join(str(e) for e in gameStats))
F.write("\n")


initialState = "123456789AB CDFE"
searchMethod = "AStar"
options = "h1"
root = (initialState, 0, "")
gameStats = treeSearch(root, searchMethod, endState, options)
F.write(initialState + " " + searchMethod + " " + options + "\n")
F.write(','.join(str(e) for e in gameStats))
F.write("\n")

initialState = "123456789ABC DFE"
searchMethod = "AStar"
options = "h2"
root = (initialState, 0, "")
gameStats = treeSearch(root, searchMethod, endState, options)
F.write(initialState + " " + searchMethod + " " + options + "\n")
F.write(','.join(str(e) for e in gameStats))
F.write("\n")

initialState = "123456789AB CDFE"
searchMethod = "AStar"
options = "h2"
root = (initialState, 0, "")
gameStats = treeSearch(root, searchMethod, endState, options)
F.write(initialState + " " + searchMethod + " " + options + "\n")
F.write(','.join(str(e) for e in gameStats))
F.write("\n")



F.close()
'''
