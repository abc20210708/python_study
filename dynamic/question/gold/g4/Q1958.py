## LCS 3 (골드 4)
#  참고 코드 https://www.acmicpc.net/source/65656039

string1 = " " + input()
string2 = " " + input()
string3 = " " + input()

dp = [[[0 for _ in range(len(string1))] for _ in range(len(string2))] for _ in range(len(string3))]

for k in range(1, len(string3)):
    for i in range(1, len(string2)):
        for j in range(1, len(string1)):
            if string2[i] == string1[j] and string1[j] == string3[k]:
                dp[k][i][j] = dp[k - 1][i - 1][j - 1] + 1
            else:
                dp[k][i][j] = max(dp[k][i - 1][j], dp[k][i][j - 1], dp[k - 1][i][j])


print(dp[-1][-1][-1])