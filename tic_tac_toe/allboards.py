''' Layout positions:
0 1 2
3 4 5
6 7 8
'''
# layouts look like "_x_ox__o_"

Wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

AllBoards = {} # this is a dictionary with key = a layout, and value = its corresponding BoardNode

class BoardNode:
    def __init__(self,layout):
        self.layout = layout
        self.endState = None # if this is a terminal board, endState == 'x' or 'o' for wins, of 'd' for draw, else None
        self.children = [] # all layouts that can be reached with a single move
        
    def print_me(self):
        print ('layout:',self.layout, 'endState:',self.endState)
        print ('children:',self.children)

def gameState(layout):
    for win in Wins:
        if layout[win[0]] == layout[win[1]] == layout[win[2]]:
            if layout[win[0]] == 'x':
                return 'x'
            if layout[win[0]] == 'o':
                return 'o'
    full = True
    for cell in layout:
        if cell == '_':
            full = False
    if full == True:
        return 'd'
    return None
        
def CreateAllBoards(layout, parent=None):
    # recursive function to manufacture all BoardNode nodes and place them into the AllBoards dictionary
    curr_node = BoardNode(layout)
    curr_state = gameState(layout)
    if curr_state:
        curr_node.endState = curr_state
        AllBoards[layout] = curr_node
        return
    else:
        if not parent:
            turn = 'x'
        else:
            for i in range(9):
                if layout[i] != parent[i]:
                    last_turn = layout[i]
            if last_turn == 'x':
                turn = 'o'
            elif last_turn == 'o':
                turn = 'x'
        children = []
        for i in range(9):
            if layout[i] == '_':
                child = layout[:i] + turn + layout[i+1:]
                children.append(child)
        curr_node.children = children
        AllBoards[layout] = curr_node
        for child in children:
            CreateAllBoards(child, layout)
        
def main():
    CreateAllBoards('_________')
    print('number of boards:', len(AllBoards))
    num_children = 0
    x_wins = 0
    o_wins = 0
    draws = 0
    not_end = 0
    for board in AllBoards.values():
        num_children += len(board.children)
        state = board.endState
        if not state:
            not_end += 1
        elif state == 'x':
            x_wins += 1
        elif state == 'o':
            o_wins += 1
        elif state == 'd':
            draws += 1
    print('number of children:', num_children)
    print('number of x wins:', x_wins)
    print('number of o wins:', o_wins)
    print('number of draws:', draws)
    print('number of not ends-of-games:', not_end)

main()
