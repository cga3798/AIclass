import os

alphaNodes = [0]
nodes = [0]
def column(matrix, i):
    return [row[i] for row in matrix]

def checkWin(board, piece):
    didWin = False
    gamePieces = []
    for i in range(6):
        temp = ""
        for j in range(6):
            temp = temp + board[i][j]
        gamePieces.append(temp)
        tempColumn = column(board, i)

        temp = ""
        for k in range(6):
            temp = temp + tempColumn[k]

        gamePieces.append(temp)
    temp = "" + board[0][0] + board[1][1] + board[2][2] + board[3][3] + board[4][4] + board[5][5]
    gamePieces.append(temp)
    temp = "" + board[5][0] + board[4][1] + board[3][2] + board[2][3] + board[1][4] + board[0][5]
    gamePieces.append(temp)
    temp = "" + board[0][4] + board[1][3] + board[2][2] + board[3][1] + board[4][0] 
    gamePieces.append(temp)
    temp = "" + board[5][1] + board[4][2] + board[3][3] + board[2][4] + board[1][5] 
    gamePieces.append(temp)
    temp = "" + board[1][0] + board[2][1] + board[3][2] + board[4][3] + board[5][4] 
    gamePieces.append(temp)
    temp = "" + board[5][0] + board[4][1] + board[3][2] + board[2][3] + board[1][4] 
    gamePieces.append(temp)
    temp = "" + board[0][1] + board[1][2] + board[2][3] + board[3][4] + board[4][5]
    gamePieces.append(temp)

    if (piece == "W"):
        piece = "WWWWW"
    else:
        piece = "BBBBB"
    for x in gamePieces:

        if (piece in x):
            didWin = True     

    return didWin

def validMove(board, square):
    valid = False
    if (square[0] == "1"):
        if (square[2] == "1"):
            if board[0][0] == ".":
                valid = True
        elif (square[2] == "2"):
            if board[0][1] == ".":
                valid = True
        elif (square[2] == "3"):
            if board[0][2] == ".":
                valid = True
        elif (square[2] == "4"):
            if board[1][0] == ".":
                valid = True
        elif (square[2] == "5"):
            if board[1][1] == ".":
                valid = True
        elif (square[2] == "6"):
            if board[1][2] == ".":
                valid = True
        elif (square[2] == "7"):
            if board[2][0] == ".":
                valid = True
        elif (square[2] == "8"):
            if board[2][1] == ".":
                valid = True
        else:
            if board[2][2] == ".":
                valid = True
    elif (square[0] == "2"):
        if (square[2] == "1"):
            if board[0][3] == ".":
                valid = True
        elif (square[2] == "2"):
            if board[0][4] == ".":
                valid = True
        elif (square[2] == "3"):
            if board[0][5] == ".":
                valid = True
        elif (square[2] == "4"):
            if board[1][3] == ".":
                valid = True
        elif (square[2] == "5"):
            if board[1][4] == ".":
                valid = True
        elif (square[2] == "6"):
            if board[1][5] == ".":
                valid = True
        elif (square[2] == "7"):
            if board[2][3] == ".":
                valid = True
        elif (square[2] == "8"):
            if board[2][4] == ".":
                valid = True
        else:
            if board[2][5] == ".":
                valid = True

    elif (square[0] == "3"):
        if (square[2] == "1"):
            if board[3][0] == ".":
                valid = True
        elif (square[2] == "2"):
            if board[3][1] == ".":
                valid = True
        elif (square[2] == "3"):
            if board[3][2] == ".":
                valid = True
        elif (square[2] == "4"):
            if board[4][0] == ".":
                valid = True
        elif (square[2] == "5"):
            if board[4][1] == ".":
                valid = True
        elif (square[2] == "6"):
            if board[4][2] == ".":
                valid = True
        elif (square[2] == "7"):
            if board[5][0] == ".":
                valid = True
        elif (square[2] == "8"):
            if board[5][1] == ".":
                valid = True
        else:
            if board[5][2] == ".":
                valid = True   
    else:
        if (square[2] == "1"):
            if board[3][3] == ".":
                valid = True
        elif (square[2] == "2"):
            if board[3][4] == ".":
                valid = True
        elif (square[2] == "3"):
            if board[3][5] == ".":
                valid = True
        elif (square[2] == "4"):
            if board[4][3] == ".":
                valid = True
        elif (square[2] == "5"):
            if board[4][4] == ".":
                valid = True
        elif (square[2] == "6"):
            if board[4][5] == ".":
                valid = True
        elif (square[2] == "7"):
            if board[5][3] == ".":
                valid = True
        elif (square[2] == "8"):
            if board[5][4] == ".":
                valid = True
        else:
            if board[5][5] == ".":
                valid = True
    return valid

