N = int(input())

men = list(map(int, input().split()))
women = list(map(int, input().split()))

men.sort()
women.sort()

men_left = women_left = 0
men_right = women_right = N - 1

ans = 0

while men_left < N and men[men_left] < 0:
    while women_right >= 0 and women[women_right] > 0:
        if women[women_right] < abs(men[men_left]):
            ans += 1
            women_right -= 1
            break
        else:
            women_right -= 1
    men_left += 1

while women_left < N and women[women_left] < 0:
    while men_right >= 0 and men[men_right] > 0:
        if men[men_right] < abs(women[women_left]):
            ans += 1
            men_right -= 1
            break
        else:
            men_right -= 1
    women_left += 1

print(ans)
