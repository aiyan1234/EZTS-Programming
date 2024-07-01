#finding the differnet ways of combination using dp
def change(amount: int, coins: list[int]) -> int:
        m=amount
        n=len(coins)
        dp=[[0 for j in range(m+1)] for i in range(n+1)]
        for i in range(n+1):
            dp[i][0]=1
        for i in range(1,n+1):
            for j in range(1,m+1):
                if coins[i-1]>j:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-coins[i-1]]
        return dp[n][m]
amount = 5
coins = [1,2,5]
print(change(amount,coins))