def movePiece(board, square, piece):
    clone = [['.' for x in range(6)] for y in range(6)]
    for i in range(6):
        for k in range(6):
            clone[i][k] = board[i][k]
    if (square[0] == "1"):
        if (square[2] == "1"):
            clone[0][0] = piece
        elif (square[2] == "2"):
            clone[0][1] = piece
        elif (square[2] == "3"):
            clone[0][2] = piece
        elif (square[2] == "4"):
            clone[1][0] = piece
        elif (square[2] == "5"):
            clone[1][1] = piece
        elif (square[2] == "6"):
            clone[1][2] = piece
        elif (square[2] == "7"):
            clone[2][0] = piece
        elif (square[2] == "8"):
            clone[2][1] = piece
        else:
            clone[2][2] = piece
    elif (square[0] == "2"):
        if (square[2] == "1"):
            clone[0][3] = piece
        elif (square[2] == "2"):
            clone[0][4] = piece
        elif (square[2] == "3"):
            clone[0][5] = piece
        elif (square[2] == "4"):
            clone[1][3] = piece
        elif (square[2] == "5"):
            clone[1][4] = piece
        elif (square[2] == "6"):
            clone[1][5] = piece
        elif (square[2] == "7"):
            clone[2][3] = piece
        elif (square[2] == "8"):
            clone[2][4] = piece
        else:
            clone[2][5] = piece

    elif (square[0] == "3"):
        if (square[2] == "1"):
            clone[3][0] = piece
        elif (square[2] == "2"):
            clone[3][1] = piece
        elif (square[2] == "3"):
            clone[3][2] = piece
        elif (square[2] == "4"):
            clone[4][0] = piece
        elif (square[2] == "5"):
            clone[4][1] = piece
        elif (square[2] == "6"):
            clone[4][2] = piece
        elif (square[2] == "7"):
            clone[5][0] = piece
        elif (square[2] == "8"):
            clone[5][1] = piece
        else:
            clone[5][2] = piece
        
    else:
        if (square[2] == "1"):
            clone[3][3] = piece
        elif (square[2] == "2"):
            clone[3][4] = piece
        elif (square[2] == "3"):
            clone[3][5] = piece
        elif (square[2] == "4"):
            clone[4][3] = piece
        elif (square[2] == "5"):
            clone[4][4] = piece
        elif (square[2] == "6"):
            clone[4][5] = piece
        elif (square[2] == "7"):
            clone[5][3] = piece
        elif (square[2] == "8"):
            clone[5][4] = piece
        else:
            clone[5][5] = piece
    return clone

