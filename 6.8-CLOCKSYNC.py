from itertools import starmap
from operator import mul

switch_info = '''
0   0, 1, 2
1   3, 7, 9, 11
2   4, 10, 14, 15
3   0, 4, 5, 6, 7
4   6, 7, 8, 10, 12
5   0, 2, 14, 15
6   3, 14, 15
7   4, 5, 7, 14, 15
8   1, 2, 3, 4, 5
9   3, 4, 5, 9, 13
'''
switch_list = []
for item in switch_info.split('\n')[1:-1]:
    idx_list = [int(i) for i in item[1:].split(',')]
    available = [1 if j in idx_list else 0 for j in range(16)]
    switch_list.append(available)


def check(picked_list):
    # y = ax + b
    # switch_list = [[0000111122223333], [1111222233330000], ... ]    # 10 by 16
    # picked_list = [1,1,1,1,1,1,1,1,1,1,1,1]   # 10 by 1
    # inner_product = switch_list (dot) picked_list   # 16 by 1
    # y = inner_product + init_condition  # 16 by 1
    inner_product = [sum(starmap(mul, zip(picked_list, col))) for col in zip(*switch_list)]
    y = [sum(i) % 4 for i in zip(inner_product, init_condition)]

    if all(v == 0 for v in y):
        ans.append(sum(picked_list))
        return True
    return False


def traverse(picked_list):
    has_found = False
    if len(picked_list) == 10:
        has_found = check(picked_list)
        return has_found

    for i in range(4):
        picked_list.append(i)
        has_found |= traverse(picked_list)
        picked_list.pop()
    return has_found


num_prob = int(input())
for prob in range(num_prob):
    ans = []
    init_condition = [int(i) / 3 for i in input().split()]
    if traverse([]):
        print(min(ans))
    else:
        print(-1)
