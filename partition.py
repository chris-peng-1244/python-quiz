def partition(lst, x):
    i = 0
    j = 0
    k = len(lst) - 1

    while j < k:
        if lst[j] == x:
            j += 1
        elif lst[j] < x:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j += 1
        else:
            lst[j], lst[k] = lst[k], lst[j]
            k -= 1

    return lst