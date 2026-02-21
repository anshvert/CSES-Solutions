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
grid = [[0] * n for _ in range(n)]
rowMax,colMax = defaultdict(set),defaultdict(set)

# Fill first row
for i in range(n):
	grid[0][i] = i
	rowMax[0].add(i)
	colMax[i].add(i)

# Fill the first column
for j in range(n):
	grid[j][0] = j
	rowMax[j].add(j)
	colMax[0].add(j)

for i in range(1,n):
	for j in range(1,n):
		if i == j: continue
		for num in range(1,n**2):
			if num not in rowMax[i].union(colMax[j]):
				grid[i][j] = num
				rowMax[i].add(num)
				colMax[j].add(num)
				break

for g in grid:
	print(*g)