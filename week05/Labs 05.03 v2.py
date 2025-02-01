import json
import random
from time import time

def main(a, b ,c):
    for i in a:
        if i in b and i in c:
            return True
    return False

def analyse_algo(n):
    # สร้างข้อมูลจำลอง
    a = [random.randint(0, n*2) for _ in range(n)]
    b = [random.randint(0, n*2) for _ in range(n)]
    c = [random.randint(0, n*2) for _ in range(n)]
    
    stime = time()
    main(a, b, c)
    etime = time()
    
    print(f"Execution time for n={n}: {etime - stime} seconds")

# รับค่าจำนวนข้อมูลจาก input
n = int(input("Enter list size: "))
analyse_algo(n)
