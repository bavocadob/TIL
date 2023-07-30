
def calc_cutting(arr, mid):
    result = 0
    for i in range(len(arr)):
        if arr[i] > mid:
            result += arr[i] - mid
    
    return result




N, M = map(int,input().split())

 
numbers = list(map(int, input().split()))

numbers.sort()



start = 0
end = numbers[-1]

while start <= end:
    mid = (start + end) // 2
    sum_of_cutted = calc_cutting(numbers, mid)
    
    if sum_of_cutted == M:
        print(mid)
        break
    elif sum_of_cutted > M:
        start = mid + 1
    elif sum_of_cutted < M:
        end = mid - 1
else:
    print(end)