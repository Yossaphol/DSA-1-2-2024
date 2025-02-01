from time import time
def summation1(n):
    result = 0
    for i in range(1,n+1):
        result += i
    print(result)
def summation2(n):
    print(int(n*(n+1)/2))
def analyse_algo(n):
    stime = time()
    summation2(n)
    etime = time()
    print("execution time:", etime-stime)

n = int(input())
summation2(n)