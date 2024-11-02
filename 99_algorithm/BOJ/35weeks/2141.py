from math import ceil
import sys

input = sys.stdin.readline
N = int(input())

village = []

all_pop = 0
for _ in range(N):
    pos, pop = map(int, input().split())
    village.append((pos, pop))
    all_pop += pop

village.sort()

temp = 0

for pos, pop in village:
    temp += pop
    if temp >= ceil(all_pop / 2):
        print(pos)
        break
