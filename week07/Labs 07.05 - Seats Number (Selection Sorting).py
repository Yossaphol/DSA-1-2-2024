import json
def SelectionSort(lis:list, last):
    current = 0
    count = 0
    for _ in range(last):
        smallest = current
        walker = current + 1
        while (walker <= last):
            # (hold[0] < lis[walker][0] or (hold[0] == lis[walker][0]) and int(hold[1:]) < int(lis[walker][1:]))):
            if lis[walker][0] < lis[smallest][0] or (lis[walker][0] == lis[smallest][0] and (int(lis[walker][1:]) < int(lis[smallest][1:]))):
                smallest = walker
            count += 1
            walker += 1
        # exchange(current,smallest)
        hold = lis[smallest]
        lis[smallest] = lis[current]
        lis[current] = hold
        current += 1
        print(lis)
    print(f"Comparison times: {count}")
SelectionSort(json.loads(input()),int(input()))
