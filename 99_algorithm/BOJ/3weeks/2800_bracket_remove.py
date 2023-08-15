def remove_bracket(depth):
    if depth == len(brackets):
        tmp_str = list(bracket_str)
        remove = False
        for i, char in enumerate(bracket_str):
            if visited[i]:
                tmp_str[i] = ''
                remove = True
        if remove:
            result.add(''.join(tmp_str))
        return

    remove_bracket(depth + 1)

    left, right = brackets[depth]
    visited[left] = True
    visited[right] = True
    remove_bracket(depth + 1)
    visited[left] = False
    visited[right] = False


bracket_str = input()

stack = []
brackets = []

for i, char in enumerate(bracket_str):
    if char == '(':
        stack.append(i)
    elif char == ')':
        left = stack.pop()
        brackets.append((left, i))

visited = [False] * len(bracket_str)

result = set()
remove_bracket(0)


for removed in sorted(result):
    print(removed)
