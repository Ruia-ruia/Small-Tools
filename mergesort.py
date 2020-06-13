def merge_sort(ls):

    if len(ls) < 2:
        return ls

    solution = []

    mid = int(len(ls) / 2)
    left = merge_sort(ls[:mid])
    right = merge_sort(ls[mid:])

    while len(left) > 0 and len(right) > 0:

        if left[0] < right[0]:
            solution.append(left[0])
            left.pop(0)

        else: 
            solution.append(right[0])
            right.pop(0)

    solution += left 
    solution += right 

    return solution


print(merge_sort([4, 3, 2, 1]))
