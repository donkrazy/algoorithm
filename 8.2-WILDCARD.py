def match(wildcard, file, cache=None, i=0, j=0):  # default value for initialization
    if cache is None:
        cache = [[-1] * 101 for _ in range(101)]  # -1: unidentified, 0: not match, 1: match

    if cache[i][j] == 1:
        return True
    elif cache[i][j] == 0:
        return False

    while i < len(wildcard) and j < len(file) and (wildcard[i] == file[j] or wildcard[i] == '?'):
        i += 1
        j += 1

    # papa^ / papa^
    # papa^ / papa^dk
    if i == len(wildcard):
        return j == len(file)

    # papa* / papadfa
    # pa*a / pazzzzzza
    if wildcard[i] == '*':
        for k in range(j, len(file) + 1):
            if match(wildcard, file, cache, i + 1, k):
                cache[i][j] = 1
                return True

    cache[i][j] = 0
    return False


def solve(wildcard, files):
    ret = [file for file in files if match(wildcard, file)]
    for file in sorted(ret):
        print(file)


if __name__ == '__main__':
    num_probs = int(input())
    for _ in range(num_probs):
        wildcard = input()
        num_files = int(input())
        files = [input() for _ in range(num_files)]
        solve(wildcard, files)