def turnBoard(board, dir, box):
    clone = [['.' for x in range(6)] for y in range(6)]
    for i in range(6):
        for k in range(6):
            clone[i][k] = board[i][k]
    if (dir == "R"):
   
        firstPiece = '.'
        secondPiece = '.'

        if (box == "1"):
            if (clone[0][0] != '.'):
                firstPiece = clone[0][0]
            else:
                firstPiece = '.'
            if (clone[0][2] != '.'):
                secondPiece = clone[0][2]
                clone[0][2] = firstPiece
            else:
                clone[0][2] = firstPiece
                secondPiece = '.'
            if (clone[2][2] != '.'):
                firstPiece = clone[2][2]
                clone[2][2] = secondPiece
            else:
                clone[2][2] = secondPiece
                firstPiece = '.'
            if (clone[2][0] != '.'):
                secondPiece = clone[2][0]
                clone[2][0] = firstPiece
            else:
                clone[2][0] = firstPiece
                secondPiece = '.'
            clone[0][0] = secondPiece
            firstPiece = '.'
            secondPiece = '.'
            if (clone[0][1] != '.'):
                firstPiece = clone[0][1]
            else:
                firstPiece = '.'
            if (clone[1][2] != '.'):
                secondPiece = clone[1][2]
                clone[1][2] = firstPiece
            else:
                clone[1][2] = firstPiece
                secondPiece = '.'
            if (clone[2][1] != '.'):
                firstPiece = clone[2][1]
                clone[2][1] = secondPiece
            else:
                clone[2][1] = secondPiece
                firstPiece = '.'
            if (clone[1][0] != '.'):
                secondPiece = clone[1][0]
                clone[1][0] = firstPiece
            else:
                clone[1][0] = firstPiece
                secondPiece = '.'
            clone[0][1] = secondPiece


        elif (box == "2"):
       
            firstPiece = '.'
            secondPiece = '.'

            if (clone[0][3] != '.'):
                firstPiece = clone[0][3]
            else:
                firstPiece = '.'
            if (clone[0][5] != '.'):
                secondPiece = clone[0][5]
                clone[0][5] = firstPiece
            else:
                clone[0][5] = firstPiece
                secondPiece = '.'
            if (clone[2][5] != '.'):
                firstPiece = clone[2][5]
                clone[2][5] = secondPiece
            else:
                clone[2][5] = secondPiece
                firstPiece = '.'
            if (clone[2][3] != '.'):
                secondPiece = clone[2][3]
                clone[2][3] = firstPiece
            else:
                clone[2][3] = firstPiece
                secondPiece = '.'
            clone[0][3] = secondPiece
            firstPiece = '.'
            secondPiece = '.'
            if (clone[0][4] != '.'):
                firstPiece = clone[0][4]
            else:
                firstPiece = '.'
            if (clone[1][5] != '.'):
                secondPiece = clone[1][5]
                clone[1][5] = firstPiece
            else:
                clone[1][5] = firstPiece
                secondPiece = '.'
            if (clone[2][4] != '.'):
                firstPiece = clone[2][4]
                clone[2][4] = secondPiece
            else:
                clone[2][4] = secondPiece
                firstPiece = '.'
            if (clone[1][3] != '.'):
                secondPiece = clone[1][3]
                clone[1][3] = firstPiece
            else:
                clone[1][3] = firstPiece
                secondPiece = '.'
            clone[0][4] = secondPiece
      
        elif (box == "3"):
            firstPiece = '.'
            secondPiece = '.'

            if (clone[3][0] != '.'):
                firstPiece = clone[3][0]
            else:
                firstPiece = '.'
            if (clone[3][2] != '.'):
                secondPiece = clone[3][2]
                clone[3][2] = firstPiece
            else:
                clone[3][2] = firstPiece
                secondPiece = '.'
            if (clone[5][2] != '.'):
                firstPiece = clone[5][2]
                clone[5][2] = secondPiece
            else:
                clone[5][2] = secondPiece
                firstPiece = '.'
            if (clone[5][0] != '.'):
                secondPiece = clone[5][0]
                clone[5][0] = firstPiece
            else:
                clone[5][0] = firstPiece
                secondPiece = '.'
            clone[3][0] = secondPiece
            firstPiece = '.'
            secondPiece = '.'
            if (clone[3][1] != '.'):
                firstPiece = clone[3][1]
            else:
                firstPiece = '.'
            if (clone[4][2] != '.'):
                secondPiece = clone[4][2]
                clone[4][2] = firstPiece
            else:
                clone[4][2] = firstPiece
                secondPiece = '.'
            if (clone[5][1] != '.'):
                firstPiece = clone[5][1]
                clone[5][1] = secondPiece
            else:
                clone[5][1] = secondPiece
                firstPiece = '.'
            if (clone[4][0] != '.'):
                secondPiece = clone[4][0]
                clone[4][0] = firstPiece
            else:
                clone[4][0] = firstPiece
                secondPiece = '.'
            clone[3][1] = secondPiece
        else:
            firstPiece = '.'
            secondPiece = '.'

            if (clone[3][3] != '.'):
                firstPiece = clone[3][3]
            else:
                firstPiece = '.'
            if (clone[3][5] != '.'):
                secondPiece = clone[3][5]
                clone[3][5] = firstPiece
            else:
                clone[3][5] = firstPiece
                secondPiece = '.'
            if (clone[5][5] != '.'):
                firstPiece = clone[5][5]
                clone[5][5] = secondPiece
            else:
                clone[5][5] = secondPiece
                firstPiece = '.'
            if (clone[5][3] != '.'):
                secondPiece = clone[5][3]
                clone[5][3] = firstPiece
            else:
                clone[5][3] = firstPiece
                secondPiece = '.'
            clone[3][3] = secondPiece
            firstPiece = '.'
            secondPiece = '.'
            if (clone[3][4] != '.'):
                firstPiece = clone[3][4]
            else:
                firstPiece = '.'
            if (clone[4][5] != '.'):
                secondPiece = clone[4][5]
                clone[4][5] = firstPiece
            else:
                clone[4][5] = firstPiece
                secondPiece = '.'
            if (clone[5][4] != '.'):
                firstPiece = clone[5][4]
                clone[5][4] = secondPiece
            else:
                clone[5][4] = secondPiece
                firstPiece = '.'
            if (clone[4][3] != '.'):
                secondPiece = clone[4][3]
                clone[4][3] = firstPiece
            else:
                clone[4][3] = firstPiece
                secondPiece = '.'
            clone[3][4] = secondPiece
    elif (dir == "L"):
        firstPiece = '.'
        secondPiece = '.'

        if (box == "1"):
            if (clone[0][0] != '.'):
                firstPiece = clone[0][0]
            else:
                firstPiece = '.'
            if (clone[2][0] != '.'):
                secondPiece = clone[2][0]
                clone[2][0] = firstPiece
            else:
                clone[2][0] = firstPiece
                secondPiece = '.'
            if (clone[2][2] != '.'):
                firstPiece = clone[2][2]
                clone[2][2] = secondPiece
            else:
                clone[2][2] = secondPiece
                firstPiece = '.'
            if (clone[0][2] != '.'):
                secondPiece = clone[0][2]
                clone[0][2] = firstPiece
            else:
                clone[0][2] = firstPiece
                secondPiece = '.'
            clone[0][0] = secondPiece
            firstPiece = '.'
            secondPiece = '.'
            if (clone[0][1] != '.'):
                firstPiece = clone[0][1]
            else:
                firstPiece = '.'
            if (clone[1][0] != '.'):
                secondPiece = clone[1][0]
                clone[1][0] = firstPiece
            else:
                clone[1][0] = firstPiece
                secondPiece = '.'
            if (clone[2][1] != '.'):
                firstPiece = clone[2][1]
                clone[2][1] = secondPiece
            else:
                clone[2][1] = secondPiece
                firstPiece = '.'
            if (clone[1][2] != '.'):
                secondPiece = clone[1][2]
                clone[1][2] = firstPiece
            else:
                clone[1][2] = firstPiece
                secondPiece = '.'
            clone[0][1] = secondPiece


        elif (box == "2"):
       
            firstPiece = '.'
            secondPiece = '.'

            if (clone[0][3] != '.'):
                firstPiece = clone[0][3]
            else:
                firstPiece = '.'
            if (clone[2][3] != '.'):
                secondPiece = clone[2][3]
                clone[2][3] = firstPiece
            else:
                clone[2][3] = firstPiece
                secondPiece = '.'
            if (clone[2][5] != '.'):
                firstPiece = clone[2][5]
                clone[2][5] = secondPiece
            else:
                clone[2][5] = secondPiece
                firstPiece = '.'
            if (clone[0][5] != '.'):
                secondPiece = clone[0][5]
                clone[0][5] = firstPiece
            else:
                clone[0][5] = firstPiece
                secondPiece = '.'
            clone[0][3] = secondPiece
            firstPiece = '.'
            secondPiece = '.'
            if (clone[0][4] != '.'):
                firstPiece = clone[0][4]
            else:
                firstPiece = '.'
            if (clone[1][3] != '.'):
                secondPiece = clone[1][3]
                clone[1][3] = firstPiece
            else:
                clone[1][3] = firstPiece
                secondPiece = '.'
            if (clone[2][4] != '.'):
                firstPiece = clone[2][4]
                clone[2][4] = secondPiece
            else:
                clone[2][4] = secondPiece
                firstPiece = '.'
            if (clone[1][5] != '.'):
                secondPiece = clone[1][5]
                clone[1][5] = firstPiece
            else:
                clone[1][5] = firstPiece
                secondPiece = '.'
            clone[0][4] = secondPiece
      
        elif (box == "3"):
            firstPiece = '.'
            secondPiece = '.'

            if (clone[3][0] != '.'):
                firstPiece = clone[3][0]
            else:
                firstPiece = '.'
            if (clone[5][0] != '.'):
                secondPiece = clone[5][0]
                clone[5][0] = firstPiece
            else:
                clone[5][0] = firstPiece
                secondPiece = '.'
            if (clone[5][2] != '.'):
                firstPiece = clone[5][2]
                clone[5][2] = secondPiece
            else:
                clone[5][2] = secondPiece
                firstPiece = '.'
            if (clone[3][2] != '.'):
                secondPiece = clone[3][2]
                clone[3][2] = firstPiece
            else:
                clone[3][2] = firstPiece
                secondPiece = '.'
            clone[3][0] = secondPiece
            firstPiece = '.'
            secondPiece = '.'
            if (clone[3][1] != '.'):
                firstPiece = clone[3][1]
            else:
                firstPiece = '.'
            if (clone[4][0] != '.'):
                secondPiece = clone[4][0]
                clone[4][0] = firstPiece
            else:
                clone[4][0] = firstPiece
                secondPiece = '.'
            if (clone[5][1] != '.'):
                firstPiece = clone[5][1]
                clone[5][1] = secondPiece
            else:
                clone[5][1] = secondPiece
                firstPiece = '.'
            if (clone[4][2] != '.'):
                secondPiece = clone[4][2]
                clone[4][2] = firstPiece
            else:
                clone[4][2] = firstPiece
                secondPiece = '.'
            clone[3][1] = secondPiece
        else:
            firstPiece = '.'
            secondPiece = '.'

            if (clone[3][3] != '.'):
                firstPiece = clone[3][3]
            else:
                firstPiece = '.'
            if (clone[5][3] != '.'):
                secondPiece = clone[5][3]
                clone[5][3] = firstPiece
            else:
                clone[5][3] = firstPiece
                secondPiece = '.'
            if (clone[5][5] != '.'):
                firstPiece = clone[5][5]
                clone[5][5] = secondPiece
            else:
                clone[5][5] = secondPiece
                firstPiece = '.'
            if (clone[3][5] != '.'):
                secondPiece = clone[3][5]
                clone[3][5] = firstPiece
            else:
                clone[3][5] = firstPiece
                secondPiece = '.'
            clone[3][3] = secondPiece
            firstPiece = '.'
            secondPiece = '.'
            if (clone[3][4] != '.'):
                firstPiece = clone[3][4]
            else:
                firstPiece = '.'
            if (clone[4][3] != '.'):
                secondPiece = clone[4][3]
                clone[4][3] = firstPiece
            else:
                clone[4][3] = firstPiece
                secondPiece = '.'
            if (clone[5][4] != '.'):
                firstPiece = clone[5][4]
                clone[5][4] = secondPiece
            else:
                clone[5][4] = secondPiece
                firstPiece = '.'
            if (clone[4][5] != '.'):
                secondPiece = clone[4][5]
                clone[4][5] = firstPiece
            else:
                clone[4][5] = firstPiece
                secondPiece = '.'
            clone[3][4] = secondPiece
            
    return clone




