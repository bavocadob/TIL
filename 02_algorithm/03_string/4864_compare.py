def search_pattern(text, pattern):
    def make_skip(p):
        skip = {}
        m = len(p)
        for i in range(m - 1):
            skip[p[i]] = m - 1 - i

        return skip

    skip_dict = make_skip(pattern)
    n = len(text)
    m = len(pattern)

    i = m - 1
    while i < n:
        j = m - 1
        while text[i] == pattern[j]:
            if j == 0:
                return True
            i -= 1
            j -= 1
        temp_distance = skip_dict.get(text[i], m)

        i += max(1, temp_distance)

    return False


for T in range(int(input())):
    str1 = input()
    str2 = input()
    print(f'#{T + 1} {int(search_pattern(str2, str1))}')
