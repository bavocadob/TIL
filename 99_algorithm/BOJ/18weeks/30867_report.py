L, N = map(int, input().split())

word = list(input().rstrip())
wh = set()

for i in range(L - 1):
    if word[i] == 'w' and word[i + 1] == 'h':
        wh.add((i, i + 1))

for _ in range(N):

    if not wh:
        break

    temp_w = []
    temp_h = []
    for w, h in wh:
        word[w], word[h] = word[h], word[w]

        temp_w.append(h)
        temp_h.append(w)
    wh = set()
    for w in temp_w:
        if w < L - 1 and word[w + 1] == 'h':
            wh.add((w, w + 1))
    for h in temp_h:
        if h > 0 and word[h - 1] == 'w':
            wh.add((h - 1, h))

print(''.join(word))
