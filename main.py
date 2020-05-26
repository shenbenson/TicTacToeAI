import math
import random


def checkwin(board):
    for row in range(3):
        phcheck = 0
        pvcheck = 0
        ahcheck = 0
        avcheck = 0
        for col in range(3):
            if board[row][col] == human:
                phcheck += 1
            if board[col][row] == human:
                pvcheck += 1
            if board[row][col] == ai:
                ahcheck += 1
            if board[col][row] == ai:
                avcheck += 1
        if phcheck == 3 or pvcheck == 3:
            return human
        elif ahcheck == 3 or avcheck == 3:
            return ai

    if board[0][0] == human and board[1][1] == human and board[2][2] == human:
        return human
    if board[0][0] == ai and board[1][1] == ai and board[2][2] == ai:
        return ai
    if board[2][0] == human and board[1][1] == human and board[0][2] == human:
        return human
    if board[2][0] == ai and board[1][1] == ai and board[0][2] == ai:
        return ai

    empty = 0
    for row in range(3):
        for col in range(3):
            if board[row][col] == '•':
                empty += 1
    if empty == 0:
        return "tie"

    return "N"


def printboard(board):
    print()
    print(board[0][0] + " " + board[0][1] + " " + board[0][2])
    print(board[1][0] + " " + board[1][1] + " " + board[1][2])
    print(board[2][0] + " " + board[2][1] + " " + board[2][2])


def minimax(board, depth, isMaximizing):
    result = checkwin(board)

    if result != "N":
        if result == human:
            return -1
        elif result == ai:
            return 1
        else:
            return 0
    if depth == 0:
        return 0

    if isMaximizing:
        bestscore = -math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == '•':
                    board[row][col] = ai
                    score = minimax(board, depth - 1, False)
                    board[row][col] = '•'
                    if score > bestscore:
                        bestscore = score
        return bestscore
    else:
        bestscore = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == '•':
                    board[row][col] = human
                    score = minimax(board, depth - 1, True)
                    board[row][col] = '•'
                    if score < bestscore:
                        bestscore = score
        return bestscore


def playgame():
    if userin == "f":
        player = human
    else:
        player = ai
    game = [['•', '•', '•'],
            ['•', '•', '•'],
            ['•', '•', '•']]
    count = 0
    while checkwin(game) == "N" and count < 9:
        if player == human:
            printboard(game)
            while True:
                move = input(player + " make your move: ")
                r = 2 - int((int(move) - 1) / 3)
                c = round((int(move) % 3 + 2) % 3)
                if game[r][c] == '•':
                    game[r][c] = player
                    break
                else:
                    print("you can't go there...")
        else:
            if count == 0:
                start = random.randint(0, 3)
                if start == 0:
                    game[0][0] = ai
                elif start == 1:
                    game[0][2] = ai
                elif start == 2:
                    game[2][0] = ai
                else:
                    game[2][2] = ai
            else:
                bestscore = -math. inf
                for row in range(3):
                    for col in range(3):
                        if game[row][col] == '•':
                            game[row][col] = ai
                            score = minimax(game, 9, False)
                            game[row][col] = '•'
                            if score > bestscore:
                                bestscore = score
                                bestr = row
                                bestc = col
                game[bestr][bestc] = ai
        count += 1
        if player == human:
            player = ai
        else:
            player = human

    print("\n")
    if count == 9:
        print("Tie")
    elif player == human:
        print(ai + " win")
    else:
        print(human + " win")

    printboard(game)


while True:
    userin = input("first or second: ")
    if userin == "f":
        human = "x"
        ai = "o"
    else:
        human = "o"
        ai = "x"
    playgame()
    userin = input("Enter y to play again, anything else to quit: ")
    if userin != "y":
        break
