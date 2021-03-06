# TicTacToe - perfect competitor code outline

import sys

Usage = '''Usage:
python3 TTT-Random-NetLogo.py {result-filename} {board}
'''

Positions = ('Top-left','Top-center','Top-right','Middle-left','Middle-center',\
             'Middle-right','Bottom-left','Bottom-center','Bottom-right')

# Below, any  variable called "board" contains a board layout string of 9 chars or 'x', 'o' and '_'
# AllBoards is a dictionary of all boards
# key = board, value = the Tboard instance
AllBoards = {}

wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

class Tboard:

    def __init__(self,board,lastmove):
        '''lastmove is the move that led to this board'''
        self.board = board
        self.lastmove = lastmove  # the move (0-8) that led to this board, None if this is the root board

        self.player,self.opponent = WhoseMove(board)

        # state is 'x' if this board is or will be a win for 'x' if the best moves are taken
        # state is 'o' if win for 'o'
        # state is None if we haven't figured this out yet
        self.state = None
        
        # moves_to_state is how many moves from here to the state if best moves are taken
        # moves_to_state == 0 if this board is actually a final board in the game
        # moves_to_state == None if we haven't figure this out yet
        self.moves_to_state = None

        # best_move is the best next move (0-8) to lead to a win, or if not,
        #   at least a draw, or, sadly, a necessary loss
        #  or -1 if this is a final board
        self.best_move = None

        self.children = [] # list of child Tboards


def FigureItOut(board):
    '''returns a list: best_move, moves_to_state, and state
    best_move (0-8) is, you know, the best move, unless moves_to_state == 0
    if moves_to_state == 0 then we're at the end of the game
    and state is the expected final state: 'x', 'o', or 'd', for X-winning, O-winning, or Draw'''
    AllBoards.clear()
    
    root = Tboard(board,None)
    AllBoards[board] = root

    # Step 1:
    # Create the board tree starting from this root.
    FindAllBoards(root)
    
    # Step 2:
    # now traverse the game tree (depth first), filling in best_move, moves_to_state and state
    CalcBestMove(root)
    
    return [root.best_move, root.moves_to_state, root.state]

def FindAllBoards(board_node):
    ''' Constructs the subtree of boards leading from board_node and puts all such boards (layouts)
    into the dictionary AllBoards.  Uses AllBoards to prevent dublicate boards.  This should
    create a tree of maximum 5478 boards if we start from the empty board.  But usually we won't
    start from the empty board'''
    
    if board_node in AllBoards:
        return

    AllBoards[board_node.board] = board_node
    
    # is this a final board?
    endboard = IsEndBoard(board_node.board)  # returns 'x' or 'o' or 'd' if final, else None
    if endboard is not None:   # this board is a win for 'x' or 'o' or a draw
        board_node.state = endboard
        board_node.moves_to_state = 0
        board_node.best_move = -1
        return

    # Now recurse through all the children:
    this_board = board_node.board
    player = board_node.player
    for i in range(9):
        if this_board[i] == '_':
            child_board = this_board[:i]+player+this_board[i+1:]
            child_node = Tboard(child_board,i)
            board_node.children.append(child_node)
            FindAllBoards(child_node)
    return

def minimax(board_node, maximize, moves):
    state = board_node.state
    if state is not None:
        if state == board_node.player:
            return [1, moves, board_node]
        elif state == board_node.opponent:
            return [-1, moves, board_node]
        elif state == 'd':
            return [0, moves, board_node]
    else:
        if maximize:
            best_score = -2
            best_move = None
            for child in board_node.children:
                curr_score = minimax(child, False, moves + 1)
                if curr_score[0] > best_score:
                    best_score = curr_score[0]
                    best_move = curr_score[2]
            return [best_score, curr_score[1], best_move]
        else:
            worst_score = 2
            worst_move = None
            for child in board_node.children:
                curr_score = minimax(child, True, moves + 1)
                if curr_score[0] < worst_score:
                    worst_score = curr_score[0]
                    worst_move = curr_score[2]
            return [worst_score, curr_score[1], worst_move]
        
        
def CalcBestMove(board_node):
    '''  updates this board_node with correct values for state, moves_to_state, and best_move
    (This is the engine.)'''
    best_score = -2
    for child in board_node.children:
        curr_score = minimax(child, True, 0)
        if curr_score[0] > best_score:
            best_score, best_moves, best_move = curr_score
    board_node.state = best_move.state
    board_node.moves_to_state = best_moves
    board_node.best_move = best_move.lastmove

        
def WhoseMove(board):
    '''returns the player (either 'x' or 'o') and also opponent'''
    if board.count('x') == board.count('o'):
        return ['x','o']
    return ['o', 'x']

def IsEndBoard(board):
    for awin in wins:
        if board[awin[0]] != '_' and board[awin[0]] == board[awin[1]] and board[awin[1]] == board[awin[2]]:
            return board[awin[0]]
    if board.count('_') == 0:
        return 'd'
    return None

def PrintBoardNode(node):
    '''for debugging'''
    print('layout',node.board)
    print('last_move',node.lastmove)
    print('player',node.player)
    print('state',node.state)
    print('moves_to_state',node.moves_to_state)
    print('best_move',node.best_move)
    for child_node in node.children:
        print('child',child_node.lastmove,child_node.board)

def main():
    if len(sys.argv) != 3:
        print(Usage)
        return
    outfile = sys.argv[1]
    board = sys.argv[2]
    best_move, moves_to_state, state = FigureItOut(board)
    print("best_move:", best_move)
    print("moves_to_state:", moves_to_state)
    print("state:", state)
    s = '%d\n' % best_move
    s += '%s\n' % Positions[best_move]
    s += '%s in %d moves' % (state, moves_to_state)
    f = open(outfile,'w')
    f.write(s)
    f.close()

main()
