def longest_common_substring(txtA, txtB):
    max_length = 0
    substring = ""
    
    for i in range(len(txtA)):
        for j in range(i + 1, len(txtA) + 1):
            if txtA[i:j] in txtB and j - i > max_length:
                max_length = j - i
                substring = txtA[i:j]
    
    if max_length == 0:
        print("No common substring.")
    else:
        print(substring)
        print(max_length)

longest_common_substring(input(), input())