import sys
sys.stdin = open('input.txt')

def recur(idx, arr):
    global result

    if idx == 12:

        if len(arr) == N and sum(arr) == K:
            print(arr)
            result += 1
        return
    arr.append(nums[idx])
    recur(idx+1, arr)

    arr.pop()
    recur(idx+1, arr)

T = int(input())

for tc in range(1, T+1):

    N, K = map(int, input().split())
    nums = list(range(1, 13))
    result = 0
    recur(0, [])
    print(result)