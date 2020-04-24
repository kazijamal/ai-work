#! /usr/bin/python3

import sys
import time

Cliques=[[0,1,2,3,4,5,6,7,8],[9,10,11,12,13,14,15,16,17],[18,19,20,21,22,23,24,25,26],[27,28,29,30,31,32,33,34,35],[36,37,38,39,40,41,42,43,44],[45,46,47,48,49,50,51,52,53],[54,55,56,57,58,59,60,61,62],[63,64,65,66,67,68,69,70,71],[72,73,74,75,76,77,78,79,80],[0,9,18,27,36,45,54,63,72],[1,10,19,28,37,46,55,64,73],[2,11,20,29,38,47,56,65,74],[3,12,21,30,39,48,57,66,75],[4,13,22,31,40,49,58,67,76],[5,14,23,32,41,50,59,68,77],[6,15,24,33,42,51,60,69,78],[7,16,25,34,43,52,61,70,79],[8,17,26,35,44,53,62,71,80],[0,1,2,9,10,11,18,19,20],[3,4,5,12,13,14,21,22,23],[6,7,8,15,16,17,24,25,26],[27,28,29,36,37,38,45,46,47],[30,31,32,39,40,41,48,49,50],[33,34,35,42,43,44,51,52,53],[54,55,56,63,64,65,72,73,74],[57,58,59,66,67,68,75,76,77],[60,61,62,69,70,71,78,79,80]]

Neighbors = {}  # key is cell-id, value is set of neighbors.  Neighbors[2] = set(0,1,3,4,5,6,7,8,11,20,29,38,47,56,65,74,9,10,18,19)

Possibilities = {}

# States
NEW_CELL = 0
FIND_NEXT_CELL = 1
BACKTRACK = 2
AllVals = set([1,2,3,4,5,6,7,8,9])

class MyStack:
    def __init__(self,store_immediate_list = None):
        self.storage = []
        self.filled = 0
        # if there's anything to store immediately, push all items in that list
        if store_immediate_list:
            for an_item in store_immediate_list:
                self.push(an_item)

    def size(self):
        return self.filled

    def push(self,item):
        if self.filled == len(self.storage):
            self.storage.append(item)
        else:
            self.storage[self.filled] = item
        self.filled += 1

    def pop(self):
        if self.filled == 0:
            return None
        self.filled -= 1
        return self.storage[self.filled]

    def peek(self,where = 0):
        if where >= 0:
            if where >= self.filled:
                return None
            return self.storage[self.filled - 1 - where]
        else:
            where = -where
            if where > self.filled:
                return None
            return self.storage[where-1]

def getBoard(argv = None):
    if not argv:
        argv = sys.argv
    board_name = argv[3]
    with open(argv[1],'r') as f_in:
        lines = f_in.read().split('\n')
        i = 0
        while i < len(lines):
            if len(lines[i].split(',')) == 3 and lines[i].split(',')[0] == board_name:
                board = []
                name = lines[i]
                for j in range(i+1,i+10):
                    for x in lines[j].split(','):
                        try:
                            board.append(int(x))
                        except ValueError:
                            board.append(x)
                i += 9
                return name, board
            else:
                i += 1
        
                
def makeNeighbors():
    global Neighbors
    for cell in range(81):
        nb = set()
        for clique in Cliques:
            if cell in clique:
                nb.update(clique)
        nb.discard(cell)
        Neighbors[cell] = nb

def calculatePossibilities(board):
    global Neighbors, Possibilities
    Possibilities = {}
    open_cells = [cell for cell in range(81) if board[cell] == '_']
    for cell in open_cells:
        possible = set([1,2,3,4,5,6,7,8,9])
        neighbors = Neighbors[cell]
        for neighbor in neighbors:
            possible.discard(board[neighbor])
        Possibilities[cell] = possible

def minPossibilities():
    global Possibilities
    minlen = 10
    min = None
    for cell,possibility in Possibilities.items():
        if len(possibility) < minlen:
            min = cell
            minlen = len(possibility)
    return min
        
def isSolved(board):
    # returns a list of the positions on this board whose values are incorrect
    inc = []
    for pos in range(len(board)):
        val = board[pos]
        for neighbor in Neighbors[pos]:
            if board[neighbor] == val:
                inc.append(pos)
                break
    if len(inc) == 0:
        return True
    else:
        return False

def printBoard(board):
    for row in range(9):
        arow = []
        for col in range(9):
            arow.append(str(board[9*row+col]))
        print(','.join(arow))
    print('\n')

def nextOpenCell(board):
    calculatePossibilities(board)
    return minPossibilities()
    
def nextOpenCellOld(board, curr_cell):
    for cell in range(curr_cell + 1, 81):
        if board[cell] == '_':
            return cell
    return None

def nextValidGuess(board, cell, next_guess):
    guess = None
    forced = None
    neighbors = Neighbors[cell]
    neighborValues = set()
    for neighbor in neighbors:
        neighborValues.add(board[neighbor])
    values = AllVals.copy()
    for value in range(0, next_guess):
        values.discard(value)
    for neighborValue in neighborValues:
        values.discard(neighborValue)
    if len(values) == 0:
        return guess,forced
    else:
        guess = 10
        for value in values:
            if value < guess:
                guess = value
        if len(values) == 1:
            forced = True
        else:
            forced = False
        return guess,forced
    
        
def writeBoard(argv,name,board):
    with open(argv[2],'w') as f_out:
        for row in range(9):
            arow = []
            for col in range(9):
                arow.append(str(board[9*row+col]))
            f_out.write(','.join(arow) + '\n')

def main(argv = None):
    if not argv:
        argv = sys.argv

    name,board = getBoard(argv)
    mystack = MyStack()
    makeNeighbors()
    nback = 0
    ntrials = 0
    cell = nextOpenCell(board)
    state = NEW_CELL
    start_time = time.time()
    end_time = None
    elapsed_time = None
    
    while True:
        ntrials += 1
        #if ntrials % 10000 == 0: print('ntrials,nback',ntrials,nback)

        # we're on a new open cell
        if state == NEW_CELL:
            guess,forced = nextValidGuess(board,cell,1)
            #print ("NEW_CELL,cell,guess,forced",cell,guess,forced)
            if not guess:
                # failed to find a valid guess for this cell, backtrack
                state = BACKTRACK
            else:
                board[cell] = guess
                if not forced:
                    mystack.push([cell,board[:]])
                state = FIND_NEXT_CELL

        # find a new open cell
        if state == FIND_NEXT_CELL:
            cell = nextOpenCell(board)
            if cell == None:
                # Solution!
                end_time = time.time()
                elapsed_time = end_time - start_time
                break
            state = NEW_CELL
            continue

        # backtrack
        if state == BACKTRACK:
            nback += 1
            cell,board = mystack.pop()
            old_guess = board[cell]
            guess,forced = nextValidGuess(board,cell,old_guess+1)
            # print('BACKTRACK,cell,guess,forced',cell,guess,forced)
            if not guess:
                state = BACKTRACK
            else:
                board[cell] = guess
                mystack.push([cell,board[:]])
                state = FIND_NEXT_CELL
            continue

    print('Solution!, with ntrials, backtracks: ', ntrials,nback)
    printBoard(board)
    writeBoard(argv,name,board)
    print('Took', elapsed_time, 'seconds to solve')
    solved = isSolved(board)
    if solved:
        print('The board was solved')
    else:
        print('The board was not solved')
                   
        
main()


















