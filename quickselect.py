def quickselect(array, k):
    # Write your code here.
	kIndex = k - 1
	return quickselectHelper(array, 1, len(array) - 1, kIndex)

def quickselectHelper(array, left, right, kIndex):
	pivotIndex = partition(array, left, right)
	if pivotIndex == kIndex:
		return array[kIndex]
	elif pivotIndex > kIndex:
		return quickselectHelper(array, left, pivotIndex-1, kIndex)
	else:
		return quickselectHelper(array, pivotIndex+2, right, kIndex)

def partition(array, left, right):
	pivot = left-1
	while left <= right:
		if array[left] > array[pivot] and array[right] < array[pivot]:
			array[left], array[right] = array[right], array[left]
		if array[left] <= array[pivot]:
			left += 1
		if array[right] >= array[pivot]:
			right -= 1
	array[pivot], array[right] = array[right], array[pivot]
	return right

print(quickselect([8,3,2,5,1,7,4,6], 5))