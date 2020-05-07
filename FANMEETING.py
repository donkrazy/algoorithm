def multiply(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i in range(len(a)):
        for j in range(len(b)):
            c[i + j] += a[i] * b[j]
    return c


# a += b * 10^k
def add(a, b, k=0):
    for i in range(k):
        a.append(0)
    j = 0
    if len(a) < len(b):
        return add(b, a)
    for i in b[::-1]:
        if i == 0:
            continue
        j -= 1
        a[j] += i
    return a


# a -= b
def subtract(a, b):
    j = 0
    for i in b[::-1]:
        if i == 0:
            continue
        j -= 1
        a[j] -= i


def normalize(a):
    for i in range(len(a) - 1, 1, -1):  # omit prepend
        if a[i] >= 10:
            a[i - 1] += int(a[i] / 10)
            a[i] = a[i] % 10
        elif a[i] < 0:
            borrow = int((abs(a[i]) + 9) / 10)
            a[i - 1] -= borrow
            a[i] += borrow * 10


def karatsuba(a, b):
    # 1) base cases
    if len(a) < len(b):
        return karatsuba(b, a)
    if len(a) == 0 or len(b) == 0:
        return []
    if len(a) <= 50:
        return multiply(a, b)

    # 2) split: a = a0 + a1; b = b0 + b1;
    half = int(len(a) / 2)
    a0 = a[:half]
    a1 = a[half:]
    b0 = b[:min(half, len(b))]
    b1 = b[min(half, len(b)):]

    # 3) z0 = a0 * b0; z2 = a1 * b1;
    #    z1 = (a0 + a1) * (b0 + b1) - z0 - z2;
    z0 = karatsuba(a0, b0)
    z2 = karatsuba(a1, b1)
    z1 = karatsuba(add(a0, a1), add(b0, b1))
    subtract(z1, z0)
    subtract(z1, z2)

    # 4) a * b = z0 + z1 * 10^n + z2 * 10 ^ 2n
    c = add(add(z0, z1, half), z2, 2 * half)
    return c


def solve(fan_list, member_list_reversed):
    # count 0 in c except for a partial hug
    count = 0
    c = karatsuba(fan_list, member_list_reversed)
    for k in c[len(member_list_reversed) - 1:len(fan_list)]:
        if k == 0:
            count += 1
    return count


if __name__ == '__main__':
    num_prob = int(input())
    for prob in range(num_prob):
        member_list_reversed = [1 if i == 'M' else 0 for i in input()[::-1]]
        fan_list = [1 if i == 'M' else 0 for i in input()]
        print(solve(fan_list, member_list_reversed))
