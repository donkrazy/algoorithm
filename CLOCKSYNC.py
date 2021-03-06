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
switch_list = [None] * 10
for item in switch_info.split('\n')[1:-1]:
    switch_idx = int(item[0])
    switch_target = [int(i) for i in item[1:].split(',')]
    switch_list[switch_idx] = switch_target


INF = 99999
SWITCHES = 10


def are_aligned(clocks):
    if all(clock % 4 == 0 for clock in clocks):
        return True
    return False


def push_switch(clocks, switch_idx):
    for clock_idx in switch_list[switch_idx]:
        clocks[clock_idx] += 1


def solve(clocks, switch_idx=0):
    if switch_idx == SWITCHES:
        return 0 if are_aligned(clocks) else INF

    ret = INF
    for count in range(4):
        ret = min(ret, count + solve(clocks, switch_idx + 1))
        push_switch(clocks, switch_idx)
    return ret


num_prob = int(input())
for prob in range(num_prob):
    clocks = [int(i) / 3 for i in input().split()]
    result = solve(clocks)
    print(result if result < INF else -1)
