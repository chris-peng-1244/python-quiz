from random import random
from bisect import bisect_left

def distribute(nums, probs):
    r = random()

    s = 0
    for num, prob in zip(nums, probs):
        s += prob
        if s >= r:
            return num

def preprocess(probs):
    lst = []

    current_val = 0
    for p in probs:
        current_val += p
        lst.append(current_val)

    return lst

def distribute2(nums, arr):
    r = random()
    i = bisect_left(arr, r)
    return nums[i]