#!/usr/bin/env python3
import sys
import string
import collections


alp = list(string.ascii_uppercase)


# getBoard: get board from reading file maze
# Input: read from file maze
# Output: list board
def getBoard():
    sys.stdin.readline()
    board = []
    while True:
        x = sys.stdin.readline()
        if x[0] != "#":
            break
        board.append(x.rstrip('\n'))
    return board


# getPos: get position of my
# Input: board and name of my
# Output: my IA position [y,x]
def getPos(board, name):
    for i in board:
        if name in i:
            return [board.index(i), i.index(name)]


# checkBonus: check if there is any "!" in board
# Input: board
# Output: True or False
def checkBonus(board):
    for i in board:
        if '!' in i:
            return True
    return False


# checkOpp: check if there is any opponent
# Input: board and position of my IA
# Output: True or False
def checkOpp(board, cur):
    y, x = cur
    for x2, y2 in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
        if x2 >= 0 and y2 >= 0 and x2 < len(board[0]) and y2 < len(board):
            if board[y2][x2] in alp:
                return True
    return False


# move: str of moving my IA will send to maze
# Input: position of my IA and position of next move
# Output: right string to send
def move(cur, point):
    if point[0] - cur[0] == 1:
        return "MOVE DOWN\n\n"
    elif point[0] - cur[0] == -1:
        return "MOVE UP\n\n"
    elif point[1] - cur[1] == 1:
        return "MOVE RIGHT\n\n"
    elif point[1] - cur[1] == -1:
        return "MOVE LEFT\n\n"


# bfs: bfs algorithm to find path to get "o" and "!"
# Input: board, my IA position and symbol(can be "o", "!" or " ")
# Output: path(list of next position) to "o" or "!"
def bfs(board, cur, sym):
    queue = collections.deque([[cur]])
    visited = set([cur])
    while queue:
        path = queue.popleft()
        y, x = path[-1]
        if board[y][x] == sym:
            path.remove(path[0])
            return path
        for x2, y2 in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if board[y2][x2] != "#" and (y2, x2) not in visited:
                if board[y2][x2] not in alp:
                    queue.append(path + [[y2, x2]])
                    visited.add((y2, x2))


def main():
    rea = sys.stdin.readline()
    while rea != '':
        if 'HELLO' in rea:
            sys.stdout.write('I AM A\n\n')
        if 'YOU ARE' in rea:
            name = rea[-2]
            sys.stdout.write('OK\n\n')
        if 'MAZE' in rea:
            y = getBoard()
            A = getPos(y, name)
            if checkOpp(y, A):
                res = bfs(y, (A[0], A[1]), 'o')
            else:
                if checkBonus(y):
                    res = bfs(y, (A[0], A[1]), '!')
                    if res is None or len(res) >= 20:
                        res = bfs(y, (A[0], A[1]), 'o')
                else:
                    res = bfs(y, (A[0], A[1]), 'o')
            if res is None:
                res = bfs(y, (A[0], A[1]), ' ')
            sys.stdout.write(move(A, res[0]))
        rea = sys.stdin.readline()


if __name__ == '__main__':
    main()
