#finding the min combination required to full the amount using dp

def coinChange(coins: list[int], amount: int) -> int:
        m=amount
        n=len(coins)
        dp=[[float('inf') for j in range(m + 1)] for i in range(n + 1)]
        for i in range(n+1):
            dp[i][0]=0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if coins[i-1]>j:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=min(dp[i-1][j],1+dp[i][j-coins[i-1]])
        return dp[n][m] if dp[n][m] != float('inf') else -1
coins = [1,2,5]
amount = 11
print(coinChange(coins,amount))

'''
#method 2
n=[1,5,7]
b=18
dp=[float('inf')]*(b+1)
dp[0]=0
for i in n:
    for j in range(i,b+1):
        dp[j]=min(dp[j],dp[j-i]+1)
if dp[b]==float('inf'):
    print(-1)
else:
    print(dp[b])
'''
    