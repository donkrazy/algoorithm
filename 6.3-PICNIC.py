import itertools


def make_pair(n):
    ret = []
    perm_list = itertools.permutations(range(n))
    for perm in perm_list:
        perm = list(zip(perm[0::2], perm[1::2]))
        ret.append(perm)
    return ret


c = int(input())
for prob in range(c):
    # generate dataset
    n, m = (int(i) for i in input().split())
    pairs_available = make_pair(n)
    data = [int(i) for i in input().split()]
    table = list(zip(data[0::2], data[1::2]))

    # test
    count = 0
    for pair_list in pairs_available:
        flag = True
        for pair in pair_list:
            if pair not in table:
                flag = False
                break

        if flag:
            print(pair_list)
            count += 1

    print(count)
