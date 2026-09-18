# Longest Palindromic Substring

# Time Complexity: O(n^2)
# Space Complexity: O(n^2)

def longest_palindromic_subsequence(s: str) -> str:
    n = len(s)

    # dp[i][j] = s[i..j] aralığındaki en uzun palindromik subsequence UZUNLUĞU
    dp = [[0] * n for _ in range(n)]

    # base case
    for i in range(n):
        dp[i][i] = 1

    # DP tablosunu doldurarak uzunluğu bulma işi
    # length = len(substring) imiz
    for length in range(2, n + 1):          # 2'den n'e kadar
        for i in range(n - length + 1):
            j = i + length - 1               # sağ sınır

            # uç karakterler aynı
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i + 1][j - 1]

            # uç karakterler farklı
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    
    print(dp[0][8])

    # DP tablosundan geri yürüyerek sayının kendisini elde etme işi
    i = 0
    j = n - 1

    left_part = []     
    right_part = []    

    while i <= j:
        # Eğer iki uç karakter eşitse
        if s[i] == s[j]:
            # Ortadaysak (tek karakter kalmışsa)
            if i == j:
                left_part.append(s[i])
            else:
                left_part.append(s[i])
                right_part.append(s[j])
            i += 1
            j -= 1

        # Eğer eşit değillerse DP tablosuna bak ve yönü belirle
        elif dp[i + 1][j] > dp[i][j - 1]:
            i += 1
        else:
            j -= 1

    # Sağ taraf ters sırada eklendiği için ters çevir
    return "".join(left_part + right_part[::-1])

# print(longest_palindromic_subsequence("bbaba")) # output: "bbb"
print(longest_palindromic_subsequence("BBABCBCAB")) # output: "BABCBAB"