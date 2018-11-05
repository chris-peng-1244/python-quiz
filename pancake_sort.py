def pancake_sort(lst):
    for size in reversed(range(len(lst))):
        max_ind = max_pos(lst[:size+1])
        reverse(lst, 0, max_ind)
        reverse(lst, 0, size)

    return lst

def max_pos(lst):
    return lst.index(max(lst))

def reverse(lst, i, j):
    while i < j:
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1

pancake_sort([3,2,4,6,7,1])