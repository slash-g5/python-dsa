def longest_common_subsequence(str1, str2):
    dp = [[0 for _ in range(len(str2))] for _ in range(len(str1))]
    if str2[0] == str1[0]:
        dp[0][0] = 1
    for i in range(1, len(str1)):
        if str1[i] == str2[0]:
            dp[i][0] = 1
        else:
            dp[i][0] = dp[i-1][0]
    for i in range(1, len(str2)):
        if str2[i] == str1[0]:
            dp[0][i] = 1
        else:
            dp[0][i] = dp[0][i-1]
    for i in range(1, len(str1)):
        for j in range(1, len(str2)):
            if str1[i] == str2[j]:
                dp[i][j] = max([1 + dp[i-1][j-1], dp[i-1][j], dp[i][j-1]])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[len(str1)-1][len(str2)-1]


if __name__ == "__main__":
    print(longest_common_subsequence("fkfmpdrjenoiwjkdfvdezkmphqgv", "zzfgkkubpolwbzgxkqarlfwmqkbz"))
