import json
def SelectionSort(lis:list, last):
    current = 0
    count = 0
    for _ in range(last):
        smallest = current
        walker = current + 1
        while (walker <= last):
            if lis[walker] < lis[smallest]:
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
