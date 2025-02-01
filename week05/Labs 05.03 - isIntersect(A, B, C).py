import json
from time import time
def main(a, b ,c):
    for i in a:
        if i in b and i in c:
            return True
    return False

def analyse_algo(a,b,c):
    stime = time()
    main(a,b,c)
    etime = time()
    print("execution time:", etime-stime)

a = json.loads(input())
b = json.loads(input())
c = json.loads(input())
print(main(a, b, c))
analyse_algo(a,b,c)