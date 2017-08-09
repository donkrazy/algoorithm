def match(wildcard, file):
    pos = 0
    while pos < len(wildcard) and pos < len(file) and (wildcard[pos] == file[pos] or wildcard[pos] == '?'):
        pos += 1
    if pos == len(wildcard):
        if pos == len(file):
            return True
        else:
            return False

    if pos == len(file):
        if wildcard[pos] == '*':
            return True

    if wildcard[pos] == '*':
        for j in range(pos, len(file) - 1):
            if match(wildcard[pos + 1:], file[j:]):
                return True
    return False


def solve(wildcard, files):
    print('input:', wildcard, files)
    for file in files:
        if not match(wildcard, file):
            files.remove(file)
    for file in sorted(files):
        print(file)


if __name__ == '__main__':
    num_probs = int(input())
    for _ in range(num_probs):
        wildcard = input()
        num_files = int(input())
        files = [input() for _ in range(num_files)]
        solve(wildcard, files)
