# import sys

# data = sys.stdin.read().split()
# n = int(data[0])
# heights = list(map(int, data[1:1+n]))

# # 5 6 9 5 4 3
# # 0 1 2 3 4 5

# stack = []
# out = []
# idx = n

# # (인덱스, 높이)
# for x in reversed(heights):
#   # 스택이 비어있고, 
#   while stack and stack[-1][1] < x:
#     stack.pop()
    
#   if stack and stack[-1][1] > x:
#     if stack[-1][0] == n:
#       out.append(n - idx)
#     else:
#       out.append(stack[-1][0] - idx - 1)
#   else:
#     out.append(0)
  
#   stack.append((idx, x))
#   idx -= 1

# # print(" ".join(out))
# print(f"debug {out}")
# print(sum(out))


import sys

data = sys.stdin.read().split()
n = int(data[0])
heights = list(map(int, data[1:1+n]))

stack = []   # (idx, height, seen)  seen = 이 건물이 볼 수 있는 오른쪽 낮은 건물 수
out = []
idx = n

for x in reversed(heights):
    cnt = 0

    # 나(x)보다 낮은 건물들은 "내가 볼 수 있으니" 전부 흡수(pop)한다
    while stack and stack[-1][1] < x:
        cnt += 1 + stack[-1][2]   # 그 건물 1개 + 그 건물이 보던 것까지
        stack.pop()

    out.append(cnt)               # 이게 바로 현재 건물의 '보이는 개수'
    stack.append((idx, x, cnt))   # 현재 건물도 후보로 저장
    idx -= 1

print(sum(out))