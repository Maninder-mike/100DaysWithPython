from algorithms.check_time import run_algorithm


def insertion_sort(num):
    for x in range(1, len(num)):
        major_item = num[x]
        y = x - 1

        while y >= 0 and num[y] > major_item:
            num[y+1] = num[y]

            y -= 1
            num[y+1] = major_item
    return num


m = [-5, -1, -3.5, 4.5, 4, 8, 4.16, 88, 6, 78, 8.2, 76, 46, 84, 546, 89, 41, 4.56]

print(run_algorithm("insertion_sort", m))
