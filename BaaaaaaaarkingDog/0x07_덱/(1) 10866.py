import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
dq = deque()
out = []

for _ in range(n):
    cmd = input().split()

    op = cmd[0]
    if op == "push_front":
        dq.appendleft(cmd[1])
    elif op == "push_back":
        dq.append(cmd[1])
    elif op == "pop_front":
        out.append(dq.popleft() if dq else "-1")
    elif op == "pop_back":
        out.append(dq.pop() if dq else "-1")
    elif op == "size":
        out.append(str(len(dq)))
    elif op == "empty":
        out.append("0" if dq else "1")
    elif op == "front":
        out.append(dq[0] if dq else "-1")
    elif op == "back":
        out.append(dq[-1] if dq else "-1")

print("\n".join(out))