def majority(elements):
    element_to_count = {}
    for element in elements:
        if element not in element_to_count:
            element_to_count[element] = 0
        element_to_count[element] += 1
    return max(element_to_count, key=element_to_count.get)

def majority_voting(elements):
    count = 0
    for i, e in enumerate(elements):
        if i == 0 or count == 0:
            majority = e
            count = 1
        elif majority == e:
            count += 1
        else:
            count -= 1

    return majority

majority_voting([1, 2, 1, 1, 3, 4, 1])