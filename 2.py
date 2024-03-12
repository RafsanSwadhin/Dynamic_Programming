# bottom up approach ,tabulation 
dp = [0]*(11)
dp[0] = 0
dp[1] =1
print(dp)
for i in range(2,9):
    dp[i] = dp[i-1] + dp[i-2]
    print(dp)

print(dp[7])