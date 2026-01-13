import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
x = int(input())

visited = [False] * 1_000_001
cnt = 0

for i in arr:
    t = x - i
    if 0 <= t <= 1_000_000 and visited[t]:
        cnt += 1
    visited[i] = True
  
print(cnt)
