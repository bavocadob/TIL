# 어렵게 풀면 다이나믹 프로그래밍인데
# 쉽게풀면 규칙이 있다.

N = int(input())

min_chicken = (N + 1) // 2
max_chicekn = (N // 3) * 2 + 1 if N % 3 == 2 else (N // 3) * 2

print(min_chicken, max_chicekn)
