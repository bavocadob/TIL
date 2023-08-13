N = int(input())
M = int(input())

journey_index = list(map(int, input().split()))
journey = input()

my_dict = dict()
temp_index = 0

for index in sorted(journey_index):
    if index not in my_dict:
        my_dict[index] = temp_index
        temp_index += 1

coordinate_list = [0] * temp_index

my_set = {tuple(coordinate_list)}

for i in range(M):
    if journey[i] == '+':
        coordinate_list[my_dict[journey_index[i]]] += 1
    else:
        coordinate_list[my_dict[journey_index[i]]] -= 1
    temp = tuple(coordinate_list)
    if temp in my_set:
        print(0)
        break
    my_set.add(temp)
else:
    print(1)
