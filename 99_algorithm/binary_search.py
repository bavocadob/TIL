# 반복문으로 이진탐색 구현

def binary_search(arr, target, start, end):
    
    while start <= end:
        mid = (start + end) // 2
        
        # 찾았을 때 인덱스 반환
        if arr[mid] == target:
            return mid
        # 중간값이 더 크면 인덱스의 오른쪽을 줄임
        elif arr[mid] > target:
            end = mid - 1
        # 중간값이 더 작으면 인덱스의 왼쪽을 올림
        elif arr[mid] < target:
            start = mid + 1
    
    return -1


if __name__ == "__main__":
    # n(원소의 개수)과 target(찾고자 하는 대상) 입력받기
    n, target = list(map(int, input().split()))

    # 전체 원소 입력받기
    array = list(map(int, input().split()))

    # 이진탐색하고 수행 결과 출력하기
    result = binary_search(array, target, 0, n - 1)
    print(result)