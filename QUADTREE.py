def reverse(a):
    head = a.pop(0)
    if head == 'w' or head == 'b':
        return head
    ul, ur, ll, lr = (reverse(a) for i in range(4))
    return 'x' + ll + lr + ul + ur


if __name__ == '__main__':
    num_prob = int(input())
    for prob in range(num_prob):
        print(reverse(list(input())))
