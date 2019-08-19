def maxProfitWithKTransactions(prices, k):
  if not prices:
    return 0

  best_price_matrix = build_matrix(prices, k)
  for i in range(1, k+1):
    for j in range(1, len(prices)):
      prev_profit = best_price_matrix[i][j-1]
      best_profit = get_best_profit(best_price_matrix, prices, i, j)
      best_price_matrix[i][j] = max(prev_profit, best_profit)
  return best_price_matrix[-1][-1]

def build_matrix(prices, k):
  return [
    [ 0 for _ in prices ] for _ in range(k+1)
  ]

def get_best_profit(matrix, prices, num_of_tx, price_index):
  price_now = prices[price_index]
  best_price = float("-inf")
  for i in range(price_index):
    profit = matrix[num_of_tx-1][i] - prices[i]
    best_price = max(best_price, profit)
  return best_price + price_now

print(maxProfitWithKTransactions([5,11,3,50,60,90], 2))
print(maxProfitWithKTransactions([], 1))