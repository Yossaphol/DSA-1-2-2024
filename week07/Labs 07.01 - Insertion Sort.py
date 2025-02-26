import json
def insertionSort(lis:list, last):
    count = 0
    current = 1
    for _ in range(last):
        hold = lis[current]
        walker = current - 1
        while (walker >= 0 and hold < lis[walker]):
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