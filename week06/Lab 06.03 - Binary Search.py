import json

class BinarySearch:
    def __init__(self, data):
        self.data = data
        self.comparisons = 0
    
    def search(self, target_name):
        begin = 0
        end = len(self.data) - 1
        
        while begin <= end:
            mid = (begin + end) // 2
            self.comparisons += 1
            
            if self.data[mid].get_name() < target_name:
                begin = mid + 1
            elif self.data[mid].get_name() > target_name:
                end = mid - 1
            else:
                print(f"Found {target_name} at index {mid}")
                self.data[mid].print_details()
                print(f"Comparisons times: {self.comparisons}")
                return
        
        print(f"{target_name} does not exists.")
        print(f"Comparisons times: {self.comparisons}")

class Student:
    def __init__(self, std_id, name, gpa):
        self.__std_id = std_id
        self.__name = name
        self.__gpa = gpa

    def get_std_id(self):
        return self.__std_id
    
    def get_name(self):
        return self.__name
    
    def get_gpa(self):
        return self.__gpa
    
    def print_details(self):
        print(f"ID: {self.get_std_id()}")
        print(f"Name: {self.get_name()}")
        print(f"GPA: {self.get_gpa():.2f}")

def main():
    l1st = json.loads(input())
    target_name = input()
    outlist = []
    for i in l1st:
        outlist.append(Student(i["id"], i["name"], i["gpa"]))
    searcher = BinarySearch(outlist)
    searcher.search(target_name)

main()
