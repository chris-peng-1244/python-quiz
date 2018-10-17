from math import inf

def max_profit(k, prices):
    n = len(prices)
    dp = [[0 for _ in range(n)] for _ in range(k+1)]

    for i in range(k+1):
        dp[i][0] = 0

    for j in range(n):
        dp[0][j] = 0

    for i in range(1, k + 1):
        best_so_far = -inf
        for j in range(1, n):
            best_so_far = max(best_so_far, dp[i-1][j-1] - prices[j-1])
            dp[i][j] = max(prices[j] + best_so_far, dp[i][j-1])

    return dp[k][n-1]