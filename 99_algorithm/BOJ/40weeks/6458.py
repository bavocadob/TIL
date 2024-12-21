import sys
import math

input = sys.stdin.readline

try:
    while True:
        data = input().strip()
        if not data:
            break

        x1, y1, x2, y2, x3, y3 = map(float, data.split())

        A1, B1, C1 = (x1 + x2) / 2, (y1 + y2) / 2, (x2 - x1) / (y1 - y2)
        A2, B2, C2 = (x2 + x3) / 2, (y2 + y3) / 2, (x3 - x2) / (y2 - y3)

        x = (B2 - B1 + A1 * C1 - A2 * C2) / (C1 - C2)
        y = C1 * (x - A1) + B1

        R = math.sqrt((x1 - x) ** 2 + (y1 - y) ** 2)

        if x > 0:
            print(f"(x - {x:.3f})^2 + ", end="")
        else:
            print(f"(x + {-x:.3f})^2 + ", end="")

        if y > 0:
            print(f"(y - {y:.3f})^2 = {R:.3f}^2")
        else:
            print(f"(y + {-y:.3f})^2 = {R:.3f}^2")

        print("x^2 + y^2 ", end="")

        if x > 0:
            print(f"- {2 * x:.3f}x ", end="")
        else:
            print(f"+ {-2 * x:.3f}x ", end="")

        if y > 0:
            print(f"- {2 * y:.3f}y ", end="")
        else:
            print(f"+ {-2 * y:.3f}y ", end="")

        M = x ** 2 + y ** 2 - R ** 2

        if M > 0:
            print(f"+ {M:.3f} = 0\n")
        else:
            print(f"- {-M:.3f} = 0\n")
except EOFError:
    pass
