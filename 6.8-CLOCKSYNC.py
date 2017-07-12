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
condition_dict = {}
for item in switch_info.split('\n')[1:-1]:
    idx_list = [int(i) for i in item[1:].split(',')]
    available = [1 if j in idx_list else 0 for j in range(16)]
    condition_dict[int(item[0])] = available


def check(picked, original):
    # picked = [1,1,1,1,1,1,1,1,1,1,1,1]
    # condition_dict = {1: [0000011], 2:[1110000], ... }
    a = []
    a.append(original)
    for i in range(10):
        k = picked[i]
        ll = [k * j for j in condition_dict[i]]
        a.append(ll)

    f = [sum(i) % 4 for i in zip(*a)]
    if all(v == 0 for v in f):
        print(sum(picked))


def traverse(picked, original):
    if len(picked) == 10:
        check(picked, original)
        return
    for i in range(4):
        picked.append(i)
        traverse(picked, original)
        picked.pop()


num_prob = int(input())
for prob in range(num_prob):
    original = [int(i) / 3 for i in input().split()]
    traverse([], original)

# def check(time_list, depth):
#     if depth == 0:
#         return False

#     for i in range(10):
#         flag = True
#         for clock_idx in switch_list[i]:
#             time_list[clock_idx] += 3
#         for time in time_list:
#             if time % 12 != 0:
#                 flag = False
#         for clock_idx in switch_list[i]:
#             time_list[clock_idx] -= 3
#         if flag:
#             break
# num_prob = int(input())
# for prob in range(num_prob):
#     time_list = [int(i) for i in input().split()]
#     for depth in range(1, 10):
#         check()
#         print(depth)
