import json
def insertionSort(lis:list, last):
    count = 0
    current = 1
    for _ in range(last):
        hold = lis[current]
        walker = current - 1
        while (walker >= 0 and (hold[0] < lis[walker][0] or (hold[0] == lis[walker][0]) and int(hold[1:]) < int(lis[walker][1:]))):
            lis[walker + 1] = lis[walker]
            walker -= 1
            count += 1
        if walker >= 0:
            count += 1
        lis[walker + 1] = hold
        current += 1
        print(lis)
    print(f"Comparison times: {count}")
insertionSort(json.loads(input()),int(input()))