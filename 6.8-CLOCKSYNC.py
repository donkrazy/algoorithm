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


def check(picked_list, init_condition):
    # y = ax + b
    y = []
    y.append(init_condition)
    for i in range(len(picked_list)):
        k = picked_list[i]
        ll = [k * j for j in switch_dict[i]]
        y.append(ll)

    y = [sum(i) % 4 for i in zip(*y)]
    if all(v == 0 for v in y):
        ans.append(sum(picked_list))
        return True
    return False


def generate_list(picked_list=None):
    if picked_list is None:
        picked_list = []

    if len(picked_list) == 10:
        available_list.append(list(picked_list))
        return

    for i in range(4):
        picked_list.append(i)
        generate_list(picked_list)
        picked_list.pop()


available_list = []
generate_list()


num_prob = int(input())
for prob in range(num_prob):
    ans = []
    init_condition = [int(i) / 3 for i in input().split()]
    for item in available_list:
        if check(item, init_condition):
            ans.append(sum(item))
    print(min(ans) if len(ans) != 0 else -1)
