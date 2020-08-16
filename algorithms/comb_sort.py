
# TODO "This code is not working yet."

def getNextGap(gap):
    gap = (gap * 10) / 13
    if gap < 1:
        return 1
    return gap


def comb_sort(nums):
    shrink_fact = 1.3
    gaps = len(nums)
    swapped = True
    i = 0

    while gaps > 1 or swapped:
        gaps = int(float(gaps) / shrink_fact)
        swapped = False
        i = 0

        while gaps + 1 < len(nums):
            if nums[i] > nums[i + gaps]:
                nums[i], nums[i + gaps] = nums[i + gaps], nums[i]
                swapped = True
            i += 1
    return nums


m = [-5, -1, -3, 5, 4, 8, 4, 88, 6, 78, 8, 76, 46, 84, 546, 89, 41, 56]
