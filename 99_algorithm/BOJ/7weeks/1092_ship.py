import sys

input = sys.stdin.readline

N = int(input())

cranes = list(map(int, input().split()))
cranes.sort(reverse=True)

M = int(input())

boxes = list(map(int, input().split()))
boxes.sort(reverse=True)

ans = 0

if boxes[0] > cranes[0]:
    print(-1)
else:
    while boxes:
        ans += 1
        idx = 0
        for crane in cranes:
            while idx < len(boxes):
                box = boxes[idx]
                if crane >= box:
                    boxes[idx] = None
                    idx += 1
                    break
                idx += 1

        boxes = [x for x in boxes if x is not None]

    print(ans)
