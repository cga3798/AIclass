import os



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


    for x in gamePieces:

        if (piece in x):
            didWin = True     

    return didWin



def movePiece(board, square, piece):
    if (square[0] == "1"):
        if (square[2] == "1"):
            board[0][0] = piece
        elif (square[2] == "2"):
            board[0][1] = piece
        elif (square[2] == "3"):
            board[0][2] = piece
        elif (square[2] == "4"):
            board[1][0] = piece
        elif (square[2] == "5"):
            board[1][1] = piece
        elif (square[2] == "6"):
            board[1][2] = piece
        elif (square[2] == "7"):
            board[2][0] = piece
        elif (square[2] == "8"):
            board[2][1] = piece
        else:
            board[2][2] = piece
    elif (square[0] == "2"):
        if (square[2] == "1"):
            board[0][3] = piece
        elif (square[2] == "2"):
            board[0][4] = piece
        elif (square[2] == "3"):
            board[0][5] = piece
        elif (square[2] == "4"):
            board[1][3] = piece
        elif (square[2] == "5"):
            board[1][4] = piece
        elif (square[2] == "6"):
            board[1][5] = piece
        elif (square[2] == "7"):
            board[2][3] = piece
        elif (square[2] == "8"):
            board[2][4] = piece
        else:
            board[2][5] = piece

    elif (square[0] == "3"):
        if (square[2] == "1"):
            board[3][0] = piece
        elif (square[2] == "2"):
            board[3][1] = piece
        elif (square[2] == "3"):
            board[3][2] = piece
        elif (square[2] == "4"):
            board[4][0] = piece
        elif (square[2] == "5"):
            board[4][1] = piece
        elif (square[2] == "6"):
            board[4][2] = piece
        elif (square[2] == "7"):
            board[5][0] = piece
        elif (square[2] == "8"):
            board[5][1] = piece
        else:
            board[5][2] = piece
        
    else:
        if (square[2] == "1"):
            board[3][3] = piece
        elif (square[2] == "2"):
            board[3][4] = piece
        elif (square[2] == "3"):
            board[3][5] = piece
        elif (square[2] == "4"):
            board[4][3] = piece
        elif (square[2] == "5"):
            board[4][4] = piece
        elif (square[2] == "6"):
            board[4][5] = piece
        elif (square[2] == "7"):
            board[5][3] = piece
        elif (square[2] == "8"):
            board[5][4] = piece
        else:
            board[5][5] = piece
    return board

