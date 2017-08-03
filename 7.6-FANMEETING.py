def solve(a, b):
    # 1) multiply with 'b' reversed, without rounding up
    c = [0] * (len(a) + len(b) - 1)
    b.reverse()
    for i in range(len(a)):
        for j in range(len(b)):
            # c[i + j] += a[i] * b[j]
            c[i + j] |= a[i] & b[j]  # boolean version

    # 2) count 0 in c except for a partial hug
    count = 0
    for k in c[len(a) - 1:len(c) - len(a) + 1]:
        if k == 0:
            count += 1
    return count


if __name__ == '__main__':
    num_prob = int(input())
    for prob in range(num_prob):
        # member_list = [1 if i == 'M' else 0 for i in input()]
        # fan_list = [1 if i == 'M' else 0 for i in input()]
        member_list = [True if i == 'M' else False for i in input()]  # boolean version
        fan_list = [True if i == 'M' else False for i in input()]  # boolean version
        print(solve(member_list, fan_list))
