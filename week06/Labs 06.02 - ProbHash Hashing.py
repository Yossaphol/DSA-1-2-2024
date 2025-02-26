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

    def hash(self, key):
        return key % self.size
    
    def rehash(self, key):
        return (key + 1) % self.size
    
    def insert_data(self, student: Student):
        # หาตำแหน่งที่จะ insert -> จากการ Hash
        std_key = student.get_std_id()
        hashkey = self.hash(std_key)
        # ถ้าตำแหน่งนั้นไม่ว่าง -> ข้อมูลชนกัน -> rehash -> ขยับหาตำแหน่งถัดไปจนกว่าจะว่าง
        while self.hash_table[hashkey] != None:
            hashkey = self.rehash(hashkey)
        #ถ้าตำแหน่งนั้นว่างใส่ข้อมูลเข้าไป
        self.hash_table[hashkey] = student
        print(f"Insert {std_key} at index {hashkey}")

    def search_data(self, std_id):
        hashkey = self.hash(std_id)
        start = hashkey
        
        while self.hash_table[hashkey] != None:
            if self.hash_table[hashkey].get_std_id() == std_id:
                print(f"Found {std_id} at index {hashkey}")
                return self.hash_table[hashkey]
            hashkey = self.rehash(hashkey)
            
            if hashkey == start:
                break
        
        print(f"{std_id} does not exist.")

def main():
    import json
    size = int(input())
    hashtable = ProbHash(size)
    while True:
        finish = input()
        if finish == "Done":
            break
        condition, data = finish.split(" = ")
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
main()


# s1 = Student(67070004, "A", 3.35)
# s2 = Student(67070062, "B", 2.89)
# s3 = Student(67070021, "C", 4.00)
# s4 = Student(67070004, "D", 1.43)
# s5 = Student(67070005, "E", 3.75)

# myHash = ProbHash(20)
# myHash.insert_data(s1)
# myHash.insert_data(s2)
# myHash.insert_data(s3)
# myHash.insert_data(s4)
# myHash.insert_data(s5)