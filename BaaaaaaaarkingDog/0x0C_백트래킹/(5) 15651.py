import sys
input = sys.stdin.readline

N, M = map(int, input().split())
path = [] # 현재까지의 경로
used = [False] * (N + 1) # 사용 여부

def backtrack():
  if len(path) == M:
    print(*path)
    return

  for x in range(1, N+1):
    # if used[x] == True: continue
    used[x] = True
    path.append(x)

    backtrack()

    used[x] = False
    path.pop()

backtrack()

