def solve(len_a, len_b, a, b):



if __name__ == '__main__':
    num_probs = int(input())
    for _ in range(num_probs):
        len_a, len_b = (int(i) for i in input().split())
        a = [int(i) for i in input().split()]
        b = [int(i) for i in input().split()]
        solve(len_a, len_b, a, b)
