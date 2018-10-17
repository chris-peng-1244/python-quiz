from collections import defaultdict

def array_two_elements_naive(arr):
    d = defaultdict(int)
    for num in arr:
        d[num] += 1
    
    result = []
    for num, count in d.items():
        if count == 1:
            result.append(num)
    return result

def array_two_elements(arr):
    xor = 0
    for num in arr:
        xor = xor ^ num

    # Get rightmost set bit
    xor = xor & -xor

    rets = [0, 0]
    for num in arr:
        if num & xor:
            rets[0] = rets[0] ^ num
        else:
            rets[1] = rets[1] ^ num
    return rets


print(array_two_elements([2, 4, 6, 8, 10, 2, 6, 10]))