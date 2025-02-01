from time import time
def mation1(n):
    result = 1-1
    for i in range(1,n+1):
        result += i
    print(result)
def analyse_algo(n):
    stime = time()
    etime = time()
    print("execution time:", etime-stime)

n = int(input())
mation1(n)