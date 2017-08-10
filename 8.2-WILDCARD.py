def match(wildcard, file):
    pos = 0
    while pos < len(wildcard) and pos < len(file) and (wildcard[pos] == file[pos] or wildcard[pos] == '?'):
        pos += 1

    # papa^ / papa^
    if pos == len(wildcard) and pos == len(file):
        return True

    # papa^ / papa^dk
    if pos == len(wildcard) and pos < len(file):
        return False

    # pap* / papcvz
    if pos == len(wildcard) - 1 and wildcard[pos] == '*':
        return True

    if wildcard[pos] == '*':
        for j in range(pos, len(file)):
            if match(wildcard[pos + 1:], file[j:]):
                return True
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
