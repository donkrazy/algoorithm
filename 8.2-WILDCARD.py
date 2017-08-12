def match(wildcard, file, i, j):
    ret = cache(i, j)
    while i < len(wildcard) and j < len(file) and (wildcard[i] == file[j] or wildcard[i] == '?'):
        i += 1
        j += 1

    # papa^ / papa^
    if i == len(wildcard) and j == len(file):
        return True

    # papa^ / papa^dk
    if i == len(wildcard) and j < len(file):
        return False

    # pap* / papcvz
    if i == len(wildcard) - 1 and wildcard[i] == '*':
        return True

    if wildcard[i] == '*':
        for k in range(i, len(file)):
            if match(wildcard[i + 1:], file[k:]):
                return True
    return False


def solve(wildcard, files, cache):
    cache = [[-1] * 100 for _ in range(100)]
    ret = [file for file in files if match(wildcard, file, 0, 0)]
    for file in sorted(ret):
        print(file)


if __name__ == '__main__':
    num_probs = int(input())
    for _ in range(num_probs):
        wildcard = input()
        num_files = int(input())
        files = [input() for _ in range(num_files)]
        solve(wildcard, files)
