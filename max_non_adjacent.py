def max_non_adjacent(nums: list) -> int:
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]

    max: int = None
    index: int = -1
    for i in range(len(nums)):
        if max is None or nums[i] > max:
            max = nums[i]
            index = i

    second_max: int = None
    for i in range(len(nums)):
        if i == index or i == (index-1) or i == (index + 1):
            continue
        elif second_max is None or second_max < nums[i]:
            second_max = nums[i]

    return max + second_max


def largest_non_adjacent(arr):
    if len(arr) <= 2:
        return max(0, max(arr))

    cache = [0 for i in arr]
    cache[0] = max(0, arr[0])
    cache[1] = max(cache[0], arr[1])

    for i in range(2, len(arr)):
        num = arr[i]
        cache[i] = max(num + cache[i - 2], cache[i - 1])
    return cache[-1]


def largest_non_adjacent_constant_space(arr):
    if len(arr) <= 2:
        return max(0, max(arr))

    max_excluding_last = max(0, arr[0])
    max_including_last = max(max_excluding_last, arr[1])

    for num in arr[2:]:
        prev_max_including_last = max_including_last
        max_including_last = max(max_including_last, max_excluding_last + num)
        max_excluding_last = prev_max_including_last

    return max(max_including_last, max_excluding_last)


print(max_non_adjacent([2, 4, 6, 8]))
print(largest_non_adjacent([5, 1, 1, 5]))
print(largest_non_adjacent_constant_space([5, 1, 1, 5]))
