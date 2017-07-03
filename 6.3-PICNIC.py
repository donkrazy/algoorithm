def make_combinations(topick, picked, ret):
    if len(topick) == 0:
        ret.append(picked)
        return
    i = topick[0]
    for j in topick[1:]:
        picked_copy = picked.copy()
        picked_copy.append({i, j})
        topick_copy = [k for k in topick[1:] if k != j]
        make_combinations(topick_copy, picked_copy, ret)


c = int(input())
for prob in range(c):
    # generate dataset
    n, m = (int(i) for i in input().split())
    pairs_available = []
    make_combinations(list(range(n)), [], pairs_available)
    data = [int(i) for i in input().split()]
    table = [set(i) for i in (zip(data[0::2], data[1::2]))]

    # test
    count = 0
    for pair_list in pairs_available:
        flag = True
        for pair in pair_list:
            if pair not in table:
                flag = False
                break

        if flag:
            count += 1
    print(count)
