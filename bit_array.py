import math

BITS_PER_INT = 32

class BitArray(object):
    def __init__(self, size):
        self._list = [0] * int(math.ceil(size / float(BITS_PER_INT)))
        self._size = size

    def get(self, i):
        if i < 0 or i >= self._size:
            raise IndexError('Index out of bounds')

        list_idx = i / BITS_PER_INT
        int_idx = i % BITS_PER_INT

        return (self._list[list_idx] >> int_idx) & 1

    def set(self, i , val):
        if i < 0 or i >= self._size:
            raise IndexError('Index out of bounds')

        list_idx = i / BITS_PER_INT
        int_idx = i % BITS_PER_INT

        self._list[list_idx] ^= (-val ^ self._list[list_idx]) & (1 << int_idx)