from typing import *
from sys import maxsize, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right
from collections import deque, Counter

setrecursionlimit(10**8)
MOD = 10 ** 9 + 7

def I():    return stdin.readline().rstrip('\r\n')
def ari():  return list(map(int,I().split()))
def ars():  return list(map(str,I().split()))
def arf():  return list(map(float,I().split()))
def mpi():  return map(int,I().split())
def mps():  return map(str,I().split())
def mpf():  return map(float,I().split())

def isValidPos(mat,i,j):

    # Checking same row for queens
    for jy in range(len(mat[0])):
        if mat[i][jy] == 'Q':
            return False

    # Checking same col for queens
    for ix in range(len(mat)):
        if mat[ix][j] == 'Q':
            return False

    # checking diagonals
    ci,cj,diff = i,j,1
    while 1:
        dxTopLeft,dyTopLeft = ci - diff, cj - diff
        dxTopRight,dyTopRight = ci - diff, cj + diff
        dxBottomLeft,dyBottomLeft = ci + diff, cj - diff
        dxBottomRight,dyBottomRight = ci + diff, cj + diff

        allInvalid = 0

        if 0 <= dxTopLeft < len(mat) and 0 <= dyTopLeft < len(mat[0]):
            allInvalid |= 1
            if mat[dxTopLeft][dyTopLeft] == 'Q':
                return False
        if 0 <= dxTopRight < len(mat) and 0 <= dyTopRight < len(mat[0]):
            allInvalid |= 1
            if mat[dxTopRight][dyTopRight] == 'Q':
                return False
        if 0 <= dxBottomLeft < len(mat) and 0 <= dyBottomLeft < len(mat[0]):
            allInvalid |= 1
            if mat[dxBottomLeft][dyBottomLeft] == 'Q':
                return False
        if 0 <= dxBottomRight < len(mat) and 0 <= dyBottomRight < len(mat[0]):
            allInvalid |= 1
            if mat[dxBottomRight][dyBottomRight] == 'Q':
                return False

        if not allInvalid:
            break
        diff += 1

    return True

def queens(mat,qCount: int, initialI: int):
    global qways
    if qCount == 8:
        qways += 1
        return
    for i in range(initialI,len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == '.' and isValidPos(mat,i,j):
                mat[i][j] = 'Q'
                queens(mat,qCount + 1,i+1)
                mat[i][j] = '.'

mat = []
qways = 0

for i in range(8):
    mat.append(list(str(I())))

queens(mat[:],0,0)

print(qways)