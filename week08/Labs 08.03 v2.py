import json
def find_stations():
    cities = json.loads(input())
    i = int(input())
    stations = [ json.loads(input()) for _ in range(i)]


    result  = []
    time = 0

    while cities:
        max = 0
        temp = {}
        for i in stations:
            cnt = len(set(cities) & set(i["Cities"]))
            if cnt > max:
                max = cnt
                temp = i
        if temp:
            cities = set(cities) - set(temp["Cities"])
            result.append(temp["Name"])
        time += 1
        if time > i:
            break
    print(sorted(result))

find_stations()