def zigzagTraverse(array):
	result = [array[0][0]]
	i = 0
	j = 0
	momentum = 'down'
	while True:
		i, j, momentum = zigzag(array, i, j, momentum)
		result.append(array[i][j])
		if momentum == 'stop':
			break
		
	return result

def zigzag(array, row, col, momentum):
	if row == len(array) - 1 and col == len(array[0]) - 1:
		return (row, col, 'stop')
	if momentum == 'up':
		return up(array, row, col)
	return down(array, row, col)	

def up(array, row, col):
	if col == len(array[0]) - 1:
		return (row + 1, col, 'down')
	if row == 0:
		return (row, col + 1, 'down')
	return (row - 1, col + 1, 'up')

def down(array, row, col):
	if row == len(array) - 1:
		return (row, col + 1, 'up')
	if col == 0:
		return (row + 1, col, 'up')
	return (row + 1, col - 1, 'down')
zigzagTraverse([
  [1,3,4,10],
  [2,5,9,11],
  [6,8,12,15],
  [7,13,14,16],
])