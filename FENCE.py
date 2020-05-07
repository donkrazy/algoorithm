def solve(left, right):
    # base case
    if left == right:
        return height_list[left]

    # left max, right max area
    mid = int((left + right) / 2)
    ret = max(solve(left, mid), solve(mid + 1, right))

    # center rectangle area width=2
    i, j = mid, mid + 1
    height = min(height_list[i], height_list[j])
    ret = max(ret, height * 2)

    # expand center rectangle
    while left < i or j < right:
        if j < right and (i == left or height_list[i - 1] < height_list[j + 1]):
            j += 1
            height = min(height, height_list[j])
        else:
            i -= 1
            height = min(height, height_list[i])
        ret = max(ret, height * (j - i + 1))
    return ret


if __name__ == '__main__':
    num_prob = int(input())
    for prob in range(num_prob):
        n = int(input())
        height_list = [int(i) for i in input().split()]
        print(solve(0, n - 1))
