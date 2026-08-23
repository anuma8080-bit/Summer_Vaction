a = int(input())

if a == 0:
    print(0)
elif a == 1:
    print(1)
else:
    dp = [0] * (a + 1)
    dp[1] = 1

    for i in range(2, a + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    print(dp[a])