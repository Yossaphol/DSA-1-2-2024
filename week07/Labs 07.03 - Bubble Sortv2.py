import json
def BubbleSort(lis:list, last):
    current = 0
    count = 0
    sorted = False
    for current in range(last):
        sorted = True
        walker = last
        while walker > current:
            count += 1 
            if lis[walker] < lis[walker - 1]:
                sorted = False
                hold = lis[walker]
                lis[walker] = lis[walker - 1]
                lis[walker - 1] = hold
            walker -= 1
        print(lis)
        if sorted:
            break
    print(f"Comparison times: {count}")

BubbleSort(json.loads(input()), int(input()))