def heuristicScore(board, piece):
    score = 0
    gamePieces = []
    for i in range(6):
        temp = ""
        for j in range(6):
            temp = temp + board[i][j]
        gamePieces.append(temp)
        tempColumn = column(board, i)

        temp = ""
        for k in range(6):
            temp = temp + tempColumn[k]

        gamePieces.append(temp)
    temp = "" + board[0][0] + board[1][1] + board[2][2] + board[3][3] + board[4][4] + board[5][5]
    gamePieces.append(temp)
    temp = "" + board[5][0] + board[4][1] + board[3][2] + board[2][3] + board[1][4] + board[0][5]
    gamePieces.append(temp)
    temp = "" + board[0][4] + board[1][3] + board[2][2] + board[3][1] + board[4][0] 
    gamePieces.append(temp)
    temp = "" + board[5][1] + board[4][2] + board[3][3] + board[2][4] + board[1][5] 
    gamePieces.append(temp)
    temp = "" + board[1][0] + board[2][1] + board[3][2] + board[4][3] + board[5][4] 
    gamePieces.append(temp)
    temp = "" + board[5][0] + board[4][1] + board[3][2] + board[2][3] + board[1][4] 
    gamePieces.append(temp)
    temp = "" + board[0][1] + board[1][2] + board[2][3] + board[3][4] + board[4][5]
    gamePieces.append(temp)

    for x in gamePieces:
        tempCount = 0
        threeIn = 0
        for letter in x:
            if (threeIn >= 3):
                score += 10

            if (letter == piece):
                threeIn = threeIn + 1
            else:
                threeIn = 0
            if (letter == piece or letter == "."):
                tempCount = tempCount + 1
            else:
                tempCount = 0
            if tempCount == 5:
                
                score = score + 1
            if tempCount == 6:
                score = score + 1    
    return score

