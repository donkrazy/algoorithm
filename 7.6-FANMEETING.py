# iterate fan_list to check match
def count(fan_list, member_list):
    ret = 0
    num_member = len(member_list)
    for group in (fan_list[i - num_member: i] for i in range(num_member, len(fan_list) + 1)):
        embarrased = False
        for member, fan in zip(member_list, group):
            if member == 'M' and fan == 'M':
                embarrased = True
                break
        if embarrased:
            continue
        else:
            ret += 1
    return ret


if __name__ == '__main__':
    num_prob = int(input())
    for prob in range(num_prob):
        member_list = list(input())
        fan_list = list(input())
        print(count(fan_list, member_list))