def turnBoard(board, dir, box):
    if (dir == "right"):
   
        firstPiece = '.'
        secondPiece = '.'

        if (box == "1"):
            if (board[0][0] != '.'):
                firstPiece = board[0][0]
            else:
                firstPiece = '.'
            if (board[0][2] != '.'):
                secondPiece = board[0][2]
                board[0][2] = firstPiece
            else:
                board[0][2] = firstPiece
                secondPiece = '.'
            if (board[2][2] != '.'):
                firstPiece = board[2][2]
                board[2][2] = secondPiece
            else:
                board[2][2] = secondPiece
                firstPiece = '.'
            if (board[2][0] != '.'):
                secondPiece = board[2][0]
                board[2][0] = firstPiece
            else:
                board[2][0] = firstPiece
                secondPiece = '.'
            board[0][0] = secondPiece
            firstPiece = '.'
            secondPiece = '.'
            if (board[0][1] != '.'):
                firstPiece = board[0][1]
            else:
                firstPiece = '.'
            if (board[1][2] != '.'):
                secondPiece = board[1][2]
                board[1][2] = firstPiece
            else:
                board[1][2] = firstPiece
                secondPiece = '.'
            if (board[2][1] != '.'):
                firstPiece = board[2][1]
                board[2][1] = secondPiece
            else:
                board[2][1] = secondPiece
                firstPiece = '.'
            if (board[1][0] != '.'):
                secondPiece = board[1][0]
                board[1][0] = firstPiece
            else:
                board[1][0] = firstPiece
                secondPiece = '.'
            board[0][1] = secondPiece


        elif (box == "2"):
       
            firstPiece = '.'
            secondPiece = '.'

            if (board[0][3] != '.'):
                firstPiece = board[0][3]
            else:
                firstPiece = '.'
            if (board[0][5] != '.'):
                secondPiece = board[0][5]
                board[0][5] = firstPiece
            else:
                board[0][5] = firstPiece
                secondPiece = '.'
            if (board[2][5] != '.'):
                firstPiece = board[2][5]
                board[2][5] = secondPiece
            else:
                board[2][5] = secondPiece
                firstPiece = '.'
            if (board[2][3] != '.'):
                secondPiece = board[2][3]
                board[2][3] = firstPiece
            else:
                board[2][3] = firstPiece
                secondPiece = '.'
            board[0][3] = secondPiece
            firstPiece = '.'
            secondPiece = '.'
            if (board[0][4] != '.'):
                firstPiece = board[0][4]
            else:
                firstPiece = '.'
            if (board[1][5] != '.'):
                secondPiece = board[1][5]
                board[1][5] = firstPiece
            else:
                board[1][5] = firstPiece
                secondPiece = '.'
            if (board[2][4] != '.'):
                firstPiece = board[2][4]
                board[2][4] = secondPiece
            else:
                board[2][4] = secondPiece
                firstPiece = '.'
            if (board[1][3] != '.'):
                secondPiece = board[1][3]
                board[1][3] = firstPiece
            else:
                board[1][3] = firstPiece
                secondPiece = '.'
            board[0][4] = secondPiece
      
        elif (box == "3"):
            firstPiece = '.'
            secondPiece = '.'

            if (board[3][0] != '.'):
                firstPiece = board[3][0]
            else:
                firstPiece = '.'
            if (board[3][2] != '.'):
                secondPiece = board[3][2]
                board[3][2] = firstPiece
            else:
                board[3][2] = firstPiece
                secondPiece = '.'
            if (board[5][2] != '.'):
                firstPiece = board[5][2]
                board[5][2] = secondPiece
            else:
                board[5][2] = secondPiece
                firstPiece = '.'
            if (board[5][0] != '.'):
                secondPiece = board[5][0]
                board[5][0] = firstPiece
            else:
                board[5][0] = firstPiece
                secondPiece = '.'
            board[3][0] = secondPiece
            firstPiece = '.'
            secondPiece = '.'
            if (board[3][1] != '.'):
                firstPiece = board[3][1]
            else:
                firstPiece = '.'
            if (board[4][2] != '.'):
                secondPiece = board[4][2]
                board[4][2] = firstPiece
            else:
                board[4][2] = firstPiece
                secondPiece = '.'
            if (board[5][1] != '.'):
                firstPiece = board[5][1]
                board[5][1] = secondPiece
            else:
                board[5][1] = secondPiece
                firstPiece = '.'
            if (board[4][0] != '.'):
                secondPiece = board[4][0]
                board[4][0] = firstPiece
            else:
                board[4][0] = firstPiece
                secondPiece = '.'
            board[3][1] = secondPiece
        else:
            firstPiece = '.'
            secondPiece = '.'

            if (board[3][3] != '.'):
                firstPiece = board[3][3]
            else:
                firstPiece = '.'
            if (board[3][5] != '.'):
                secondPiece = board[3][5]
                board[3][5] = firstPiece
            else:
                board[3][5] = firstPiece
                secondPiece = '.'
            if (board[5][5] != '.'):
                firstPiece = board[5][5]
                board[5][5] = secondPiece
            else:
                board[5][5] = secondPiece
                firstPiece = '.'
            if (board[5][3] != '.'):
                secondiece = board[5][3]
                board[5][3] = firstPiece
            else:
                board[5][3] = firstPiece
                secondPiece = '.'
            board[3][3] = secondPiece
            firstPiece = '.'
            secondPiece = '.'
            if (board[3][4] != '.'):
                firstPiece = board[3][4]
            else:
                firstPiece = '.'
            if (board[4][5] != '.'):
                secondPiece = board[4][5]
                board[4][5] = firstPiece
            else:
                board[4][5] = firstPiece
                secondPiece = '.'
            if (board[5][4] != '.'):
                firstPiece = board[5][4]
                board[5][4] = secondPiece
            else:
                board[5][4] = secondPiece
                firstPiece = '.'
            if (board[4][3] != '.'):
                secondPiece = board[4][3]
                board[4][3] = firstPiece
            else:
                board[4][3] = firstPiece
                secondPiece = '.'
            board[3][4] = secondPiece
    elif (dir == "left"):
        firstPiece = '.'
        secondPiece = '.'

        if (box == "1"):
            if (board[0][0] != '.'):
                firstPiece = board[0][0]
            else:
                firstPiece = '.'
            if (board[2][0] != '.'):
                secondPiece = board[2][0]
                board[2][0] = firstPiece
            else:
                board[2][0] = firstPiece
                secondPiece = '.'
            if (board[2][2] != '.'):
                firstPiece = board[2][2]
                board[2][2] = secondPiece
            else:
                board[2][2] = secondPiece
                firstPiece = '.'
            if (board[0][2] != '.'):
                secondPiece = board[0][2]
                board[0][2] = firstPiece
            else:
                board[0][2] = firstPiece
                secondPiece = '.'
            board[0][0] = secondPiece
            firstPiece = '.'
            secondPiece = '.'
            if (board[0][1] != '.'):
                firstPiece = board[0][1]
            else:
                firstPiece = '.'
            if (board[1][0] != '.'):
                secondPiece = board[1][0]
                board[1][0] = firstPiece
            else:
                board[1][0] = firstPiece
                secondPiece = '.'
            if (board[2][1] != '.'):
                firstPiece = board[2][1]
                board[2][1] = secondPiece
            else:
                board[2][1] = secondPiece
                firstPiece = '.'
            if (board[1][2] != '.'):
                secondPiece = board[1][2]
                board[1][2] = firstPiece
            else:
                board[1][2] = firstPiece
                secondPiece = '.'
            board[0][1] = secondPiece


        elif (box == "2"):
       
            firstPiece = '.'
            secondPiece = '.'

            if (board[0][3] != '.'):
                firstPiece = board[0][3]
            else:
                firstPiece = '.'
            if (board[2][3] != '.'):
                secondPiece = board[2][3]
                board[2][3] = firstPiece
            else:
                board[2][3] = firstPiece
                secondPiece = '.'
            if (board[2][5] != '.'):
                firstPiece = board[2][5]
                board[2][5] = secondPiece
            else:
                board[2][5] = secondPiece
                firstPiece = '.'
            if (board[0][5] != '.'):
                secondPiece = board[0][5]
                board[0][5] = firstPiece
            else:
                board[0][5] = firstPiece
                secondPiece = '.'
            board[0][3] = secondPiece
            firstPiece = '.'
            secondPiece = '.'
            if (board[0][4] != '.'):
                firstPiece = board[0][4]
            else:
                firstPiece = '.'
            if (board[1][3] != '.'):
                secondPiece = board[1][3]
                board[1][3] = firstPiece
            else:
                board[1][3] = firstPiece
                secondPiece = '.'
            if (board[2][4] != '.'):
                firstPiece = board[2][4]
                board[2][4] = secondPiece
            else:
                board[2][4] = secondPiece
                firstPiece = '.'
            if (board[1][5] != '.'):
                secondPiece = board[1][5]
                board[1][5] = firstPiece
            else:
                board[1][5] = firstPiece
                secondPiece = '.'
            board[0][4] = secondPiece
      
        elif (box == "3"):
            firstPiece = '.'
            secondPiece = '.'

            if (board[3][0] != '.'):
                firstPiece = board[3][0]
            else:
                firstPiece = '.'
            if (board[5][0] != '.'):
                secondPiece = board[5][0]
                board[5][0] = firstPiece
            else:
                board[5][0] = firstPiece
                secondPiece = '.'
            if (board[5][2] != '.'):
                firstPiece = board[5][2]
                board[5][2] = secondPiece
            else:
                board[5][2] = secondPiece
                firstPiece = '.'
            if (board[3][2] != '.'):
                secondPiece = board[3][2]
                board[3][2] = firstPiece
            else:
                board[3][2] = firstPiece
                secondPiece = '.'
            board[3][0] = secondPiece
            firstPiece = '.'
            secondPiece = '.'
            if (board[3][1] != '.'):
                firstPiece = board[3][1]
            else:
                firstPiece = '.'
            if (board[4][0] != '.'):
                secondPiece = board[4][0]
                board[4][0] = firstPiece
            else:
                board[4][0] = firstPiece
                secondPiece = '.'
            if (board[5][1] != '.'):
                firstPiece = board[5][1]
                board[5][1] = secondPiece
            else:
                board[5][1] = secondPiece
                firstPiece = '.'
            if (board[4][2] != '.'):
                secondPiece = board[4][2]
                board[4][2] = firstPiece
            else:
                board[4][2] = firstPiece
                secondPiece = '.'
            board[3][1] = secondPiece
        else:
            firstPiece = '.'
            secondPiece = '.'

            if (board[3][3] != '.'):
                firstPiece = board[3][3]
            else:
                firstPiece = '.'
            if (board[5][3] != '.'):
                secondPiece = board[5][3]
                board[5][3] = firstPiece
            else:
                board[5][3] = firstPiece
                secondPiece = '.'
            if (board[5][5] != '.'):
                firstPiece = board[5][5]
                board[5][5] = secondPiece
            else:
                board[5][5] = secondPiece
                firstPiece = '.'
            if (board[3][5] != '.'):
                secondiece = board[3][5]
                board[3][5] = firstPiece
            else:
                board[3][5] = firstPiece
                secondPiece = '.'
            board[3][3] = secondPiece
            firstPiece = '.'
            secondPiece = '.'
            if (board[3][4] != '.'):
                firstPiece = board[3][4]
            else:
                firstPiece = '.'
            if (board[4][3] != '.'):
                secondPiece = board[4][3]
                board[4][3] = firstPiece
            else:
                board[4][3] = firstPiece
                secondPiece = '.'
            if (board[5][4] != '.'):
                firstPiece = board[5][4]
                board[5][4] = secondPiece
            else:
                board[5][4] = secondPiece
                firstPiece = '.'
            if (board[4][5] != '.'):
                secondPiece = board[4][5]
                board[4][5] = firstPiece
            else:
                board[4][5] = firstPiece
                secondPiece = '.'
            board[3][4] = secondPiece
            
    return board



player1 = input("Enter name of player1: ")
player2 = "AI"
player1Color = input("Player1 Token Color (B or W): ")
if (player1Color == "W"):
    computerColor = "B"
else:
    computerColor = "W"
choice = input("Player to Move First (1 or 2): ")
gameBoard = [['.' for x in range(6)] for y in range(6)]
if (choice == 2):
    player2 = player1
    player1 = "AI"
while (not checkWin(gameBoard, "W")):

    player1Move = input(player1 + " Enter Move: ")
    player1Move = player1Move.split()
    gameBoard = movePiece(gameBoard, player1Move[0], player1Color)
    print(player1Move)
    gameBoard = turnBoard(gameBoard,player1Move[1][1], player1Move[1][0])
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in gameBoard]))
    player2Move = input(player2 + " Enter Move")