from algorithms.bubble_sort import run_algorithm


def bubble_sort(num):
    for x in range(len(num)):
        for y in range(len(num) - x - 1):
            if num[y] > num[y + 1]:
                num[y], num[y + 1] = num[y + 1], num[y]
                already_sorted = False

                if already_sorted:
                    break
    return num


m = [-5, -1, -3.5, 4.5, 4, 8, 4.16, 88, 6, 78, 8, 76, 46, 84, 546, 89, 41, 4.56]

print(run_algorithm('bubble_sort', m))