def utility(state, piece):
    if (piece == "W"):
        score = heuristicScore(state, "W") - heuristicScore(state, "B")
    else:
        score = heuristicScore(state, "B") - heuristicScore(state, "W")
    if(checkWin(state, "W") and checkWin(state, "B")):
        score = "tie"
    elif (checkWin(state, "w")):
        score = 100
    elif (checkWin(state, "B")):
        score = -100
    #elif(score == 0):
        #score = heuristicScore(state, piece)
    return score

def successors(state, piece):
    possibleMoves = []
    possibleFlips = [("1","R"),("1","L"),("2","R"),("2","L"),("3","R"),("3","L"),("4","R"),("4","L")]
    for i in range(4):
        for k in range(9):
            move = "" + str(i + 1) + "/" + str(k + 1)
            if (validMove(state, move)):
                newState = movePiece(state, move, piece)
                for flip in possibleFlips:
                    clone = turnBoard(newState,flip[1], flip[0])
                    possibleMoves.append((clone, i + 1, k + 1, flip[1], flip[0]))
                    
    return possibleMoves


def MaxValue(state, piece, depth, nodes, limit):
    moveList = []
    nodes[0] = nodes[0] + 1
    if (checkWin(state, "W") or checkWin(state, "B") or depth >= limit):
        return utility(state, piece)
    moves = successors(state, piece)
    if (len(moves) == 0 ):
        return utility(state, piece)
    best_score = float('-inf')
    for move in moves:
        best_score = max(best_score, minValue(move[0],piece,depth + 1, nodes, limit))
        if (depth == 0):
            moveList.append((move, best_score))
    return (best_score, moveList)

