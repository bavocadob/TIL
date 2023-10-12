import sys

input = sys.stdin.readline


def insert(parent, child, file_type):
    if child not in folders:
        folders[child] = set()

    if parent not in folders:
        folders[parent] = set()

    folders[parent].add((child, file_type))


def merge(from_folder, to_folder):
    folders[to_folder].update(folders[from_folder])
    del folders[from_folder]


def query(folder_name):
    if folder_name in dp:
        return dp[folder_name]

    file_types = set()
    file_cnt = 0

    for file_name, file_type in folders[folder_name]:
        if file_type:  # 파일이 폴더인 경우
            if file_name not in folders:
                continue
            child_file_type, child_file_cnt = query(file_name)
            file_types.update(child_file_type)
            file_cnt += child_file_cnt
        else:  # 파일이 그냥 파일인 경우
            file_types.add(file_name)
            file_cnt += 1

    dp[folder_name] = (file_types, file_cnt)
    return dp[folder_name]


N, M = map(int, input().split())

folders = {'main': set()}
dp = dict()
for _ in range(N + M):
    a, b, c = input().rstrip().split()
    insert(a, b, int(c))

K = int(input())

for _ in range(K):
    a, b = input().rstrip().split()
    a = a.split('/')[-1]
    b = b.split('/')[-1]
    merge(a, b)

Q = int(input())

for _ in range(Q):
    a = input().rstrip().split('/')[-1]
    types, files = query(a)
    print(len(types), files)
