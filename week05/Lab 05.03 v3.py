import json
import random
from time import time

def main(a, b, c):
    for i in a:
        if i in b and i in c:
            return True  # Best case: เจอตั้งแต่ตัวแรก
    return False  # Worst case: วนจนครบแล้วยังไม่เจอ

def analyse_algo(n):
    # สร้างข้อมูลจำลองแบบ worst case
    a = list(range(n))
    b = list(range(n, 2*n))
    c = list(range(2*n, 3*n))
    
    stime = time()
    main(a, b, c)
    etime = time()
    
    print(f"Execution time for worst case n={n}: {etime - stime} seconds")

# รับค่าจำนวนข้อมูลจาก input
n = int(input("Enter list size: "))
analyse_algo(n)
