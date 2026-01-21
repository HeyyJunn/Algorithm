# Silver 4

# 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# 명령은 총 다섯 가지이다.

# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.


import sys
input = sys.stdin.readline

n = int(input())
stack = []
out = []

for _ in range(n):
  cmd = input().split()

  if cmd[0] == "push":
    stack.append(int(cmd[1]))
  elif cmd[0] == "pop":
    out.append(str(stack.pop()) if stack else "-1")
  elif cmd[0] == "size":
    out.append(str(len(stack)))
  elif cmd[0] == "empty":
    out.append("1" if len(stack) == 0 else "0")
  elif cmd[0] == "top":
    out.append(str(stack[-1]) if stack else "-1")

print("\n".join(out))