import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = list(map(int, input().split()))
board.sort()

used = [False] * (board[-1] + 1)
path = []

def backtrack():
  if len(path) == M:
    print(*path)
    return
  
  for x in board:
    if used[x] == True: continue
    used[x] = True
    path.append(x)

    backtrack(x)

    used[x] = False
    path.pop()

backtrack(start)