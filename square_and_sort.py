def square_and_sort(lst):
    return sorted([x**2 for x in lst])




def square_sort(lst):
    negatives = [x for x in lst if x < 0]
    non_negatives = [x for x in lst if x >= 0]

    negatives_square_sorted = [x ** 2 for x in reversed(negatives)]
    non_negatives_square_sorted = [x ** 2 for x in non_negatives]

    return _merge(negatives_square_sorted, non_negatives_square_sorted)


def _merge(left_lst, right_lst):
    result = []

    i = j = 0
    while i < len(left_lst) and j < len(right_lst):
        if left_lst[i] < right_lst[j]:
            result.append(left_lst[i])
            i += 1
        elif left_lst[i] > right_lst[j]:
            result.append(right_lst[j])    
            j += 1
        else:
            result.append(left_lst[i])
            result.append(right_lst[j])
            j += 1
            i += 1

    result.extend(left_lst[i:])
    result.extend(right_lst[j:])
    return result

print(square_sort([-9, -2, 0, 2, 3]))