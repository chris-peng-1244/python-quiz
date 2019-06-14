def knapsackProblem(items, capacity):
  max_values = [[0 for _ in range(capacity + 1)] for _ in range(len(items) + 1)]

  for i in range(1, len(items) + 1):
    for j in range(capacity + 1):
      item = items[i-1]
      if j < item[1]:
        max_values[i][j] = max_values[i-1][j]
      else:
        max_values[i][j] = max(item[0] + max_values[i-1][j - item[1]], max_values[i-1][j])

  max_value = max_values[-1][-1]
  row = len(items)
  col = capacity
  selected_items = []
  while max_value > 0:
    if max_value > max_values[row-1][col]:
      selected_item = items[row-1]
      selected_items.append(row-1)
      col -= selected_item[1]
      max_value -= selected_item[0]
    row -= 1

  return [max_values[-1][-1], sorted(selected_items)]

knapsackProblem([[1,2], [4,3], [5,6], [6,7]], 10)