def minValue(state, piece, depth, nodes, limit):
    nodes[0] = nodes[0] + 1
    if (checkWin(state, "W") or checkWin(state, "B") or depth >= limit):
        return utility(state, piece)
    moves = successors(state, piece)
    if (len(moves) == 0 ):
        return utility(state, piece)
    best_score = float('inf')
    for move in moves:
        best_score = min(best_score, MaxValue(move[0],piece, depth + 1, nodes, limit))
    return best_score

def miniMaxDecision(state, piece, nodes, limit):
    v = MaxValue(state, piece, 0, nodes, limit)
    moveList = v[1]
    for move in moveList:     
        if v[0] == move[1]:
            return move[0]


def alphaMaxValue(state, piece, depth, alpha, beta, nodes, limit):
    moveList = []
    alphaNodes[0] = alphaNodes[0] + 1
    if (checkWin(state, "W") or checkWin(state, "B") or depth >= limit):
        return utility(state, piece)
    moves = successors(state, piece)
    if (len(moves) == 0 ):
        return utility(state, piece)
    best_score = float('-inf')
    for move in moves:
        if (alpha < beta):
            best_score = max(best_score, alphaMinValue(move[0],piece,depth + 1, alpha, best_score, nodes, limit))
        if (depth == 0):
            moveList.append((move, best_score))
    return (best_score, moveList)

