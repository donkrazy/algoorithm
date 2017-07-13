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
switch_dict = {}
for item in switch_info.split('\n')[1:-1]:
    idx_list = [int(i) for i in item[1:].split(',')]
    available = [1 if j in idx_list else 0 for j in range(16)]
    switch_dict[int(item[0])] = available


def check(picked_list):
    # picked_list = [1,1,1,1,1,1,1,1,1,1,1,1]
    # condition_dict = {1: [0000011], 2:[1110000], ... }
    a = []
    a.append(init_condition)
    for i in range(len(picked_list)):
        k = picked_list[i]
        ll = [k * j for j in switch_dict[i]]
        a.append(ll)

    f = [sum(i) % 4 for i in zip(*a)]
    if all(v == 0 for v in f):
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
