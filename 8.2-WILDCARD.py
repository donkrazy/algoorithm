def match(wildcard, file):
    ret = True

    # case 1: only '?'
    if '*' not in wildcard:
        if len(wildcard) != len(file):
            return False
        for i in range(len(wildcard)):
            if wildcard[i] == '?':
                continue
            elif wildcard[i] != file[i]:
                return False

    # case 2: only '*':
    if '?' not in wildcard:
        for i in range(len(wildcard)):
            if wildcard[i] == '*':
                for j in range(i, len(file[i:]) - 1):
                    if wildcard[i + 1] == file[j]:
                        break
                ret = match(wildcard[i + 1:], file[j + 1:])
            elif wildcard[i] != file[i]:
                return False
    return ret


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
