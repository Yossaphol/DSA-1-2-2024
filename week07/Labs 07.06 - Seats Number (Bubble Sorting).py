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
            # (hold[0] < lis[walker][0] or (hold[0] == lis[walker][0]) and int(hold[1:]) < int(lis[walker][1:]))):
            if lis[walker][0] < lis[walker - 1][0] or (lis[walker][0] == lis[walker - 1][0] and (int(lis[walker][1:]) < int(lis[walker - 1][1:]))):
                sorted = False
                lis[walker - 1], lis[walker] = lis[walker], lis[walker - 1]
            walker -= 1
        print(lis)
        if sorted:
            break
        current += 1
    print(f"Comparison times: {count}")
BubbleSort(json.loads(input()), int(input()))