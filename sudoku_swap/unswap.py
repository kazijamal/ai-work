#! /usr/bin/python3

import sys

Cliques = [[0, 1, 2, 3, 4, 5, 6, 7, 8],
           [9, 10, 11, 12, 13, 14, 15, 16, 17],
           [18, 19, 20, 21, 22, 23, 24, 25, 26],
           [27, 28, 29, 30, 31, 32, 33, 34, 35],
           [36, 37, 38, 39, 40, 41, 42, 43, 44],
           [45, 46, 47, 48, 49, 50, 51, 52, 53],
           [54, 55, 56, 57, 58, 59, 60, 61, 62],
           [63, 64, 65, 66, 67, 68, 69, 70, 71],
           [72, 73, 74, 75, 76, 77, 78, 79, 80],
           [0, 9, 18, 27, 36, 45, 54, 63, 72],
           [1, 10, 19, 28, 37, 46, 55, 64, 73],
           [2, 11, 20, 29, 38, 47, 56, 65, 74],
           [3, 12, 21, 30, 39, 48, 57, 66, 75],
           [4, 13, 22, 31, 40, 49, 58, 67, 76],
           [5, 14, 23, 32, 41, 50, 59, 68, 77],
           [6, 15, 24, 33, 42, 51, 60, 69, 78],
           [7, 16, 25, 34, 43, 52, 61, 70, 79],
           [8, 17, 26, 35, 44, 53, 62, 71, 80],
           [0, 1, 2, 9, 10, 11, 18, 19, 20],
           [3, 4, 5, 12, 13, 14, 21, 22, 23],
           [6, 7, 8, 15, 16, 17, 24, 25, 26],
           [27, 28, 29, 36, 37, 38, 45, 46, 47],
           [30, 31, 32, 39, 40, 41, 48, 49, 50],
           [33, 34, 35, 42, 43, 44, 51, 52, 53],
           [54, 55, 56, 63, 64, 65, 72, 73, 74],
           [57, 58, 59, 66, 67, 68, 75, 76, 77],
           [60, 61, 62, 69, 70, 71, 78, 79, 80]
           ]

neighborsDict = dict()


def findNeighbors(cell):
    ans = set()
    for clique in Cliques:
        if cell in clique:
            for c in clique:
                if c != cell:
                    ans.add(c)
    return list(ans)


def createNeighborsDict():
    for cell in range(81):
        neighborsDict[cell] = findNeighbors(cell)


createNeighborsDict()


def findErrors(board):
    index = 0
    s = set()
    for cell in board:
        neighbors = neighborsDict[index]
        for neighbor in neighbors:
            if board[index] == board[neighbor]:
                s.add(index)
        index += 1
    ans = list(s)
    return ans


def findSwap(board):
    errors = findErrors(board)
    copy = board.copy()
    for e in range(len(errors)):
        temp = copy[errors[e]]
        for s in range(len(errors)):
            copy[errors[e]] = copy[errors[s]]
            copy[errors[s]] = temp
            newErrors = findErrors(copy)
            if len(newErrors) == 0:
                ans = []
                if errors[e] < errors[s]:
                    ans.append(errors[e])
                    ans.append(errors[s])
                else:
                    ans.append(errors[s])
                    ans.append(errors[e])
                return ans
            copy = board.copy()


def unswap():
    if len(sys.argv) == 1:
        print('enter more arguments')
        return
    fin = open(sys.argv[1], 'r')
    lines = [line.split(',') for line in fin.read().split('\n')]
    fin.close()
    lines = lines[1:]
    print(lines)
    board = []
    fout = open(sys.argv[2], 'w')
    for line in lines:
        if len(line) != 9:
            print(board)
            if len(board) == 0:
                continue
            ans = findSwap(board)
            fout.write(str(ans[0]) + ',' + str(ans[1]) + '\n')
            board = []
        else:
            board += line
    fout.close()
    ### METHOD FOR PARSING WITH NEWLINE BETWEEN EACH BOARD ###
    # fin = open(sys.argv[1], 'r')
    # lines = fin.read().split('\n')
    # fin.close()
    # start = 1
    # end = 10
    # fout = open(sys.argv[2], 'w')
    # while end < len(lines):
    #     board = []
    #     for lineno in range(start, end):
    #         board += [int(x) for x in lines[lineno].split(',')]
    #     ans = findSwap(board)
    #     fout.write(str(ans[0]) + ',' + str(ans[1]) + '\n')
    #     start += 10
    #     end += 10
    # fout.close()
	### METHOD FOR PARSING WITH NEWLINE BETWEEN EACH BOARD ###
    # fin = open(sys.argv[1], 'r')
    # boards = fin.read().split('\n\n')
    # fin.close()
    # fout = open(sys.argv[2], 'w')
    # for board in boards:
    # 	currBoard = []
    # 	rows = board.split('\n')
    # 	rows = rows[1:]
    # 	for row in rows:
    # 		currBoard += [int(x) for x in row.split(',')]
    # 	ans = findSwap(currBoard)
    # 	fout.write(str(ans[0]) + ',' + str(ans[1]) + '\n')
    # fout.close()


def main():
    unswap()


if __name__ == "__main__":
    main()
