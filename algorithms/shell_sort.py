from Algorithms.check_time import run_algorithm


def shell_sort(num):
    gap = len(num) // 2
    while gap > 0:
        for index in range(gap, len(num)):
            current_element = num[index]
            pos = index
            while pos >= gap and current_element < num[pos - gap]:
                num[pos] = num[pos - gap]
                pos -= gap
            num[pos] = current_element
        gap = gap // 2
    return num


list_1 = [5, 68, 4, .54, 64.7, 5.4, 68, 75, -4, 89, 65, 45, 44]

print(shell_sort(list_1))
print(run_algorithm('shell_sort', list_1))
