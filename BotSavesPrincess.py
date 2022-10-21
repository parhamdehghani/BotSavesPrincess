#!/usr/bin/python3


def displayPathtoPrincess(n,grid):
    moves = []
    diff = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'p':
                p_index = [i,j]

    center_index = [(n-1)/2,(n-1)/2]
    diff.append(p_index[0] - center_index[0])
    diff.append(p_index[1] - center_index[1])
    if diff[0] < 0:
        moves.append(int(abs(diff[0]))*'UP ')
    else:
        moves.append(int(diff[0])*'DOWN ')

    if diff[1] < 0:
        moves.append(int(abs(diff[1]))*'LEFT ')
    else:
        moves.append(int(diff[1])*'RIGHT ')

    score = (n**2 - len(moves)) / 10.0

    for i in range(len(moves[0].split())):
        print("{}".format(moves[0].split()[i]))
        print("{}".format(moves[1].split()[i]))

m = int(input())
grid = []
for i in range(m):
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
