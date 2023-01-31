import random
import os
import time


uinp = 0


def neighbours (grid, x, y):
    
    tot = 0

    taille = len(grid)-1
    
    if x == y == 0:
        if grid[x][y+1] == 1:
            tot += 1
        if grid[x+1][y] == 1:
            tot += 1
        if grid[x+1][y+1] == 1:
            tot += 1
    
    elif (x == taille) and (y == 0):
        if grid[x-1][y] == 1:
            tot += 1
        if grid[x-1][y+1] == 1:
            tot += 1
        if grid[x][y+1] == 1:
            tot += 1

    elif (x == 0) and (y == taille):
        if grid[x+1][y] == 1:
            tot += 1
        if grid[x+1][y-1] == 1:
            tot += 1
        if grid[x][y-1] == 1:
            tot += 1

    elif x == y == taille:
        if grid[x][y-1] == 1:
            tot += 1
        if grid[x-1][y-1] == 1:
            tot += 1
        if grid[x-1][y] == 1:
            tot += 1

    elif x == 0:
        if grid[x][y-1] == 1:
            tot += 1
        if grid[x][y+1] == 1:
            tot += 1
        if grid[x+1][y-1] == 1:
            tot += 1
        if grid[x+1][y] == 1:
            tot += 1
        if grid[x+1][y+1] == 1:
            tot += 1
    
    elif x == taille:
        if grid[x][y-1] == 1:
            tot += 1
        if grid[x][y+1] == 1:
            tot += 1
        if grid[x-1][y-1] == 1:
            tot += 1
        if grid[x-1][y] == 1:
            tot += 1
        if grid[x-1][y+1] == 1:
            tot += 1

    elif y == 0:
        if grid[x-1][y] == 1:
            tot += 1
        if grid[x-1][y+1] == 1:
            tot += 1
        if grid[x][y+1] == 1:
            tot += 1
        if grid[x+1][y] == 1:
            tot += 1
        if grid[x+1][y+1] == 1:
            tot += 1
    
    elif y == taille:
        if grid[x][y-1] == 1:
            tot += 1
        if grid[x+1][y] == 1:
            tot += 1
        if grid[x+1][y-1] == 1:
            tot += 1
        if grid[x-1][y-1] == 1:
            tot += 1
        if grid[x-1][y] == 1:
            tot += 1

    else:
        if grid[x-1][y-1] == 1:
            tot += 1
        if grid[x-1][y] == 1:
            tot += 1
        if grid[x-1][y+1] == 1:
            tot += 1
        if grid[x][y-1] == 1:
            tot += 1    
        if grid[x][y+1] == 1:
            tot += 1
        if grid[x+1][y-1] == 1:
            tot += 1
        if grid[x+1][y] == 1:
            tot += 1
        if grid[x+1][y+1] == 1:
            tot += 1
    return tot



def affichage (grid, uinp):
    os.system('clear')
    for i in range (uinp):
        print()
        for j in range (uinp):
            print(grid[i][j], end='')


def GameOfLife ():

    uinp = int(input("qu'elle est la taille de votre tableau ? "))

    grid = [[(random.randint(0,1)) for x in range(uinp)] for y in range(uinp)]

    print()

    r = int(input("Combien d'itérations voulez vous faire ? "))

    print()

    for k in range (r):

        grid2 = grid

        affichage(grid, uinp)
        time.sleep(0.5)
        for i in range(uinp):

            for j in range(uinp):

                if (neighbours(grid, i, j) == 3) and (grid[i][j] == 0):
                    grid2[i][j] = 1
                elif neighbours(grid, i , j) < 2:
                    grid2[i][j] = 0
                elif (neighbours(grid, i, j) > 3):
                    grid2[i][j] = 0
        
        grid = grid2

                
GameOfLife()
    
                