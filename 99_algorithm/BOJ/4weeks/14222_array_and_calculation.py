def solution(arr, k, target):
    curr = 1
    idx = 0
    while True:
        if idx == target:
            break
        if arr[idx] == curr:
            curr += 1
            idx += 1
        else:
            arr[idx] += k
            arr.sort()
            if arr[idx] > curr:
                return 0

    return 1


N, K = map(int, input().split())

numbers = list(map(int, input().split()))

numbers.sort()

print(solution(numbers, K, N))
