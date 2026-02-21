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

Q = []

for t in range(int(I())):
    Q.append(mpi())

for num_cards,a,b in Q:
    if a + b > num_cards:
        print('NO')
        continue

    if a == 0 and b == 0:
        print('YES')
        print(*range(1,num_cards+1))
        print(*range(1,num_cards+1))
        continue

    if a == 0 or b == 0:
        print('NO')
        continue

    c1,c2 = [i for i in range(1,num_cards+1)],[]
    for i in range(a+1,a+b+1):
        c2.append(i)
    for i in range(1,a+1):
        c2.append(i)
    for i in range(a+b+1,num_cards+1):
        c2.append(i)
    print('YES')
    print(*c1)
    print(*c2)
