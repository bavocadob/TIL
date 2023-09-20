marks = {'!', '?', ',', '.'}
prefix = 'K-'
for _ in range(int(input())):

    phrase = input().split()
    result = []

    k_stack = 0
    mark = ''
    while phrase:
        word = phrase.pop()

        if word.startswith('Korea') and len(word) == 6 and word[-1] in marks:
            if phrase and phrase[-1] == 'of':
                phrase.pop()
                k_stack += 1
                mark = word[-1]
            else:
                if k_stack == 1:
                    result.append('of Korea' + mark)
                    result.append(word)
                elif k_stack > 1:
                    result.append('of ' + prefix * (k_stack - 1) + 'Korea' + mark)
                    result.append(word)
                else:
                    result.append(word)
                k_stack = 0
                mark = ''
        elif word == 'Korea':
            if phrase and phrase[-1] == 'of':
                phrase.pop()
                k_stack += 1
            else:
                if k_stack:
                    result.append(prefix * k_stack + word + mark)
                    k_stack = 0
                    mark = ''
                elif result:
                    word2 = result.pop()
                    word2 = word2[0].upper() + word2[1:]
                    result.append(prefix + word2)
                else:
                    result.append(word)
        else:
            if word[-1] in marks:
                if k_stack == 1:
                    result.append('of Korea' + mark)
                    result.append(word)
                elif k_stack > 1:
                    result.append('of ' + prefix * (k_stack - 1) + 'Korea' + mark)
                    result.append(word)
                else:
                    result.append(word)
                k_stack = 0
                mark = ''
            elif k_stack:
                word = word[0].upper() + word[1:]
                result.append(prefix * k_stack + word + mark)
                k_stack = 0
                mark = ''
            else:
                result.append(word)

    if k_stack == 1:
        result.append('of Korea' + mark)
    elif k_stack > 1:
        result.append('of ' + prefix * (k_stack - 1) + 'Korea' + mark)

    print(*result[::-1])
