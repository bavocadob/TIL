import sys

input = sys.stdin.readline
K = int(input())

for case_num in range(1, K + 1):
    n = int(input())
    tasks = []

    for _ in range(n):
        temp = input().split()
        t = int(temp[0])
        p = float(temp[1])
        dependencies = [int(dep) - 1 for dep in temp[2:]]
        tasks.append((t, p, dependencies))

    max_state = 1 << n
    best = tasks[-1][1]

    for state in range(max_state):
        total_prob = sum(tasks[k][1] for k in range(n) if state & (1 << k))
        if total_prob >= best:
            continue

        safe = 0
        for k in range(n):
            if state & (1 << k):
                safe |= 1 << k
                continue

            remaining_time = tasks[k][0]
            for dep in tasks[k][2]:
                if not (safe & (1 << dep)):
                    remaining_time -= 1

            if remaining_time > 0:
                safe |= 1 << k

        if safe & (1 << (n - 1)):
            best = total_prob

    print(f"Data Set {case_num}:\n{best:.2f}\n")
