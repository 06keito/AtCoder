import sys
import os
import shutil
f = open('input.txt', 'r')
sys.stdin = f
#--------------------------
N,Q = map(int,input().split())
board = [0]*(N+1)
ans = [0]*(N+1)
for i in range(Q):
    l,r = map(int,input().split())
    board[l] += 1
    if r+1 != N+1:
        board[r+1] -= 1
for j in range(1,N+1):
    ans[j] += ans[j-1]+board[j]
ans = [a%2 for a in ans]
print("".join(map(str,ans[1:])))
#--------------------------
filename = 'test.py'
out = open(filename,"w")
shutil.copy("code.py",filename)
out.close()
f.close()
