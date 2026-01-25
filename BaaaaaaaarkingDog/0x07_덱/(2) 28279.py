import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
dq = deque()
out = []

for _ in range(n):
    cmd = input().split()

    op = cmd[0]
    if op == "1":
        dq.appendleft(cmd[1])
    elif op == "2":
        dq.append(cmd[1])
    elif op == "3":
        out.append(dq.popleft() if dq else "-1")
    elif op == "4":
        out.append(dq.pop() if dq else "-1")
    elif op == "5":
        out.append(str(len(dq)))
    elif op == "6":
        out.append("0" if dq else "1")
    elif op == "7":
        out.append(dq[0] if dq else "-1")
    elif op == "8":
        out.append(dq[-1] if dq else "-1")

print("\n".join(out))