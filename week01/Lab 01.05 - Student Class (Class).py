"""student class"""
class student:
    """class"""
    def __init__(self,name,sex,age,id,grade):
        """init"""
        self.name = name
        self.sex = sex
        self.age = age
        self.id = id
        self. grade = float(grade)
    def __str__(self):
        """str"""
        name = "Mr " if self.sex == 'Male' else "Miss "
        name += f"{self.name} ({self.age}) ID: {self.id} GPA {self.grade:.2f}"
        return name
    
def main():
    fst = student(input(), input(), input(), input(), input())
    sec = student(input(), input(), input(), input(), input())
    trd = student(input(), input(), input(), input(), input())
    known = input()
    # print(fst.id)
    # print(sec.id)
    # print(trd.id)
    for i in [fst,sec,trd]:
        if i.id == known:
            return print(i)
    return print('Student not found')
main()