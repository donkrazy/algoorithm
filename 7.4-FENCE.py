def draw_line(height_list, y):
    return [True if height >= y else False for height in height_list]

def count_true(TF_list):
    count_list = []
    count = 0
    for TF in TF_list:
        if TF:
            count += 1
        elif not TF and count != 0:
            count_list.append(count)
            count = 0
    count_list.append(count)  # all True
    return max(count_list)


if __name__ == '__main__':
    num_prob = int(input())
    for prob in range(num_prob):
        n = int(input())
        height_list = [int(i) for i in input().split()]
        max_y = max(height_list)
        area_list = []
        for y in range(max_y, 0, -1):
            TF_list = draw_line(height_list, y)
            max_width = count_true(TF_list)
            area_list.append(y * max_width)
        print(max(area_list))
