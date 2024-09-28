x1, y1, x2, y2 = map(int, input().split())

ans = 0

#  y가 1, 3, 5, 7, 9 일때 높이가 2, 4, 6, 8, 10
y_start = y1 + 1 if y1 % 2 == 1 else y1 + 2

for i in range(y_start, y2 + 1, 2):
    # i는 0부터 기둥 있는 높이
    # i칸 까지 기둥이 있는데 그중 x1~x2까지만 잘라 쓰겠다.
    ans += max(0, min(i, x2) - x1)

#  x가 1, 3, 5, 7, 9 일때 높이가 1, 3 ,5 ,7 ,9
x_start = x1 if x1 % 2 == 1 else x1 + 1

for i in range(x_start, x2, 2):
    ans += max(0, min(i, y2) - y1)

print(ans)