def alphaMinValue(state, piece, depth, alpha, beta, nodes, limit):
    alphaNodes[0] = alphaNodes[0] + 1
    if (checkWin(state, "W") or checkWin(state, "B") or depth >= limit):
        return utility(state, piece)
    moves = successors(state, piece)
    if (len(moves) == 0 ):
        return utility(state, piece)
    best_score = float('inf')
    for move in moves:
        if (alpha < beta):
            best_score = min(best_score, alphaMaxValue(move[0],piece, depth + 1, best_score, beta, nodes, limit))
    return best_score

def alphaMiniMaxDecision(state, piece, nodes, limit):
    v = alphaMaxValue(state, piece, 0, float('-inf'), float('inf'), nodes, limit)
    moveList = v[1]
    for move in moveList:     
        if v[0] == move[1]:
            return move[0]
    
def noMoreSpaces(state):
    gameOver = True
    for square in state:
        if square == ".":
            gameOver = False   
    return gameOver

def printBoard(board):
    print("----------------------------")
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
        for row in board]))
    print("----------------------------") 

def filePrintBoard(board, fle):
    fle.write("----------------------------\n")
    fle.write('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
        for row in board]))
    fle.write("\n----------------------------\n")


player1Win = False
player2Win = False
player1Win = False
player2Win = False

player1 = input("Enter name of player: ")
player2 = "AI"
player1Color = input(player1 +" please pick Token Color (B or W): ")
player1Color = player1Color.upper()
if (player1Color == "W"):
    player2Color = "B"
else:
    player2Color = "W"
choice = input("Player to Move First (player or AI): ")
choice = choice.upper()
gameBoard = [['.' for x in range(6)] for y in range(6)]
if (choice == "AI"):
    player2 = player1
    player1 = "AI"
    temp = player1Color
    player1Color = player2Color
    player2Color = temp
f = open("Output.txt", "w")
test = False

