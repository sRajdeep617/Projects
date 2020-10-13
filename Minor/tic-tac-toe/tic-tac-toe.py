board=[' ' for x in range(10) ]#there is no zero or 10, range is from 1-9

def insertInBoard(symbol,pos):
    # here symbol refers to 'X' or 'O'
    # pos refers to the the position where we have to enter
    board[pos]=symbol

def workingOnBoard(board):
    # creating and updating board 
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')

def spaceAvailable(pos):
    # check if the position where we want to input is available or not
    return(board[pos]==' ')

def isBoardFull(board):
    # check if board is full or it still has sapce available
    if board.count(' ') > 1:
        # space is available
        return False
    else: 
        # board is full
        return True

def checkForWinner(b,l):
    # here b is for borad and l for the symbol 'X' or 'O'
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))

def playerMove():
    run=True
    while run:
        pos=input('Please select a position(1-9) to enter the "X": ')
        try:
            pos=int(pos)
            if pos >0 and pos < 10:
                if spaceAvailable(pos):
                    run=False # to indicate computer to make its move
                    insertInBoard('X',pos)
                else:
                    print('This space is occupied!')
            else:
                print('Please enter a valid position that is a digits between 1 and 9')
                
        except:
            # will work when try block fails
            # when user enters a string and try to convert it into integer
            print('Enter a digit between 1 and 9')

def computerMove():
    possibleMoves = [x for x , letter in enumerate(board) if letter == ' ' and x != 0  ]
    move = 0

    for let in ['O' , 'X']:
        for i in possibleMoves:
            board_copy = board[:]
            board_copy[i] = let
            if checkForWinner(board_copy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1 , 3 , 7 , 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def main():
    print("Aloha! Welcome to the Game!")
    workingOnBoard(board)

    while not(isBoardFull(board)):
        if not(checkForWinner(board , 'O')):
            playerMove()
            workingOnBoard(board)
        else:
            print("You lost! Better luck next time!!")
            break

        if not(checkForWinner(board,'X')):
            move=computerMove()
            if move==0:
                print(" ")
            else:
                insertInBoard('O',move)
                print('The Computer placed an "O" on position',move ,':')
                workingOnBoard(board)
        else:
            print("Gracias! Congratulations you won!!")
            break

    
    if isBoardFull(board):
        print("The Game is tied!")

while True:
    x = input("Do you want to play? ")
    if (x.lower() == 'y') or (x.lower()=='yes'):
        board = [' ' for x in range(10)]
        print('--------------------')
        main()
    else:
        break



