def duplicate1(lst):
    i = 0
    while i < len(lst):
        if lst[i] != i:
            j = lst[i]
            if lst[j] == lst[i]:
                return j
            lst[i], lst[j] = lst[j], lst[i]
        else:
            i += 1
    raise IndexError("Malformed input.") 

def duplicate2(lst):
    n = len(lst) - 1
    return sum(lst) - (n * (n+1)//2)