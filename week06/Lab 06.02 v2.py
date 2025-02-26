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

class ProbHash:
    def __init__(self, cap):
        self.hash_table = [None] * cap
        self.size = cap
        self.count = 0  # นับจำนวนข้อมูลที่เก็บ

    def hash(self, key):
        return key % self.size
    
    def rehash(self, key):
        return (key + 1) % self.size
    
    def insert_data(self, student: Student):
        if self.count == self.size:  # ตารางเต็ม
            print(f"The list is full. {student.get_std_id()} could not be inserted.")
        else:
            std_key = student.get_std_id()
            hashkey = self.hash(std_key)
            start = hashkey
            
            while self.hash_table[hashkey] is not None:
                hashkey = self.rehash(hashkey)
                if hashkey == start:  # วนกลับมาตำแหน่งเดิม
                    print(f"The list is full. {student.get_std_id()} could not be inserted.")

            self.hash_table[hashkey] = student
            self.count += 1  # นับจำนวนข้อมูลที่เก็บ
            print(f"Insert {std_key} at index {hashkey}")

    def search_data(self, std_id):
        hashkey = self.hash(std_id)
        start = hashkey

        while self.hash_table[hashkey] is not None:
            if self.hash_table[hashkey].get_std_id() == std_id:
                print(f"Found {std_id} at index {hashkey}")
                return self.hash_table[hashkey]
            hashkey = self.rehash(hashkey)
            
            if hashkey == start:  # วนกลับมาตำแหน่งเริ่มต้น
                break

        print(f"{std_id} does not exist.")
        return None

def main():
    import json
    size = int(input())
    hashtable = ProbHash(size)
    
    while True:
        finish = input().strip()
        if finish == "Done":
            break
        try:
            condition, data = finish.split(" = ", 1)
            if condition == "I":
                std_in = json.loads(data)
                std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
                hashtable.insert_data(std)
            elif condition == "S":
                print("------")
                student = hashtable.search_data(int(data))
                if student is not None:
                    student.print_details()
                print("------")
            else:
                print("Invalid Condition!")
        except Exception as e:
            print(f"Error: {e}")

main()
