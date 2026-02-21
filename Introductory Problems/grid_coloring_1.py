from typing import *
from sys import maxsize, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right
from collections import deque, Counter, defaultdict

setrecursionlimit(10**8)
MOD = 10 ** 9 + 7

def I():    return stdin.readline().rstrip('\r\n')
def ari():  return list(map(int,I().split()))
def ars():  return list(map(str,I().split()))
def arf():  return list(map(float,I().split()))
def mpi():  return map(int,I().split())
def mps():  return map(str,I().split())
def mpf():  return map(float,I().split())

n,m = mpi()
grid = []
for i in range(n):
	grid.append(list(str(I())))

for i in range(n):
	for j in range(m):
		upp = grid[i-1][j] if i-1 >= 0 else None
		left = grid[i][j-1] if j-1 >= 0 else None
		old = grid[i][j]
		for ch in ['A','B','C','D']:
			if ch not in [upp, left, old]:
				grid[i][j] = ch
				break

for g in grid:
	print("".join(g))
