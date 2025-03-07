import sys

input = sys.stdin.readline


def solve(plaques):
    box_count = 1
    current_height = plaques[0][1]

    for i in range(1, n):
        min_overlap = float('inf')

        for j in range(w):
            overlap = plaques[i - 1][2][j] + plaques[i][3][j]
            min_overlap = min(min_overlap, overlap)

        if current_height + plaques[i][1] - min_overlap <= b:
            current_height += plaques[i][1] - min_overlap
        else:
            print(current_height, end=' ')
            current_height = plaques[i][1]
            box_count += 1

    print(current_height)


n, w, b = map(int, input().split())

p = []
for _ in range(n):
    h = int(input())
    shape = [input().strip() for _ in range(h)]

    top, bottom = [0] * w, [0] * w

    for j in range(w):
        top[j] = next((k for k in range(h) if shape[k][j] != '.'), h)
        bottom[j] = next((k for k in range(h - 1, -1, -1) if shape[k][j] != '.'), -1)
        bottom[j] = h - bottom[j] - 1

    p.append((w, h, top, bottom))

solve(p)
