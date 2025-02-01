from time import time
def main(n):
    result = 0
    for i in range(1,n+1):
        result += len(str(i)) + 1
    print(result)
main(int(input()))