# 부동산 경매
# 10246번
# 이것도 브루트포스로?


size = 1000000
arr = [0] * 1000001
acc = [0] * 1000001
sum = 0
for i in range(1,len(acc)):
    sum +=i
    acc[i] = sum
    for j in range(i-1,0,-1):
        if acc[i] - acc[j] <= size:
            arr[acc[i] - acc[j]]+=1
        else:
            break

# while True:
#     n = int(input())
#     if n ==0:
#         exit()
#     print("%d\n" %arr[n])

print(acc[:100])
print(arr[:100])