def main(txtA, txtB):
    n = len(txtA)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    max_length = 0
    end_index = 0
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if txtA[i - 1] == txtB[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i
            
    if max_length == 0:
        print("No common substring.")
    else:
        print(txtA[end_index - max_length:end_index])
        print(max_length)

main(input(), input())
