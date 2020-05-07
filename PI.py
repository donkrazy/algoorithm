import sys
sys.setrecursionlimit(3334)  # 10000 / 3


# check difficulty of a[idx:dix + diff]
def difficulty(a, idx, diff):
    b = a[idx:idx + diff]
    # case 1
    if len(set(b)) == 1:
        return 1

    # case 2
    if all(b[i] - b[i - 1] == 1 for i in range(1, len(b))) or all(b[i] - b[i - 1] == -1 for i in range(1, len(b))):
        return 2

    # case 3
    if len(set(b)) == 2 and len(set(b[1::2])) == 1 and len(set(b[::2])) == 1:
        return 4

    # case 4
    d = b[1] - b[0]
    if all(b[i] - b[i - 1] == d for i in range(1, len(b))):
        return 5

    # case 5
    return 10


# find min difficulty from a[idx:]
def solve(a, cache, idx):
    if cache[idx] != -1:
        return cache[idx]

    len_a = len(a[idx:])
    if len_a < 3:
        ret = 9999999
    elif len_a >= 3 and len_a <= 5:
        ret = difficulty(a, idx, len_a)
    else:
        ret = min(difficulty(a, idx, 3) + solve(a, cache, idx + 3),
                  difficulty(a, idx, 4) + solve(a, cache, idx + 4),
                  difficulty(a, idx, 5) + solve(a, cache, idx + 5))

    cache[idx] = ret
    return ret


if __name__ == '__main__':
    num_probs = int(input())
    for _ in range(num_probs):
        a = [int(i) for i in list(input())]
        cache = [-1] * len(a)
        print(solve(a, cache, 0))
