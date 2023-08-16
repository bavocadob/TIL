def solution(depth):
    global result

    if depth == N:
        result += 1
        return

    for i in range(N):
        check[depth] = i
        valid = True
        for j in range(depth):
            if check[j] == check[depth] or (abs(check[j] - check[depth]) == abs(depth - j)):
                valid = False
                break
        if valid:
            solution(depth + 1)


N = int(input())
result = 0

check = [None] * N
solution(0)
print(result)
