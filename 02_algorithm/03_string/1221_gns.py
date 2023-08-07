import sys
sys.stdin = open('input.txt')

i = input
a=["ZRO","ONE","TWO","THR","FOR","FIV","SIX","SVN","EGT","NIN"]
for t in range(int(i())):
    i()
    s = i()
    print(f'#{t+1}')
    for o in a:
        print((o+' ')*s.count(o))
