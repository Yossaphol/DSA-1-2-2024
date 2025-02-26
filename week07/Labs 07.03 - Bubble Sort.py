import json
def BubbleSort(lis:list, last):
    current = 0
    count = 0
    sorted = False
    while (current <= last and sorted is False):
        walker = last
        sorted = True
        while walker > current:
            count += 1
            if (lis[walker] < lis[walker - 1]):
                sorted = False
                # hold = lis[walker]
                # lis[walker] = lis[walker - 1]
                # lis[walker - 1] = hold
                # ตัวหน้า , ตัวหลัง = ตัวหลัง,ตัวหน้า
                lis[walker - 1], lis[walker] = lis[walker], lis[walker - 1]
            walker -= 1
        print(lis)
        if sorted:
            break
        current += 1
    print(f"Comparison times: {count}")
BubbleSort(json.loads(input()), int(input()))