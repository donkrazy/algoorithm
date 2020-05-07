# find jlis starting from A[i:] and B[j:]
def jlis(i, j, A, B, cache):
    # print('jlis:', i, j)
    if cache[i + 1][j + 1] != -1:
        return cache[i + 1][j + 1]
    ret = 2
    a = -999999 if i == -1 else A[i]
    b = -999999 if j == -1 else B[j]
    bigger = max(a, b)
    for ii in range(i + 1, len(A)):
        if A[ii] > bigger:
            ret = max(ret, 1 + jlis(ii, j, A, B, cache))
    for jj in range(j + 1, len(B)):
        if B[jj] > bigger:
            ret = max(ret, 1 + jlis(i, jj, A, B, cache))
    cache[i + 1][j + 1] = ret
    return ret


def find_max(A, B, len_a, len_b):
    cache = [[-1] * (len_b + 1) for _ in range(len_a + 1)]
    ret = jlis(-1, -1, A, B, cache)
    print(cache, ret - 2)


if __name__ == '__main__':
    num_probs = int(input())
    for _ in range(num_probs):
        len_a, len_b = (int(i) for i in input().split())
        A = [int(i) for i in input().split()]
        B = [int(i) for i in input().split()]
        find_max(A, B, len_a, len_b)
