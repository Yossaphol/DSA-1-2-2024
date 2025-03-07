import json

def findStations(station_dict, all_cities):
    uncovered_cities = set(all_cities)
    selected_stations = []
    
    while uncovered_cities:
        best_station = None
        best_coverage = set()
        
        for station, cities in station_dict.items():
            coverage = uncovered_cities & set(cities)
            if len(coverage) > len(best_coverage):
                best_station = station
                best_coverage = coverage
        
        if best_station is None:
            break
        
        selected_stations.append(best_station)
        uncovered_cities -= best_coverage
    
    return sorted(selected_stations)

all_cities = json.loads(input().strip())
n = int(input().strip())
station_dict = {}

for _ in range(n):
    station_info = json.loads(input().strip())
    station_dict[station_info["Name"]] = station_info["Cities"]

print(findStations(station_dict, all_cities))
