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

n = int(I())
grid = [[-1] * n for _ in range(n)]
grid[0][0] = 0

Q = deque([(0,0,1)])

while Q:
	i,j,moves = Q.popleft()
	for nx,ny in [(i-2,j+1),(i-2,j-1),(i+2,j+1),(i+2,j-1),(i+1,j-2),(i-1,j-2),(i+1,j+2),(i-1,j+2)]:
		if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == -1:
			grid[nx][ny] = moves
			Q.append((nx,ny,moves+1))

for g in grid:
	print(*g)

