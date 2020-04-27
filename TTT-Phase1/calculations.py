#! /usr/bin/python3

Wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

# Transformations (rotations are counter-clockwise)
Rot90 = [6,3,0,7,4,1,8,5,2]
Rot180 = [8,7,6,5,4,3,2,1,0]
Rot270 = [2,5,8,1,4,7,0,3,6]
VertFlip= [2,1,0,5,4,3,8,7,6]
Transformations = [[Rot90],[Rot180],[Rot270],[VertFlip],[Rot90,VertFlip],[Rot180,VertFlip],[Rot270,VertFlip]]

not_finished = -1
draw = 0
x_win = 1
o_win = 2

x_wins = 0
o_wins = 0
draws = 0
possible_games = 0

possible_configurations = {'_________'}

def printBoard(board):
    print((' | ').join(board[:3]))
    print('---------')
    print((' | ').join(board[3:6]))
    print('---------')
    print((' | ').join(board[6:]))
    print()
    
def gameState(board):
    for win in Wins:
        if board[win[0]] == board[win[1]] == board[win[2]]:
            if board[win[0]] == 'x':
                return x_win
            if board[win[0]] == 'o':
                return o_win
    full = True
    for cell in board:
        if cell == '_':
            full = False
    if full == True:
        return draw
    return not_finished

def finishGameTree(board, turn, move):
    global x_wins, o_wins, draws, possible_games
    # complete current turn
    board = board[:move] + turn + board[move+1:]
    # add current board to possible configurations set
    possible_configurations.add(board)
    # change turn
    if turn == 'x':
        turn = 'o'
    elif turn == 'o':
        turn = 'x'
    # move on to next turn if game not finished
    state = gameState(board)
    if state == not_finished:
        # calculate next move
        possible_moves = []
        for i in range(9):
            if board[i] == '_':
                possible_moves.append(i)
        # compute game trees for all possible moves
        for possible_move in possible_moves:
            finishGameTree(board, turn, possible_move)
    else:
        if state == x_win:
            x_wins += 1
        elif state == o_win:
            o_wins += 1
        elif state == draw:
            draws += 1
        possible_games += 1

def calculatePossibleGames():
    for start in range(9):
        finishGameTree('_________', 'x', start)

def calculateIrreducibleBoardFamilies():
    families = list()
    added = set()
    for board in possible_configurations:
        if board not in added:
            # create a new family for the current board
            added.add(board)
            family = [board]
            listboard = list(board)
            # perform transformations and add them to family
            for transformation in Transformations:
                if len(transformation) == 1:
                    transformed = [listboard[i] for i in transformation[0]]
                    joined = ''.join(transformed)
                    if joined in possible_configurations and joined not in added:
                        added.add(joined)
                        family.append(joined)
                elif len(transformation) == 2:
                    transformed1 = [listboard[i] for i in transformation[0]]
                    transformed2 = [transformed1[i] for i in transformation[1]]
                    joined = ''.join(transformed2)
                    if joined in possible_configurations and joined not in added:
                        added.add(joined)
                        family.append(joined)
            families.append(family)
    return len(families)
                
        
def main():
    calculatePossibleGames()
    print('Number of different possible games:', possible_games)
    print('X wins:', x_wins)
    print('O wins:', o_wins)
    print('Draws:', draws)
    print('Number of different possible board configurations:', len(possible_configurations))
    print('Number of irreducible board families:', calculateIrreducibleBoardFamilies())

main()
