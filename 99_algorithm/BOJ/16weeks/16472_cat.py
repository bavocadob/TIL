from collections import defaultdict

N = int(input())

cat_string = input()
alphabet_dict = defaultdict(int)

left = right = 0
cnt = 0

ans = 0

while right < len(cat_string):
    if cnt <= N:
        if alphabet_dict[cat_string[right]] == 0:
            cnt += 1
        alphabet_dict[cat_string[right]] += 1
        right += 1
    else:
        alphabet_dict[cat_string[left]] -= 1
        if alphabet_dict[cat_string[left]] == 0:
            cnt -= 1
        left += 1

    if cnt <= N:
        ans = max(ans, right - left)

print(ans)
