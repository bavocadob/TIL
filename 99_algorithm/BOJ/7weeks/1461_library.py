
import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())

location = list(map(int, input().split()))
location.sort()
print(location)
# 22
# 12
# 58
# 39