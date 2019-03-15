def buy_and_sell_with_fee(arr, fee):
  current_max_profit = 0
  hold = -arr[0]
  for price in arr[1:]:
    current_max_profit = max(current_max_profit, hold + price - fee)
    hold = max(hold, current_max_profit - price)
  return current_max_profit


buy_and_sell_with_fee([1,3,2,8,4,10], 2)