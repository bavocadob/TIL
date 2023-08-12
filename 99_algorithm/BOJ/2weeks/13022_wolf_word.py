def valid_word(word_stack, word_dict):
    if ''.join(word_stack) == 'wolf' and word_dict['w'] == word_dict['o'] == word_dict['l'] == word_dict['f']:
        return True
    return False


input_string = input()

stack = []

word_count = {'w': 0, 'o': 0, 'l': 0, 'f': 0}


for char in input_string:
    if stack:  # 스택이 비지 않았을때
        if char == stack[-1]:  # 스택 마지막글자와 같은게 주어지면 word_count가 오른다
            stack.pop()
        else:
            if stack[-1] == 'f' and char == 'w':  # 문장이 새로 시작되면 검증을 시작한다.
                if valid_word(stack,word_count):
                    stack.clear()
                    word_count = {'w': 0, 'o': 0, 'l': 0, 'f': 0}
                else:
                    print(0)
                    break
    stack.append(char)
    word_count[char] += 1
else:  # for문이 다끝났을때 검증한다.
    print(int(valid_word(stack, word_count)))
