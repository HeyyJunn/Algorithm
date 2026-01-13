import sys
input = sys.stdin.readline

word = input().strip()

ans_list = [0] * 26

for i in word:
  ans_list[ord(i) - 97] += 1

print(*ans_list)