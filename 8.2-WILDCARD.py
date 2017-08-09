def match(wildcard, file):
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
        return False

    return True


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
        break
