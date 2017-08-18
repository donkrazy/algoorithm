# find jlis starting from A[i:] and B[j:]
def jlis(i, j, A, B, cache):
    if cache[i][j] != -1:
        return cache[i][j]
    ret = 2
    bigger = max(A[i], B[j])
    for ii in range(i + 1, len(A)):
        if A[ii] > bigger:
            ret = max(ret, 1 + jlis(ii, j, A, B, cache))
    for jj in range(j + 1, len(B)):
        if B[jj] > bigger:
            ret = max(ret, 1 + jlis(i, jj, A, B, cache))
    cache[i][j] = ret
    return ret


def find_max(A, B, len_a, len_b):
    cache = [[-1] * len_b for _ in range(len_a)]
    ret = 0
    for i in range(len_a):
        for j in range(len_b):
            ret = max(ret, jlis(i, j, A, B, cache))
    print(cache, ret)
    # print(ret)


if __name__ == '__main__':
    num_probs = int(input())
    for _ in range(num_probs):
        len_a, len_b = (int(i) for i in input().split())
        A = [int(i) for i in input().split()]
        B = [int(i) for i in input().split()]
        find_max(A, B, len_a, len_b)
