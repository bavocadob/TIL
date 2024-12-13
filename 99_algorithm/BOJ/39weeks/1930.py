import sys

input = sys.stdin.readline
face_mapping_a = [1, 0, 0, 0]
face_mapping_b = [2, 3, 1, 2]
face_mapping_c = [3, 2, 3, 1]


def rotate_face(face):
    return face[1:] + face[:1]


def solve(a, b):
    for i in range(4):
        base_1 = a[i]
        sides_1 = [
            a[face_mapping_a[i]],
            a[face_mapping_b[i]],
            a[face_mapping_c[i]]
        ]

        for j in range(4):
            base_2 = b[j]
            sides_2 = [
                b[face_mapping_a[j]],
                b[face_mapping_b[j]],
                b[face_mapping_c[j]]
            ]

            if base_1 == base_2:
                for _ in range(3):
                    if sides_1 == sides_2:
                        return 1
                    sides_2 = rotate_face(sides_2)

    return 0


T = int(input())

for _ in range(T):
    line = input().split()
    A, B = line[:4], line[4:]
    print(solve(A, B))
