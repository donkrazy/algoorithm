def narashi(height_list):
    changed = False
    for i in range(len(height_list) - 1):
        left = height_list[i]
        right = height_list[i + 1]
        if left == 0 or right == 0 or left == right:
            continue
        # left != right
        changed = True
        # clean code
        if left > right:  
            area_c = right * 2
            if left > area_c:
                height_list[i + 1] = 0
            else:
                height_list[i] = right
        else:
            area_c = left * 2
            if right > area_c:
                height_list[i] = 0
            else:
                height_list[i + 1] = left
    return changed


def get_area(height_list):
    area_list = []
    return max(area_list)


if __name__ == '__main__':
    num_prob = int(input())
    for prob in range(num_prob):
        n = int(input())
        height_list = [int(i) for i in input().split()]
        while True:
            has_changed = narashi(height_list)
            if not has_changed:
                break
        # max_area = get_area(height_list)
        # print(max_area)
        print(height_list)
        