f.write("player1 - " = player1 + " Piece - " + player1Color + "\n")
f.write("player2 - " = player2 + " Piece - " + player2Color + "\n")
printBoard(gameBoard)
filePrintBoard(gameBoard, f)
while (not test):
    if(player1 == "AI"):
        player1Move = alphaMiniMaxDecision(gameBoard, player1Color, nodes, 2)
        print(player1 + " Enter Move: "  + str(player1Move[1]) + "/" + str(player1Move[2]) + " " + str(player1Move[4]) + player1Move[3])
        f.write(player1 + " Enter Move: "  + str(player1Move[1]) + "/" + str(player1Move[2]) + " " + str(player1Move[4]) + player1Move[3] + "\n")
        square = str(player1Move[1]) + "/" + str(player1Move[2])
        gameBoard = movePiece(gameBoard, square, player1Color)
        
        printBoard(gameBoard)
        filePrintBoard(gameBoard, f)

        print("Move: " + square)
        f.write("Move: " + square + "\n")
        if (checkWin(gameBoard, player1Color)):
            player1Win = True
            break
        gameBoard = turnBoard(gameBoard,player1Move[3], player1Move[4])
       
        printBoard(gameBoard)
        filePrintBoard(gameBoard, f)

        print("Turn: " + str(player1Move[4]) +  " " + player1Move[3])
        f.write("Turn: " + str(player1Move[4]) +  " " + player1Move[3]+ "\n")
        if (checkWin(gameBoard, player1Color)):
            player1Win = True
            break
    else:
        player1Move = input(player1 + " Enter Move: ")
        f.write(player1 + " Enter Move: "  + player1Move + "\n")
        player1Move = player1Move.split()
        square = player1Move[0].upper()
        if (not validMove(gameBoard, square)):
            while (not validMove(gameBoard, square)):
                player1Move = input("Move not valid please try again: ")
                player1Move = player1Move.split()
                square = player1Move[0].upper()
        gameBoard = movePiece(gameBoard, square, player1Color)
        
        printBoard(gameBoard)
        filePrintBoard(gameBoard, f)
        
        print("Move: " + square)
        f.write("Move: " + square+ "\n")
        if (checkWin(gameBoard, player1Color)):
            player1Win = True
            break
        gameBoard = turnBoard(gameBoard,player1Move[1][1].upper(), player1Move[1][0])
        
        printBoard(gameBoard)
        filePrintBoard(gameBoard, f)
        
        print("Turn: " + str(player1Move[1][0]) +  " " + player1Move[1][1].upper())
        f.write("Turn: " + str(player1Move[1][0]) +  " " + player1Move[1][1].upper())
        if (checkWin(gameBoard, player1Color)):
            player1Win = True
            break
    if(player2 == "AI"):
        player2Move = alphaMiniMaxDecision(gameBoard, player2Color, nodes, 2)
        print(player2 + " Enter Move: "  + str(player2Move[1]) + "/" + str(player2Move[2])  + " " + str(player2Move[4]) + player2Move[3])
        f.write(player2 + " Enter Move: "  + str(player2Move[1]) + "/" + str(player2Move[2])  + " " + str(player2Move[4]) + player2Move[3]+ "\n")
        square = str(player2Move[1]) + "/" + str(player2Move[2])
        gameBoard = movePiece(gameBoard, square, player2Color)
        
        printBoard(gameBoard)
        filePrintBoard(gameBoard, f)

        print("Move: " + square)
        f.write("Move: " + square)
        if (checkWin(gameBoard, player2Color)):
            player2Win = True
            break
        gameBoard = turnBoard(gameBoard,player2Move[3], player2Move[4])
        
        printBoard(gameBoard)
        filePrintBoard(gameBoard, f)

        print("Turn: " + str(player2Move[4]) +  " " + player2Move[3])
        f.write("Turn: " + str(player2Move[4]) +  " " + player2Move[3]+ "\n")
        if (checkWin(gameBoard, player2Color)):
            player2Win = True
            break
    else:
        player2Move = input(player2 + " Enter Move: ")
        f.write(player2 + " Enter Move: "  + player2Move + "\n")
        player2Move = player2Move.split()
        square = player2Move[0].upper()
        if (not validMove(gameBoard, square)):
            while (not validMove(gameBoard, square)):
                player2Move = input("Move not valid please try again: ")
                player2Move = player2Move.split()
                square = player2Move[0].upper()
        gameBoard = movePiece(gameBoard, square, player2Color)
        
        printBoard(gameBoard)
        filePrintBoard(gameBoard, f)
        
        print("Move: " + square)
        f.write("Move: " + square + "\n")
        if (checkWin(gameBoard, player2Color)):
            player2Win = True
            break
        gameBoard = turnBoard(gameBoard,player2Move[1][1].upper(), player2Move[1][0])
        
        printBoard(gameBoard)
        filePrintBoard(gameBoard, f)
        
        print("Turn: " + str(player2Move[1][0]) +  " " + player2Move[1][1].upper())
        f.write("Turn: " + str(player2Move[1][0]) +  " " + player2Move[1][1].upper()+ "\n")
        if (checkWin(gameBoard, player2Color)):
            player2Win = True
            break
    if not noMoreSpaces(gameBoard):
        player1Win = True
        player2Win = True
        break
player1Win = checkWin(gameBoard, player1Color)
player2Win = checkWin(gameBoard, player2Color)
if(player1Win and player2Win):
    print("Game Tie!")
    f.write("Game Tie!"+ "\n")
elif(player1Win):
    print(player1 + " wins!")
    f.write(player1 + " wins!"+ "\n")
elif(player2Win):
    print(player2 + " wins!")
    f.write(player2 + " wins!"+ "\n")
else:
    print("Game Tie!")
    f.write("Game Tie!"+ "\n")